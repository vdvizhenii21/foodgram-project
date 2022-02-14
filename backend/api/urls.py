from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import (IngredientViewSet, RecipeViewSet, TagViewSet)

router_v1 = DefaultRouter()

router_v1.register('ingredients', IngredientViewSet)
router_v1.register('recipes', RecipeViewSet)
router_v1.register('tags', TagViewSet)


urlpatterns = [
    path(
        '', include(router_v1.urls),
    ),
    #re_path(
    #    r'recipes/(?P<recipe_id>\d+)/favorite/',
    #    FavoriteCreateDestroy.as_view(),
    #    name='favorite',
    #),
    #re_path(
    #    r'recipes/(?P<recipe_id>\d+)/shopping_cart/',
    #    ShoppingListCreateDestroy.as_view(),
    #    name='shopping-list',
    #),
]
