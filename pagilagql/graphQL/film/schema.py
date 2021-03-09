import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .types import FilmNode, CategoryType
from film.models import Film, Category


class FilmQueries(graphene.ObjectType):
    all_films = DjangoFilterConnectionField(FilmNode, description="List of all films. [Optional filter arguments - title, release year]")
    all_film_categories = graphene.List(CategoryType, description="List of all categories")
    
    film_by_id = graphene.Field(FilmNode, id=graphene.ID(), description="Get Film by ID")

    def resolve_film_by_id(_, info, id):
        return Film.objects.get(pk=id)
    
    def resolve_all_film_category(_, info):
        return Category.objects.all()

    # def resolve