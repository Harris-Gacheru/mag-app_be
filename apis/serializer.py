from rest_framework import serializers
from . import models

class AuthorSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only = True)

    class Meta:
        model = models.Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only = True)

    class Meta:
        model = models.Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only = True)
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = models.Article
        fields = '__all__'