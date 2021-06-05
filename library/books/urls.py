from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.book, name='book'),
    path('loan', views.loan, name='loan'),
    path('search', views.search, name='search'),
]