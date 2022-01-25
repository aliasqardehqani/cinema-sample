from django.contrib import admin

from .models import Foods, Comment, Sales

# Register your models here.

admin.site.register(Foods)
admin.site.register(Comment)
admin.site.register(Sales)

