from django.urls import path
from BookingSystem import views
from .views import TrainListVIew, TrainDetailVIew, TrainCreateVIew, TrainUpdateVIew, TrainDeleteVIew

urlpatterns = [
    path('', TrainListVIew.as_view(), name='railway-home'),
    path('train/<int:pk>/', TrainDetailVIew.as_view(), name='train-detail'),
    path('train/new/', TrainCreateVIew.as_view(), name='train-create'),
    path('train/<int:pk>/update', TrainUpdateVIew.as_view(), name='train-update'),
    path('train/<int:pk>/delete', TrainDeleteVIew.as_view(), name='train-delete'),
    path('about/', views.about, name='railway-about'),
    path('contact/', views.contact, name='railway-contacts'),
]

