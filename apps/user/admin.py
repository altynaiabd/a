from django.contrib import admin
from .models import UserModel

# Register your models here.

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name',)
    list_filter = ('is_staff',)

    
