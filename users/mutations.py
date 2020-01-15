import graphene
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from .models import User
from rooms.models import Room


class CreateAccountMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, email, password, first_name=None, last_name=None):
        try:
            User.objects.get(email=email)
            return CreateAccountMutation(ok=False, error="User already exists")
        except User.DoesNotExist:
            try:
                User.objects.create_user(email, email, password)
                return CreateAccountMutation(ok=True)
            except Exception:
                return CreateAccountMutation(error="Can't create user.", ok=False)


class LoginMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()
    pk = graphene.Int()
    error = graphene.String()

    def mutate(self, info, email, password):
        user = authenticate(username=email, password=password)
        if user:
            token = jwt.encode({"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256")
            return LoginMutation(token=token.decode("utf-8"), pk=user.pk)
        else:
            return LoginMutation(error="Wrong username/password")


class ToggleFavsMutation(graphene.Mutation):
    class Arguments:
        room_id = graphene.Int(required=True)

    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, room_id):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("You need to be logged in")
        try:
            room = Room.objects.get(pk=room_id)
            if room in user.favs.all():
                user.favs.remove(room)
            else:
                user.favs.add(room)
            return ToggleFavsMutation(ok=True)
        except Room.DoesNotExist:
            return ToggleFavsMutation(ok=False, error="Room not found")


class EditProfileMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, first_name=None, last_name=None, email=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("You need to be logged in")
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email and email != user.email:
            try:
                User.objects.get(email=email)
                return EditProfileMutation(ok=False, error="That email is taken")
            except User.DoesNotExist:
                user.email = email
        user.save()
        return EditProfileMutation(ok=True)
