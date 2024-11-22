# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_normal_user', 'location')
    search_fields = ('user__username', 'location')
    list_filter = ('is_normal_user',)  # Add filter by is_normal_user in admin
    ordering = ('user',)  # Order by user field

admin.site.register(Profile, ProfileAdmin)
