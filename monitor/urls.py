
from django.urls import path
from monitor import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('toggle/', views.toggle_irrigation, name='toggle'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
