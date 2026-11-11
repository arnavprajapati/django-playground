from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/<int:item_id>/', views.menu_detail, name='menu_detail'),
]