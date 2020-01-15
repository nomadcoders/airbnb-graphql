import graphene
from graphene_django import DjangoObjectType
from .models import Room


class RoomType(DjangoObjectType):

    is_fav = graphene.Boolean()

    class Meta:
        model = Room

    def resolve_is_fav(room, info):
        user = info.context.user
        if user.is_authenticated:
            return room in user.favs.all()
        return False


class RoomListResponse(graphene.ObjectType):

    arr = graphene.List(RoomType)
    total = graphene.Int()
