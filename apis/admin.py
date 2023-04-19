from django.contrib import admin
from . import models

list_models = [models.Author, models.Article, models.Category]
admin.site.register(list_models)
