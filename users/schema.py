import graphene
from .types import UserType
from .models import User


class Query(object):

    user = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        return User.objects.get(id=id)
