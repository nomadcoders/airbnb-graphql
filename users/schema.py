import graphene
from .types import UserType
from .mutations import (
    CreateAccountMutation,
    LoginMutation,
    ToggleFavsMutation,
    EditProfileMutation,
)
from .queries import resolve_user, resolve_me


class Query(object):

    user = graphene.Field(
        UserType, id=graphene.Int(required=True), resolver=resolve_user
    )
    me = graphene.Field(UserType, resolver=resolve_me)


class Mutation(object):

    create_account = CreateAccountMutation.Field()
    login = LoginMutation.Field()
    toggle_favs = ToggleFavsMutation.Field()
    edit_profile = EditProfileMutation.Field()
