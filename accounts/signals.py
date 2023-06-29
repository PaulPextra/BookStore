from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()

@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created,**kwargs):
        '''Email Notification For Registered User'''
        
        if created:
                message = f""""Hello, {instance.username}.
                Thank you for signing up on our platform. We are very glad!


                Regards,
                The BookStore Team.
                """
                
                send_mail(subject="Your Account Has Been Created",
                        message=message,
                        recipient_list=[instance.email],
                        from_email="p3xtra@gmail.com",
                )