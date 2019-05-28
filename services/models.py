# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.html import format_html

class TypeService(models.Model):
    """
        El tipo servicio es el que va a contener el nombre de el servicio que se va a vencer
        'solo por hacer lo más dinámico'
        en este se almacena una url alternativa por si el no entregan una url de vencimiento en el modelo de servicio
        se pondrá por defecto esta.

    """
    type_services_name = models.CharField("Nombre del tipo de servicio", max_length=60,blank=False, null=False,help_text="Nombre del Tipo de Servicio")
    type_services_url_default = models.URLField("Url del tipo de servicio",blank=False, null=False, help_text="Url donde Se Paga el servicio")
    type_Services_image = models.ImageField("Imagen tipo de servicio", upload_to="tiposervicios",blank=True, null=True,help_text="Imagen para representar el tipo de servicio (Se recomienda el fondo transparente)")

    class Meta:
        verbose_name = "Tipo Servicio"
        verbose_name_plural = "Tipos de Servicios"

    def __unicode__(self):
        return "%s" % (self.type_services_name)
    
    def image_service(self):
        """
            funcion encargada de retornar una imagen con el icono de el tipo de servicio
        """
        try:
            return format_html('<a href="#"><img style="width: 76%;" src="'+self.type_Services_image.url+'"></a>')
        except ValueError:
            return format_html('<a href="#"><img style="width: 76%;" src="/static/material/imgs/logo.png"></a>')
    

class Client(models.Model):
    """
        El usuario va a contener un nombre y un email el cual es donde se le enviará el correo.
    """
    client_name = models.CharField("Nombre cliente", max_length=50,blank=False, null=False,help_text="Nombre del Cliente")
    client_email = models.CharField("Email Cliente", max_length=60,blank=False, null=False,help_text="Email del Cliente")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __unicode__(self):
        return "%s" % (self.client_name)

class Platform(models.Model):
    """
        Datos de la plataforma la cual está asociada a los servicios.
    """
    platform_name = models.CharField("Nombre", max_length=100, blank=False, null=False,help_text="Nombre de la Plataforma")
    platform_url = models.URLField("Url plataforma", blank=True, null=True, help_text="Url del Plataforma")
    platform_client = models.ForeignKey(Client,verbose_name="Cliente de la plataforma", blank=False, null=False)

    def __unicode__(self):
        return "%s" % (self.platform_name)

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'

class Services(models.Model):
    """
        En este modelo se almacena la fecha de vencimiento del servicio y el tipo de servicio para poder relacionar
        usuario con servicio y poder mostrar a qué usuario se le vence cual servicio.
    """
    services_date = models.DateField("Fecha de vencimiento", auto_now=False, auto_now_add=False,blank=False, null=False,help_text="Fecha de Vencimiento Servicio")
    services_user = models.ForeignKey(Client, verbose_name="Cliente", blank=False, null=False, help_text="Usuario del Servicio")
    services_platform = models.ForeignKey(Platform, verbose_name="Plataforma", blank=False, null=False, help_text="Plataforma del servicio")
    services_type_service = models.ForeignKey(TypeService, verbose_name="Tipo de servicio", blank=False, null=False, help_text="Tipo de servicio")
    services_email_send = models.BooleanField(verbose_name="Email enviado", default=False)
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        
    def __unicode__(self):
        return "{0}".format(self.services_type_service.type_services_name)
    
    def get_default_url(self):
        if self.services_platform:
            url = self.services_platform
        else:
            url = self.services_type_service.type_services_url_default
        return url
    
    def image_service(self):
        """
            funcion encargada de retornar una imagen con el icono de el servicio
        """
        try:
            return format_html('<a href="#"><img style="width: 76%;" src="'+self.services_type_service.type_Services_image.url+'"></a>')
        except ValueError:
            return format_html('<a href="#"><img style="width: 76%;" src="/static/material/imgs/logo.png"></a>')
    
    def service_status_notificated(self):
        """
        Esta función es la encargada de mostrar en qué estado se encuentra un
        servicio.

        Tipos de estado:
           correo enviado : este es el estado donde ya se notificó a el usuario
           próximo a vencer : este es el estado en el cual se vence en 7 días
           vencido : este es el estado en el cual ya se venció el servicio

        """
        today = datetime.datetime.now()
        next_week = today + datetime.timedelta(days=7)
        html = ""
        i_material = "<i class='material-icons'>"
        i_material_close = "</i>"

        if self.services_email_send:
            html += "<p style='color:#7b9add;vertical-align: top;display: inherit;'>"+i_material+'email'+i_material_close+" Notificado</p><br>"

        if self.services_date == today.date():
            html += "<p style='color:#f14337;vertical-align: top;display: inherit;'>"+i_material+'cancel'+i_material_close+" Vencido</p>"

        elif self.services_date <= next_week.date():
            html += "<p style='color:#FF5722;vertical-align: top;display: inherit;'>"+i_material+'change_history'+i_material_close+"Una semana</p>"

        else:
            html += "<p style='color:#20be14;vertical-align: top;display: inherit;'>"+i_material+'check_box'+i_material_close+" Correcto</p>"
        
        return format_html(html)
