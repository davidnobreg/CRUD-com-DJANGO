from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.insert, name='cliente-create'),
    path('update/<int:id>/', views.update, name='cliente-update'), 
    path('delete/<int:id>/', views.delete, name='cliente-delete'), 
]