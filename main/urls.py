from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login', views.loginpage, name='login'),
    path('fault/', views.centralfaultpage, name='fault'),
    path('logout', views.logoutpage, name='logout'),
    path('escom-central/', views.escomcentralpage, name='escom-central'),
    path('delete', views.deletepage, name='delete'),
    path('escom-north/', views.escomnorthpage, name='escom-north'),
    path('escom-south/', views.escomsouthpage, name='escom-south'),
    path('waterboard-central/', views.waterboardcentralpage, name='waterboard-central'),
    path('waterboard-north/', views.waterboardnorthpage, name='waterboard-north'),
    path('waterboard-south/', views.waterboardsouthpage, name='waterboard-south'),
    path('construction-central/', views.constructioncentralpage, name='construction-central'),
    path('construction-north/', views.constructionnorthpage, name='construction-north'),
    path('construction-south/', views.constructionsouthpage, name='construction-south'),


]