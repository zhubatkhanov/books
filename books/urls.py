from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/<int:category_id>/', views.books, name='books_filter'),
    path('book_item/<int:pk>', views.display_about_book, name='book_item'),
    path('favorites/', views.favorites, name='favorites'),
    path('books/favorite/add/<int:book_id>/', views.favorite_add, name='favorite_add'),
    path('books/favorite/remove/<int:book_id>/', views.favorite_remove, name='favorite_remove'),
]