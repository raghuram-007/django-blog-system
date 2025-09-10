from django.contrib import admin
from blog.models import *
# Register your models here.
class Mediaadmin(admin.ModelAdmin):
    list_display=("title","content")
    search_fields=("title",)
    list_filter=("title",)
    
admin.site.register(Media,Mediaadmin)
admin.site.register(About)
admin.site.register(Category)