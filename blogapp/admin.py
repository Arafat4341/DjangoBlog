from django.contrib import admin
from .models import Author, Category, Article, Comment


class authorModel(admin.ModelAdmin):
	list_display = ['__str__']
	search_fields = ['__str__', 'details']
	class Meta:
		Model = Author
		
admin.site.register(Author, authorModel)

class articleModel(admin.ModelAdmin):
	list_display = ['__str__', 'posted_on']
	search_fields = ['__str__', 'title']
	list_filter = ['posted_on', 'category']
	list_per_page = 10
	class Meta:
		Model = Article
admin.site.register(Article, articleModel)

class categoryModel(admin.ModelAdmin):
	list_display = ['__str__']
	search_fields = ['__str__']
	class Meta:
		Model = Category

admin.site.register(Category, categoryModel)

class commentModel(admin.ModelAdmin):
	list_display = ['__str__']
	search_fields = ['__str__']
	class Meta:
		Model = Comment

admin.site.register(Comment, commentModel)
