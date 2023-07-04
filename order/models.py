from django.db import models
from bookstore.models import Book
from accounts.models import CustomUser
import random

def order_no():
    """ Generate Random Order Number """
    
    gen_order_no = int(random.randint(100000, 199999))
    return gen_order_no

class Order(models.Model):
    """ Order Model """
    
    PENDING = 'PE'
    REJECTED = 'RE'
    COMPLETED = 'CO'
    
    STATUSES = (
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (COMPLETED, 'Completed'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    price = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_no = models.IntegerField(primary_key=True, unique=True, editable=False, default=order_no)
    status = models.CharField(max_length=2, choices=STATUSES, default=PENDING)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.order_no)

    def get_price(self):
        price = self.book.price
        quantity = self.quantity
        total_price = price * quantity
        self.cost = total_price
        self.save()
        return self.cost
    
    @property
    def customer(self):
        return f'{self.user.first_name} {self.user.last_name}'
