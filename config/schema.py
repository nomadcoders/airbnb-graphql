import graphene
from rooms import schema as rooms_schema
from users import schema as users_schema


class Query(rooms_schema.Query, users_schema.Query, graphene.ObjectType):
    pass


class Mutation(users_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
