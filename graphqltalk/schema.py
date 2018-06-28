


import graphene

from rebels.schema import RebelQuery

class Query(RebelQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
