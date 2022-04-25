from django.db import models


class PasswordModel(models.Model):
    title = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title} {self.username}'
