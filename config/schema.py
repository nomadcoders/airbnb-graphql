import graphene
from rooms import schema as rooms_schema


class Query(rooms_schema.Query, graphene.ObjectType):
    pass


class Mutation:
    pass


schema = graphene.Schema(query=Query)
