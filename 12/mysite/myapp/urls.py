from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('software/<int:software_id>/', views.software_detail, name='software_detail'),  # Детальный просмотр
    path('software/<int:software_id>/edit/', views.software_edit, name='software_edit'),  # Редактирование
]
