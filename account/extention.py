from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(to_email, otp):
    subject = 'accept email'
    message = f'please accept your email: {otp}'
    from_email = settings.EMAIL_HOST_USER  # ایمیل فرستنده

    send_mail(
        subject,
        message,
        from_email,
        [to_email],  # لیست دریافت‌کنندگان
        fail_silently=False,
    )