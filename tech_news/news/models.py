from django.db import models


class News(models.Model):

    def __str__(self):
        return f'{self.title} : {self.text}'

    title = models.CharField()
    text = models.CharField()


class Tag(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField()
    news = models.ManyToManyField(News)
