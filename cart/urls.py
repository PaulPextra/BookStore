from django.urls import path
from cart import views

urlpatterns = [
    path('carts/', views.cart),
    path('carts/<str:cart_id>/', views.fetch_cartitem_by_id),
]