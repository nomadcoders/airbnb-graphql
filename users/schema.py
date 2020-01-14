import graphene
from .types import UserType
from .mutations import CreateAccountMutation
from .queries import resolve_user


class Query(object):

    user = graphene.Field(
        UserType, id=graphene.Int(required=True), resolver=resolve_user
    )


class Mutation(object):

    create_account = CreateAccountMutation.Field()
