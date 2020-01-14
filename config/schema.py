import graphene


class Query(graphene.ObjectType):
    pass


class Mutation:
    pass


schema = graphene.Schema(query=Query)
