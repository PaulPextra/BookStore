from django.urls import path
from order import views

urlpatterns = [
    path('orders/', views.order),
    path('orders/<int:order_no>/', views.modify_order),
]
