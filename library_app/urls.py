from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('books/', views.books, name='books'),

    path('add-book/', views.add_book, name='add_book'),

    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),

    path('edit-book/<int:id>/', views.edit_book, name='edit_book'),

    path('issue-book/', views.issue_book, name='issue_book'),

    path('issued-books/', views.issued_books, name='issued_books'),

    path(
        'return-book/<int:pk>/',
        views.return_book,
        name='return_book'
    ),

]