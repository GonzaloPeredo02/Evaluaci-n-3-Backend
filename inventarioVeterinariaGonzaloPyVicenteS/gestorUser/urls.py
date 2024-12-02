from django.urls import path
from . import views
from gestorUser.views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('', views.gestor_usuarios, name='gestor_usuarios'),
    ]