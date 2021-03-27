import json

from django.db import models


class Organisation(models.Model):
    name = models.TextField(blank=True)
    subject = models.TextField(blank=True)
    logo = models.TextField(blank=True)
    _contacts = models.TextField(blank=True)

    @property
    def contacts(self):
        if self._contacts:
            return json.loads(self._contacts)
        return []

    @contacts.setter
    def contacts(self, value):
        self._contacts = json.dumps(list(dict.fromkeys(value)))


class Project(models.Model):
    name = models.TextField(blank=True)
    subject = models.TextField(blank=True)
    organization = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        related_name="projects",
        related_query_name="project",
        null=True
    )
    _images = models.TextField(blank=True)

    @property
    def images(self):
        if self._images:
            return json.loads(self._images)
        return []

    @images.setter
    def images(self, value):
        self._images = json.dumps(list(dict.fromkeys(value)))


class User(models.Model):
    email = models.TextField()
    nickname = models.TextField()
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    country = models.TextField(null=True)
    birthday = models.DateField(null=True)


