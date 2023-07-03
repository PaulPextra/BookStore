from django.contrib import admin
from bookstore.models import Book, Author

admin.site.register(Book)
admin.site.register(Author)