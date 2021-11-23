from django.shortcuts import render
from rest_framework import mixins, viewsets
from .serializers import TagSerializer, IngridientSerializer, RecipeSerializer
from .models import Tag, Ingredient, Recipe
from rest_framework.parsers import JSONParser,ParseError
from django.http import HttpResponse

class TagsViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class IngridientViewSet(viewsets.ModelViewSet):
    serializer_class = IngridientSerializer
    queryset = Ingredient.objects.all()

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
