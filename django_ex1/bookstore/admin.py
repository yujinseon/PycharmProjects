from django.contrib import admin

# Register your models here.
from bookstore.models import Bookstore

class BookstoreAdmin(admin.ModelAdmin):
    list_display = ('code','name','author','price','url')

admin.site.register(Bookstore, BookstoreAdmin)