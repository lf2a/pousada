# django
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic

# local django
from cliente.forms import UserRegisterForm


def deslogar(request):
    logout(request)
    return redirect('home')


def error_404_view(req, exception):
    data = {
        "msg": "404 Não Encontrado"
    }

    return render(req, '404.html', {'data': data})


class SignUp(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
