from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import Member


admin.site.register(Member)
admin.site.unregister(Group)
