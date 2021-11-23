from django.contrib import admin
from .models import Recipe, Tag, Ingredient, IngredientItem


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    empty_value_display = "-пусто-"

class IngredientInline(admin.TabularInline):
    model = IngredientItem
    fields = ["ingredient", "amount"]

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "title", "image", "cooking_time")
    search_fields = ("title",)
    empty_value_display = "-пусто-"
    inlines = [IngredientInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "dimension")
    search_fields = ("name",)
    empty_value_display = "-пусто-"


@admin.register(IngredientItem)
class IngredientItemAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "recipe",
        "ingredient",
        "amount",
    )
    list_display_links = ("pk", "recipe")
    list_filter = (
        "recipe",
        "ingredient",
    )