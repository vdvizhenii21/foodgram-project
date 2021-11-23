from rest_framework import serializers
from .models import Tag, Ingredient, Recipe, IngredientItem
from drf_extra_fields.fields import Base64ImageField
from rest_framework.fields import CharField
from django.db import transaction
from django.db.models.query import QuerySet
from django.shortcuts import get_list_or_404, get_object_or_404


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag


class IngridientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Ingredient


class IngridientItemSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only=True, source='Ingredient'
    )
    name = CharField(source='ingredient.name')
    dimension = CharField(source="ingredient.dimension")
    class Meta:
        model = IngredientItem
        fields = (
            "id",
            "name",
            "dimension",
            "amount",
        )
        

class RecipeSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    tag = TagSerializer(many=True)
    ingredient = IngridientItemSerializer(many=True, source='item_ingredients')
    class Meta:
        fields = ['id', 'title', 'tag', 'author', 'ingredient','description', 'cooking_time', 'image']
        model = Recipe
    
   
    def create(self, validated_data):
