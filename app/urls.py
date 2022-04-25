from django.urls import path
from app import views

urlpatterns = [
    path('list/', views.password_list, name='list'),
    path('detail/<int:pk>/', views.password_detail, name='detail'),
    path('create/', views.password_create, name='create'),
    path('edit/<int:pk>/', views.password_edit, name='edit'),
]
