from django.shortcuts import render, HttpResponseRedirect
from .models import Book, BookCategory, Favorite
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'books/index.html')


def books(request, category_id=None):
    if category_id:
        category = BookCategory.objects.get(id=category_id)
        book = Book.objects.filter(category=category)
        if category.name == 'Все книги':
            book=Book.objects.all()
    else:
        book = Book.objects.all()

    context = {
        'title': 'Books - Catalog',
        'categories': BookCategory.objects.all(),
        'books': book,
    }
    return render(request, 'books/books.html', context)


def display_about_book(request, pk=None):
    if pk:
        book_item = Book.objects.get(pk=pk)
    else:
        book_item = ''

    context = {
        'title': 'About book',
        'book_item': book_item,
    }

    return render(request, 'books/about.html', context)

def favorites(request):
    context = {
        'favorites': Favorite.objects.all(),
    }
    return render(request, 'books/favorites.html', context)


@login_required
def favorite_add(request, book_id):
    book = Book.objects.get(id = book_id)
    favorites = Favorite.objects.filter(user=request.user, book=book)
    if not favorites.exists():
        Favorite.objects.create(user=request.user, book=book, quantity=1)
    else:
        favorite = favorites.first()
        favorite.quantity += 1
        favorite.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required()
def favorite_remove(request, book_id):
    favorite = Favorite.objects.get(id = book_id)
    favorite.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])