from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import Member


admin.site.unregister(Group)


@admin.register(Member)
class CustomMemberAdmin(UserAdmin):
    model = Member
    
    # part2
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)
            }),
    )
