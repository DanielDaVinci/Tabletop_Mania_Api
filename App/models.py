from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404

from core import storage_backends


class MaterialManager(models.Manager):
    def find_by_id(self, id: int):
        try:
            vote = self.filter(pk__exact=id)
        except ObjectDoesNotExist:
            raise Http404
        return vote

    def search_by_name(self, name: str):
        return self.filter(name__contains=name)

    def get_all_in_range(self, start: int, end: int):
        result = self.all()
        start = max(0, start - 1)
        end = min(result.count(), max(start + 1, end))
        return result[start: end]


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(storage=storage_backends.MaterialStorage, blank=True, null=True)

    objects = MaterialManager()

    def __str__(self):
        return self.name


class GameManager(models.Manager):
    def find_by_id(self, id: int):
        try:
            vote = self.filter(id__exact=id)
        except ObjectDoesNotExist:
            raise Http404
        return vote

    def search_by_name(self, name: str):
        return self.filter(name__contains=name)


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(storage=storage_backends.GameStorage, blank=True, null=True)
    materials = models.ManyToManyField(Material)

    objects = GameManager()

    def __str__(self):
        return self.name
