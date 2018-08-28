import graphene as graphene


class Query(graphene.ObjectType):
    hello = graphene.String(description="A typical hello world")

    def resolve_hello(self, info):
        return "World"

scheme = graphene.Schema(query=Query)


query_str = '''
        query SayHello {
            hello
            hello
            }
'''

result = scheme.execute(query_str)
print(result)