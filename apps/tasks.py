from celery import shared_task
from django.core.mail import send_mail
from root import settings


@shared_task
def send_email(subject, message, receiver_email):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver_email])
    return {"status": "success", "email": receiver_email}
