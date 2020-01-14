import graphene
from graphene_django import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):

    rooms = graphene.List("rooms.schema.RoomType")

    class Meta:
        model = User
