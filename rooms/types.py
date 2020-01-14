import graphene
from graphene_django import DjangoObjectType
from .models import Room


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class RoomListResponse(graphene.ObjectType):

    arr = graphene.List(RoomType)
    total = graphene.Int()
