from django.contrib import admin
from .models import Book, BookCategory, Favorite

# Register your models here.
admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Favorite)
