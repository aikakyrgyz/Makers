from django.contrib import admin

# Register your models here.
from .models import *


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin, ]

# admin.site.register(Image)
# admin.site.register(Recipe)
admin.site.register(Category)