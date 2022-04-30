from django.contrib import admin
from .models import *
# Register your models here.

class PostImageInline(admin.TabularInline):
    model = Image
    max_num = 10
    min_num = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, ]

admin.site.register(Category)
