# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User,Group

from services.models import (TypeService,Client,Services,Platform)

class TypeServiceAdmin(admin.ModelAdmin):
    """
        administrador de tipos de servicio
    """
    model = TypeService
    icon = '<i class="material-icons">line_weight</i>'
    search_fields = ('type_services_name','image_service',)
    list_display = ('type_services_name','image_service',)
    
    class Media:
        js=('js/admin_services.js', )

class ClientAdmin(admin.ModelAdmin):
    """
        administrador de clientes
    """
    model = Client
    icon = '<i class="material-icons">account_circle</i>'
    search_fields = ('client_name','client_email',)
    list_display = ('client_name','client_email',)


class ServicesAdmin(admin.ModelAdmin):
    """
        administrador de servicios
    """
    model = Services
    icon = '<i class="material-icons">build</i>'
    search_fields = (
        'services_platform',
        'services_user',
        'services_type_service', 
        'services_date',)

    list_display = (
        'service_status_notificated',
        'services_platform',
        'services_user',
        'services_type_service', 
        'services_date',
        'image_service')
    
    exclude = ('services_email_send',)

    class Media:
        js=('js/admin_services.js', )

class PlatformAdmin(admin.ModelAdmin):
    """
        administrador de las plataformas
    """
    model = Platform
    icon = '<i class="material-icons">lightbulb_outline</i>'
    search_fields = (
        'platform_name',
        'platform_client',
        'platform_url',)
    list_display = (
        'platform_name',
        'platform_client',
        'platform_url')

admin.site.register(TypeService,TypeServiceAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Services,ServicesAdmin)
admin.site.register(Platform,PlatformAdmin)

admin.site.unregister(Group)