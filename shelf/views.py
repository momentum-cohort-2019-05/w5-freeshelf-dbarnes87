from django.shortcuts import render

from shelf.models import Category, Book

from django.views import generic


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