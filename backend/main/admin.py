from django.contrib import admin
from .models import *

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass
