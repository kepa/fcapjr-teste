from django.contrib import admin
from django.db import models
from .models import *

admin.site.register([Banner, Area, Membro, ValueDescription])

@admin.register(Mission, Vision, Value, Description)
class Essence(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True
