from django.contrib import admin
from main.models import *

class ItemAdmin(admin.ModelAdmin):
     list_display = ('name', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
