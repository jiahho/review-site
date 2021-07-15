from django.db import models
from core.models import TimeStampedModel
from categories.models import Category
from people.models import Person


class Movie(TimeStampedModel):

    """Movie Model Definition"""

    title = models.CharField(max_length=200, blank=True)
    year = models.IntegerField(null=True, blank=True)
    cover_image = models.ImageField(null=True)
    rating = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(
        Person, related_name="director", on_delete=models.CASCADE
    )
    cast = models.ForeignKey(Person, related_name="cast", on_delete=models.CASCADE)

    def __str__(self):
        return self.title