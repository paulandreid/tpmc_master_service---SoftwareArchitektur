from django.contrib import admin

# Register your models here.
from master_service.models import User, Routine

admin.site.register(User)
admin.site.register(Routine)
