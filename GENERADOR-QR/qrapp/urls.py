from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # La página de inicio
    path('generar_qr/', views.generar_qr, name='generar_qr'),  # Generar el código QR
]
