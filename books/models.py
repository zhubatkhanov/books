from django.db import models
from users.models import User

# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='books_images')
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=BookCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} | {self.author} | {self.category.name}"


class Favorite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

