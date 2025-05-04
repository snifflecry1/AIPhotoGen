from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

class Blog_Post(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)




