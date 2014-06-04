from django.contrib import admin

# Register your models here.

from grid.models import Grid_Square, Command

admin.site.register(Grid_Square)
admin.site.register(Command)