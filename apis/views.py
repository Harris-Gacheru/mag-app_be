from rest_framework import views, status, response
from . import models, serializer

# Authors List
class AuthorsAPI(views.APIView):
    def get(self, request, pk=None):
        if pk:
            authors = models.Author.objects.exclude(pk=pk)
            authors_serializer = serializer.AuthorSerializer(authors, many=True)

            # check if authors exist
            if len(authors) > 0:
                return response.Response(authors_serializer.data)
            elif len(authors) == 0:
                return response.Response({'message': 'Authors not found'}, status=status.HTTP_404_NOT_FOUND)
            
            return response.Response(authors_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: 
            authors = models.Author.objects.all()
            authors_serializer = serializer.AuthorSerializer(authors, many=True)

            # check if authors exist
            if len(authors) > 0:
                return response.Response(authors_serializer.data)
            elif len(authors) == 0:
                return response.Response({'message': 'Authors not found'}, status=status.HTTP_404_NOT_FOUND)
            
            return response.Response(authors_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Author
class AuthorAPI(views.APIView):
    def get(self, request, pk):
        try:
            author = models.Author.objects.get(pk=pk)

            if author:
                author_serializer = serializer.AuthorSerializer(author)
                return response.Response(author_serializer.data)
        except models.Author.DoesNotExist:
            return response.Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
    
# Categories
class CategoriesAPI(views.APIView):
    def get(self, request, pk=None):
        if pk:
            categories = models.Category.objects.exclude(pk=pk)
            categories_serializer = serializer.CategorySerializer(categories, many=True)

            if len(categories) > 0:
                return response.Response(categories_serializer.data)
            elif len(categories) == 0:
                return response.Response({'message': 'Categories not found'}, status=status.HTTP_404_NOT_FOUND)
            return response.Response(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            categories = models.Category.objects.all()
            categories_serializer = serializer.CategorySerializer(categories, many=True)

            if len(categories) > 0:
                return response.Response(categories_serializer.data)
            elif len(categories) == 0:
                return response.Response({'message': 'Categories not found'}, status=status.HTTP_404_NOT_FOUND)
            return response.Response(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryAPI(views.APIView):
    def get(self, request, pk):
        try:
            category = models.Category.objects.get(pk=pk)

            if category:
                category_serializer = serializer.CategorySerializer(category)
                return response.Response(category_serializer.data)
        except models.Category.DoesNotExist:
            return response.Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

class CategoryCreateAPI(views.APIView):
    def post(self, request):
        category_serializer = serializer.CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return response.Response({'message': 'Submitted successfully', 'data': category_serializer.data})
        return response.Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ArticleCreateAPI(views.APIView):
    def post(self, request):
        article_serializer = serializer.ArticleSerializer(data=request.data)
        if article_serializer.is_valid():
            article_serializer.save()
            return response.Response({'message': 'Submitted successfully', 'data': article_serializer.data})
        return response.Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArticlesAPI(views.APIView):
    def get(self, request, pk=None):
        if pk:
            articles = models.Article.objects.exclude(pk=pk)
            articles_serializer = serializer.ArticleSerializer(articles, many=True)

            if len(articles) > 0:
                return response.Response(articles_serializer.data)
            elif len(articles) == 0:
                return response.Response({'message': 'Articles not found'}, status=status.HTTP_404_NOT_FOUND)
            return response.Response(articles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif not pk:
            articles = models.Article.objects.all()
            articles_serializer = serializer.ArticleSerializer(articles, many=True)

            if len(articles) > 0:
                return response.Response(articles_serializer.data)
            elif len(articles) == 0:
                return response.Response({'message': 'Articles not found'}, status=status.HTTP_404_NOT_FOUND)
            return response.Response(articles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class ArticlesAuthorAPI(views.APIView):
    def get(self, request, author=None):
        if author:
            articles = models.Article.objects.filter(author_id=author).all()
            articles_serializer = serializer.ArticleSerializer(articles, many=True)

            if len(articles) > 0:
                return response.Response({'data': articles_serializer.data})
            elif len(articles) == 0:
                return response.Response({'message': 'Author has no articles published', 'data': []}, status=status.HTTP_404_NOT_FOUND)
            return response.Response(articles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class ArticlesCategoryAPI(views.APIView):
    def get(self, request, category=None):
        if category:
            articles = models.Article.objects.filter(category_id=category).all()
            articles_serializer = serializer.ArticleSerializer(articles, many=True)

            if len(articles) > 0:
                return response.Response(articles_serializer.data)
            elif len(articles) == 0:
                return response.Response({'message': 'Articles not found'}, status=status.HTTP_404_NOT_FOUND)
            return response.Response(articles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class ArticleAPI(views.APIView):
    def get(self, request, pk):
        try:
            article = models.Article.objects.get(pk=pk)

            if article:
                article_serializer = serializer.ArticleSerializer(article)
                return response.Response(article_serializer.data)
        except models.Article.DoesNotExist:
            return response.Response({'message': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)