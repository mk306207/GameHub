from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login_view",views.login_manager,name="login_view"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("logout_handler", views.logout_handler, name="logout_handler"),
    path("register",views.register,name="register")
]
