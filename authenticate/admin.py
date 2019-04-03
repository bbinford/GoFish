from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email',  'is_guide',
                    ]
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name',
                           'last_name', 'is_staff', 'is_guide',
                           'is_active', 'is_superuser', 'last_login',
                           'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'is_guide', 'password1', 'password2')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
