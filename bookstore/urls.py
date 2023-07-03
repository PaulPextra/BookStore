from django.urls import path
from bookstore import views

urlpatterns = [
    path('superadmin/books/', views.add_book),
    path('superadmin/books/<str:book_title>/', views.modify_book),
    path('books/', views.fetch_books),
    path('books/<str:title>/', views.fetch_book_by_title),
    path('books/<str:category>/', views.fetch_book_by_category),
    path('books/<str:book_author>/', views.fetch_book_by_author),
]