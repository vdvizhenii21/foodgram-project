from django.urls import include, path
from .views import TagsViewSet, RecipeViewSet
from rest_framework.routers import DefaultRouter

app_name = "recipies"

router = DefaultRouter()
router.register("tags", TagsViewSet, basename="tags")
router.register("recipes", RecipeViewSet, basename="recipes")


urlpatterns = [
    path("", include(router.urls)),
]
