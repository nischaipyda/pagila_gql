# from django.db.models import fields
# from graphene import ObjectType, List, Field, String, Schema, relay
# from graphene_django import DjangoObjectType

# from film.models import Film, Language

# class LanguageType(DjangoObjectType):
#     class Meta:
#         model = Language        

# class FilmType(DjangoObjectType):
#     class Meta:
#         model = Film
#         interfaces = (relay.Node, )
#         fields = '__all__'
# class FilmConnection(relay.Connection):
#     class Meta:
#         node = FilmType

# class Query(ObjectType):
#     ''' Hello this is docstring. '''
#     all_films = relay.ConnectionField(FilmConnection)
#     language_by_id = List(LanguageType)

#     film_by_id = Field(FilmType, name=String())

#     def resolve_film_by_id(root, info, name):
#         return Film.objects.get(title= name)

#     def resolve_all_films(root, info, **kwargs):
#         return Film.objects.all()

#     def resolve_language_by_id(root, info, id):
#         try:
#             return Language.objects.get(id=id)
#         except Language.DoesNotExist:
#             return None

# schema = Schema(query=Query)



import graphene
from graphQL.film.schema import FilmQueries

class Query(FilmQueries, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)