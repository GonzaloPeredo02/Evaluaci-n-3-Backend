
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def index(request):
    return render(request,"index.html")

class SignUpView(CreateView):
    form_class= UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "¡Usuario creado exitosamente!"

def gestor_usuarios(request):
    return render(request, 'gestorUser/gestorUsuarios.html')

