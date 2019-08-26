from django.contrib import admin
from .models import Item, Category, Tag, Arrow
# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Arrow)