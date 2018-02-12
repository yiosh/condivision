from django.contrib import admin
from . import models
# Register your models here.



admin.site.register(models.CcAccount)
admin.site.register(models.CcAnagrafica)
admin.site.register(models.AuthGroup)
admin.site.register(models.AuthGroupPermissions)
admin.site.register(models.AuthPermission)
admin.site.register(models.AuthUser)
