# django
from django.shortcuts import render, HttpResponse

# local django
from core.models import Reserva
from .models import Quarto, ImagemQuarto


def buscar_quartos_disponiveis():
    '''Buscando quartos disponiveis

    return:
        list: retorna os quartos que não estão reservados
    '''

    # buscando todos os quartos do banco
    quartos = Quarto.objects.all()

    # buscando todas as reservas do banco
    reservas = Reserva.objects.all()

    quartos_list = []
    reservas_list = []

    # adiciona todos os quartos em uma lista
    for q in quartos:
        quartos_list.append(q)

    # adiciona todos os quartos que estao reservados e os coloca em uma lista
    for r in reservas:
        reservas_list.append(r.quarto)

    # faz a diferenca dos conjuntos e retorna os quartos que não estão em `reservas_list`
    quartos_disponiveis = set(quartos_list).difference(reservas_list)

    # lista que irá ser retornada
    data = []

    # busca todas as imagens do cada quarto disponivel
    for q in quartos_disponiveis:
        foto = ImagemQuarto.objects.filter(quarto__id=q.id)

        # adiciona em uma lista uma dict contendo o quarto e suas imagens
        data.append({
            'quarto': q,
            'foto': foto
        })

    # limpando
    del quartos, quartos_list, reservas, reservas_list, quartos_disponiveis

    return data


def home(request):
    # só aceita método do tipo `GET`
    if request.method == 'GET':

        # buscar quartos disponiveis
        data = buscar_quartos_disponiveis()

        # `request.user` -> verificação de autenticação
        return render(request, 'home.html', {
            'data': data,
            'user': request.user
        })
    else:
        return HttpResponse('método não permitido')
