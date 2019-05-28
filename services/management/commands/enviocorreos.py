# -*- encoding: utf-8 -*-
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.template import Context, RequestContext, loader
from django.template.loader import render_to_string

from services.models import Services

#   CRONETAB 
# 0 0 * * * theevil  ~/.virtualenvs/custom_reminder/bin/python ~/Proyects/customer-reminder/customer_reminder/manage.py enviocorreos

def send_email_to(ctx,email):
    """
        Función encargada de enviar correos con un contexto específico
    """
    
    body = render_to_string('email/service.html',ctx)
    message = EmailMessage('Notificacion Notify', body, settings.EMAIL_USER, [email])
    message.content_subtype = 'html'
    message.send()

class Command(BaseCommand):
    def handle(self, *args, **kargs):
        """
            Comando para filtrar los servicios que estan proximos a vencer para enviar el correo 
        """
        today = datetime.datetime.now()
        next_week = today + datetime.timedelta(days=7)

        services = Services.objects.filter(
            services_date__lte=next_week,
            services_email_send=False
        )

        print ("cantidad de services a vencer : "+str(services.count()))
        
        if services.count() > 0:
            for service in services:
                
                print ("enviando correo a el user : "+str(service.services_user))
                
                ctx = {
                    'title':service.services_type_service.type_services_name,
                    'date': service.services_date,
                    'name':service.services_user,
                    'service':service,
                    'platform':service.services_platform,
                }
                send_email_to(ctx,service.services_user.client_email)

                if User.objects.all().last().email:
                    ctx = {
                        'title':service.services_type_service.type_services_name,
                        'date': service.services_date,
                        'name':User.objects.all().last().username,
                        'service':service,
                        'platform':service.services_platform,
                    }
                    send_email_to(ctx,User.objects.all().last().email)
                
                service.services_email_send = True
                service.save()