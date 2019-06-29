from django.shortcuts import render
from shelf.models import Category, Book, Favorite
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def index(request):
    """View function for home page of site."""

    book_list = Book.objects.all()
      
    category_list = Category.objects.all()

    category = Book.category

    # def book_category():
    #     for category in all_categories:
    #         return category.name


    context = {
        'book_list': book_list,
        'category': category,
        'category_list': category_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class CategoryDetailView(generic.DetailView):
    model = Category

@login_required
def user_favorites(request):
    favorites = Favorite.objects.filter(owner=request.user)

    favorites_list = []

    for favorite in favorites:
        favorites_list.append(favorite.book)

    context = {
        'favorites': favorites,
        'favorites_list': favorites_list,
    }

    return render(request, 'shelf/favorites.html', context)

@login_required
def add_to_favorites(request, pk):
    book = get_object_or_404(Book, pk=pk)

    new_favorite, created = Favorite.objects.get_or_create(book=book, owner=request.user)
    if not created:
        new_favorite.delete()
    
    context = {
        'book': book,
        'new_favorite': new_favorite,
        'created': created,
    }

    return render(request, 'shelf/favorite_added.html', context)




