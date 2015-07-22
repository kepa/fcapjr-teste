from django.contrib import admin
from django.db import models
from .models import (Banner, Area, Membro, Mission, Vision, Value, ValueDescription)

admin.site.register([Banner, Area, Membro, ValueDescription])

@admin.register(Mission, Vision, Value)
class Essence(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True
    def has_delete_permission(self, request):
        return False
