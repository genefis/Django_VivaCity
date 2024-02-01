from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from VivaCityApp.views import login_register, dashboard, agenda, hospedaje, bardisco, gastronomia, shopping
# se importa las vistas de la aplicación
from django.contrib.auth.views import logout_then_login
from VivaCityApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_register/', login_register, name='login_register'),
    path('admin/', admin.site.urls),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/',views.index,name='index'),

    path('dashboard/',login_required(views.dashboard), name='dashboard'),
    path('agenda/',login_required(views.agenda), name='agenda'),
    path('rutas/',login_required(views.rutas), name='rutas'),
    path('hospedajes/',login_required(views.hospedajes), name='hospedajes'),
    path('bardisco/',login_required(views.bardisco), name='bardisco'),
    path('gastronomia/',login_required(views.gastronomia), name='gastronomia'),
    path('shopping/',login_required(views.shopping), name='shopping'),
    path('lugares/',login_required(views.lugares), name='lugares'),

    path('buscar_eventos/', views.buscar_eventos, name='buscar_eventos'),
    path('buscar_hospedajes/', views.buscar_hospedajes, name='buscar_hospedajes'),
    path('buscar_lugares/', views.buscar_lugares, name='buscar_lugares'),
    path('lista_canton/', views.lista_canton, name='lista_canton'),
    path('reservar_evento/', views.reservar_evento, name='reservar_evento'),
    path('logout/',logout_then_login,name='logout'),

]
