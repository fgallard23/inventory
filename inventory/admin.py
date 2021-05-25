from django.contrib import admin

from .models import Item
from .models import Blog
from .models import Author
from .models import Entry


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','amount'] #atributo

admin.site.register(Item, ItemAdmin)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
