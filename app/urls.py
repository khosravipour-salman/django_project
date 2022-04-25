from django.urls import path
from app import views

urlpatterns = [
    path('list/', views.password_list, name='list'),
    path('detail/<int:pk>/', views.password_detail, name='detail'),
]
