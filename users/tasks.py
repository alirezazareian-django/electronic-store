from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    subject = "خوش‌آمدید!"
    message = "به وبسایت ما خوش آمدید. از حضورتان خوشحالیم!"
    from_email = "your_email@gmail.com"  # ایمیل فرستنده
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return f"ایمیل خوش‌آمدگویی به {email} ارسال شد!"
