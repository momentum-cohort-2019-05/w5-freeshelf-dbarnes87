from django.contrib import admin

from shelf.models import Category, Book

admin.site.register(Category)


# @admin.register(Category)
# class Category(admin.ModelAdmin):
#     pass

@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ('title', 'author', 'add_date', 'display_category')
