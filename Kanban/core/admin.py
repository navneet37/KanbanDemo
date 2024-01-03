from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Role, Technology, DeveloperProfile, Board, List, Card, Comment

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Technology)
admin.site.register(DeveloperProfile)
admin.site.register(Board)
admin.site.register(List)
admin.site.register(Card)
admin.site.register(Comment)
