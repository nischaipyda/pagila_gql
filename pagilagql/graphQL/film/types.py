from django.db import models
from graphene import relay, List, ID
from graphene_django import DjangoObjectType
from film.models import Film, Language, Category, FilmCategory


class LanguageType(DjangoObjectType):
    class Meta:
        model = Language
        fields = ('name',)

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('name',)

class FilmNode(DjangoObjectType):

    category = List(CategoryType, id=ID(), description="Category of film")

    class Meta:
        model = Film
        filter_fields = ['title', 'release_year']
        interfaces = (relay.Node,)
    
    def resolve_category(_, info, id):
        category_list = []
        categories = FilmCategory.objects.filter(film_id=id)

        for category in categories:
            category_list.append(category.category_id)

        return category_list

class FilmConnection(relay.Connection):
    class Meta:
        node = FilmNode

