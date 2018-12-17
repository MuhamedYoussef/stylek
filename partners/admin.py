from django.contrib import admin
from .models import Partner

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'city')

admin.site.register(Partner, PartnerAdmin)
