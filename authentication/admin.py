from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'is_active', 'is_staff')
    search_fields = ('email', 'name', 'surname',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        'name', 'surname', 'patronymic', 'email', 'phone', 'address', 'birthday', 'job', 'is_active', 'is_staff')


admin.register(User, UserAdmin)
