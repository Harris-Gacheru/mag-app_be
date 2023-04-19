from django.db import models

class Author(models.Model):
    name = models.CharField("Author Name", max_length=255)
    email = models.EmailField("Author Email Address", max_length=255)
    bio = models.TextField("Author Biography")

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField("Category Name", max_length=255)
    description = models.TextField("Category Description")

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField("Article Title", max_length=255)
    content = models.TextField("Article content")
    published_on = models.DateField("Publish Date")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
