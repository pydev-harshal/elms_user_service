from django.contrib import admin
from django.contrib.auth import get_user_model
from users_app.models import Profile


User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user__id', 'user__first_name', 'user__last_name', 'user__email', 'profile_photo')
admin.site.register(Profile, ProfileAdmin)
