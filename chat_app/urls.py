from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('chat/<str:recipient_username>/', views.chat_view, name='chat'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]