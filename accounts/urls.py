from django.urls import path
from . import views

urlpatterns = [
    path('users/signup/', views.user_signup),
    path('users/login/', views.user_login),
    path('users/reset_passowrd/', views.reset_password),
    path('superadmin/users/',views.get_all_users),
    path('users/profile/', views.user_profile),
    path('superadmin/users/<uuid:user_id>/', views.get_user_by_id),
]