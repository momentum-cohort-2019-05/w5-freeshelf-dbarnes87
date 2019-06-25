from django.db import models
from django.urls import reverse
from datetime import date

class Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ='categories'


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
        return reverse('book-detail', args=[str(self.id)])










