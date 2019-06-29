from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Safer, but more complex method
# from django.contrib.auth import get_user_model
# User = get_user_model()

from datetime import date

class Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ='categories'

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])


class Book(models.Model):
    
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=200)
    
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    url_address = models.URLField(max_length=1000, unique=True, help_text='Enter the url for the book')

    add_date = models.DateTimeField(auto_now_add=True)

    category = models.ManyToManyField(Category, help_text='Select a category for this book')

    class Meta:
        ordering = ['-add_date']

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return self.url_address

    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])
    
    display_category.short_description = 'Category'

class Favorite(models.Model):

    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)

    # def get_absolute_url(self):
    #     return render('favorite-added', args=[str(self.id)])

    # def __str__(self):
    #     return f"{self.user}|{self.favorite_book}"

    # class Meta:
    #     unique_together = [ 'user', 'favorite_book' ]
     












