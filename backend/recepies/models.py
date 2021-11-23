from django.db import models
from django.core.validators import MinValueValidator
from users.models import User


class Tag(models.Model):
    name = models.CharField(db_index=True,
                            max_length=200,
                            verbose_name='тег блюда')
    colour = models.CharField(max_length=20, null=True)
    slug = models.SlugField(max_length=20,
                            unique=True,
                            verbose_name='короткая метка')
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField("Название ингредиента", max_length=100)
    dimension = models.CharField("Единица измерения", max_length=10)


class Recipe(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='recipes',
                               verbose_name='автор рецепта')
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='recipes/')
    description = models.CharField(db_index=True,
                            max_length=200,)
    ingredient = models.ManyToManyField(Ingredient,
        through="IngredientItem",
        through_fields=("recipe", "ingredient"),
        verbose_name="Ингредиенты",
    )
    tag = models.ManyToManyField(Tag, related_name="recipes")
    cooking_time = models.PositiveIntegerField("Время приготовления")


class IngredientItem(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="item_ingredients",
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="item_ingredients",
        verbose_name="Ингредиент",
    )
    amount = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1),)
    )

    class Meta:
        verbose_name = "Ингредиент итем"
        verbose_name_plural = "Ингредиент итемы"

    def __str__(self):
        return str(self.amount)