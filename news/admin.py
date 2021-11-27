from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'photo','created_at', 'updated_at', 'is_published', 'category')
	list_display_links = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'photo', 'category')
	search_fields = ('title', 'content')
	list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')
	list_display_links = ('id', 'title')
	search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)