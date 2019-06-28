from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
]