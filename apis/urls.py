from django.urls import path
from . import views

urlpatterns = [
    # authors
    path('authors/', views.AuthorsAPI.as_view(), name="Authors Listing"),
    path('authors/<int:pk>/', views.AuthorsAPI.as_view(), name="Exclusive Authors Listing"), # get authors excluding the selected
    path('author/<int:pk>/', views.AuthorAPI.as_view(), name="Author"),
    # categories
    path('categories/', views.CategoriesAPI.as_view(), name="Categories Listing"),
    path('categories/<int:pk>/', views.CategoriesAPI.as_view(), name="Exclusive Categories Listing"), # get categories excluding the selected
    path('category/<int:pk>/', views.CategoryAPI.as_view(), name="Category"),
    path('category/add/', views.CategoryCreateAPI.as_view(), name="Add Category"),
    # # articles
    path('articles/', views.ArticlesAPI.as_view(), name="Articles Listing"),
    path('articles/<int:pk>', views.ArticlesAPI.as_view(), name="Exclusive Articles Listing"), # get articles excluding the selected
    path('articles/author/<int:author>/', views.ArticlesAuthorAPI.as_view(), name="Author Articles Listing"),
    path('articles/category/<int:category>/', views.ArticlesCategoryAPI.as_view(), name="Category Articles Listing"),
    path('article/<int:pk>', views.ArticleAPI.as_view(), name="Article"),
    path('article/add/', views.ArticleCreateAPI.as_view(), name="Add Article"),
]