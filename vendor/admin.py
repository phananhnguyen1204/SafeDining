from django.contrib import admin

from vendor.models import Vendor, OpeningHour

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
  list_display = ('user', 'vendor_name', 'is_approved', 'created_at')
  list_display_link = ('user','vendor_name')
  
class OpeningHourAdmin(admin.ModelAdmin):
  list_display: ('vendor', 'day', 'from_hour', 'to_hour')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(OpeningHour)
