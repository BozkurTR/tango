from django.contrib import admin
from rango.models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

#admin.site.register(Category)
admin.site.register(Category, CategoryAdmin)
#admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
admin.site.register(Page, PageAdmin)
# Register your models here.

admin.site.register(UserProfile)