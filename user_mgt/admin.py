from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from user_mgt.models import TodoUserProfile


# Register your models here.
class TodoUserProfileInline(admin.StackedInline):
    model = TodoUserProfile


class TodoUserAdmin(UserAdmin):
    inlines = (TodoUserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, TodoUserAdmin)
