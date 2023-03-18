from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class MaterialManager(models.Manager):
    def find_by_id(self, id: int):
        try:
            vote = self.filter(pk__exact=id)
        except ObjectDoesNotExist:
            raise Http404
        return vote

    def search_by_title(self, title):
        return self.filter(title__contains=title)

    def get_all_in_range(self, start: int, end: int):
        result = self.all()
        start = max(0, start - 1)
        end = min(result.count(), max(start + 1, end))
        return result[start: end]


class Material(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="images/")

    objects = MaterialManager()

    def __str__(self):
        return self.title


class GamenManager(models.Manager):
    def find_by_id(self, id: int):
        try:
            vote = self.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404
        return vote

    def search_by_title(self, title: str):
        return self.filter(title__contains=title)


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    materials = models.ManyToManyField(Material)

    objects = GamenManager()

    def __str__(self):
        return self.title
