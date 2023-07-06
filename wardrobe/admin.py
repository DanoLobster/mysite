from django.contrib import admin
from .models import Clothing

#@admin.register(Category)#
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

#@admin.register(Clothing)#
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description', 'user__username')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {'fields': ('name', 'user', 'category')}),
        ('Additional Information', {'fields': ('description', 'image')}),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
