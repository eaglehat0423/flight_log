from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_list, name='log_list'),
    path('add/', views.add_log, name='add_log'),
    path('<int:pk>/edit/', views.edit_log, name='edit_log'),
    path('delete/', views.delete_logs, name='delete_logs'),
    path('<int:pk>/', views.flight_log_detail, name='flight_log_detail'),
]

