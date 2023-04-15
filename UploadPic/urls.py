from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='Index'),
    path('delete_photo/<int:pk>/', views.delete_photo, name='delete_photo'),
]