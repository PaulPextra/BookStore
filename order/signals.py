from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from order.models import Order

User = get_user_model()

@receiver(post_save, sender=User)
def order_mail(sender, instance, created,**kwargs):
        """ Email Notification For Book Ordered """
        
        if created:
                message = f""""Hello, {instance.username}.
                Your Order has been placed successfully. Thank you for your patronage!
                
                Regards,
                BookStore Team.
                """
                send_mail(subject=f"Order {Order.order_no}",
                  message=message,
                  recipient_list=[instance.email],
                  from_email="p3xtra@gmail.com")

                