from django.contrib import admin
from .models import Attendant


class AttendantAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone_number"]


admin.site.register(Attendant, AttendantAdmin)
