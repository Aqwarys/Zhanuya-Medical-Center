from django.contrib import admin
from . import models


admin.site.register(models.Role)
admin.site.register(models.Department)
admin.site.register(models.User)


# Register your models here.
