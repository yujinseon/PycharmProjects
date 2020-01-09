from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','name','url')

admin.site.register(Bookmark, BookmarkAdmin)