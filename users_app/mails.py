from django.core.mail import EmailMessage


def send_welcome_email(user):    
    subject = f'Welcome to ELMS {user.first_name}'
    body = f'Hello {user.first_name} {user.last_name[0]}, welcome to ELMS PORTAL.\n\nRegards.\nELMS Portal.'
    email = EmailMessage(subject, body, to=[user.email])
    email.send()