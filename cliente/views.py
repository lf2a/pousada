# django
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

# local django
from core.models import Reserva
from quarto.models import ImagemQuarto
from cliente.models import User
from .forms import UserForm


@login_required
def buscar_minhas_reservas(request):
    # capturar o id do usuario logado
    id_usuario = request.user.id

    # filtrnado todas as reservas pelo id do usuario
    minhas_reservas = Reserva.objects.filter(cliente__id=id_usuario)

    # retorno das informacoes
    data = []

    # iterando as reservas
    for r in minhas_reservas:
        # buscando as fotos de cada quarto reservado
        foto = ImagemQuarto.objects.filter(quarto__id=r.quarto.id)

        # adicionando ao array as informações de cada reserva
        data.append({
            'quarto': r.quarto,
            'foto': foto,
            'reserva': r
        })

    return render(request, 'reservas.html', {'data': data})


@login_required
def atualizar_informacoes(request):

    id_usuario = request.user.id

    # buscando usuario
    usuario = User.objects.get(id=id_usuario)

    # formulario do usuario
    usuario_form = UserForm(request.POST or None, instance=usuario)

    if usuario_form.is_valid():
        usuario_form.save()
        return redirect('reservas')

    return render(request, 'atualizar.html', {'form': usuario_form})


@login_required
def excluir(request):
    id_usuario = request.user.id

    usuario = User.objects.get(id=id_usuario)

    usuario.delete()
    return redirect('home')
