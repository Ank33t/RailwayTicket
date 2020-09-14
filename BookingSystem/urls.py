from django.urls import path
from BookingSystem import views

urlpatterns = [
    path('', views.home, name='railway-home'),
    path('about/', views.about, name='railway-about'),
    path('news/', views.news, name='railway-news'),
    path('contact/', views.contact, name='railway-contacts'),
    path('register/', views.registration, name= 'railway-registration')
]