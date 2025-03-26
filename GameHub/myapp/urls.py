from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login",views.login_manager,name="login"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("logout", views.logout, name="logout"),
    path("register",views.register,name="register")
]
