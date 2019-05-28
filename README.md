Custom_reminder
===============
## Proyecto encargado de enviar correos a los clientes una semana antes de que se venza el servicio
___________

## Estructura:

* Tecnica:

   Python 2.7

   Django 1.11.5

   administrador django-material 1.0.0


* Cron:

    Para el envío de correos es necesario un cron que se ejecute todos los días
   ejemplo:
  

       * 1 * * * /usr/bin/python full-path/customer_reminder/manage.py enviocorreos

  
* Estados:

   1. Notificado     :  Este es cuado a el cliente ya se el envio el correo este se puede combinar con los demás

   2. Vencido        :  Este es cuando es servicio ya se paso de la fecha de vencimiento

   3. Alerta         :  Este es cuado el faltan 7 días para que se venza



>NOTA: "
   el comando para enviar el correo es
       "muestra el listado de las personas que se les va a enviar el correo"

       python manage.py enviocorreos"


## Colaboradores:
+ Wilson Andres Salgado Quiceno

# NotifY
