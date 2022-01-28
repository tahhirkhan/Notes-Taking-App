from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('registerUser', views.register, name='registerUser'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),



    path('', views.home, name='home'),
    path('addItem', views.addItem, name='addItem'),
    path('deleteItem/<str:pk>/', views.deleteItem, name='deleteItem'),


]
