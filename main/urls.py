from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login', views.loginpage, name='login'),
    path('fault-central/', views.centralfaultpage, name='fault-central'),
    path('fault-north/', views.northfaultpage, name='fault-north'),
    path('fault-south/', views.southfaultpage, name='fault-south'),
    path('logout', views.logoutpage, name='logout'),
    path('escom-central/', views.escomcentralpage, name='escom-central'),
    path('delete-escom-central/<str:pk>/', views.deletecentralescompage, name='delete-escom-central'),
    path('delete-escom-north/<str:pk>/', views.deletenorthescompage, name='delete-escom-north'),
    path('delete-escom-south/<str:pk>/', views.deletesouthescompage, name='delete-escom-south'),
    path('delete-construction-central/<str:pk>/', views.deletecentralconstructionpage, name='del-construction-central'),
    path('delete-construction-north/<str:pk>/', views.deletenorthconstructionpage, name='del-construction-north'),
    path('delete-construction-south/<str:pk>/', views.deletesouthconstructionpage, name='del-construction-south'),
    path('delete-waterboard-central/<str:pk>/', views.deletecentralwaterboardpage, name='delete-waterboard-central'),
    path('delete-waterboard-north/<str:pk>/', views.deletenorthwaterboardpage, name='delete-waterboard-north'),
    path('delete-waterboard-south/<str:pk>/', views.deletesouthwaterboardpage, name='delete-waterboard-south'),
    path('escom-north/', views.escomnorthpage, name='escom-north'),
    path('escom-south/', views.escomsouthpage, name='escom-south'),
    path('waterboard-central/', views.waterboardcentralpage, name='waterboard-central'),
    path('waterboard-north/', views.waterboardnorthpage, name='waterboard-north'),
    path('waterboard-south/', views.waterboardsouthpage, name='waterboard-south'),
    path('construction-central/', views.constructioncentralpage, name='construction-central'),
    path('construction-north/', views.constructionnorthpage, name='construction-north'),
    path('construction-south/', views.constructionsouthpage, name='construction-south'),


]