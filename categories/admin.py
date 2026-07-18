from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug', 'date_creation')
    search_fields = ('nom', 'description')
    prepopulated_fields = {'slug': ('nom',)}
