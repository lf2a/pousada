# django
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

# local django
from cliente.models import User
from quarto.models import Quarto
from .models import Reserva

# python standard library
from datetime import datetime


def obter_valor_total(inicio, termino, diaria):

    # recebe a data no formato do tipo string e retorna um objeto datetime
    t = datetime.strptime(termino, '%Y-%m-%d')
    i = datetime.strptime(inicio, '%Y-%m-%d')

    # calcula a quanditade de dias de `s -> inicio da reserva` até `f -> o termino da reserva`
    quantidade_dias = (t - i).days + 1

    # verifica se a quantidade de dias é igual a 0 ou 1
    if quantidade_dias == 0 or quantidade_dias == 1:
        return diaria

    # se o dia for menor que zero retorna um erro
    # pode ser causado se o usuário inserir a data de termino antes da data de inicio
    elif quantidade_dias < 0:
        return 'error'
    else:
        # calcula a diaria vezes a quantidade de dias
        return float(diaria) * int(quantidade_dias)


def criar_reserva(request, id_quarto):
    # captura o id do usuário logado
    id_usuario = request.user.id

    # busca as informações do usuário logado
    usuario = User.objects.get(id=id_usuario)

    # busca as informações do quarto escolhido
    quarto = Quarto.objects.get(id=id_quarto)

    # captura a data de inicio
    inicio = request.POST.get('inicio')

    # captura a data de termino
    termino = request.POST.get('termino')

    # captura a diaria do quarto escolhido
    diaria = quarto.diaria

    # calcular o valor total `quantidade de dias * diaria`
    total = obter_valor_total(inicio, termino, diaria)

    # verifica se a data é válida
    if total == 'error':
        return HttpResponse('erro')

    # criando o objeto reserva com todos os atributos preenchidos
    reserva = Reserva(
        cliente=usuario,
        quarto=quarto,
        inicio=inicio,
        termino=termino,
        total=total
    )

    # sava objeto no banco de dados
    reserva.save()


@login_required
def reservar_quarto(request, id_quarto):

    # só aceita método do tipo post
    if request.method == 'POST':
        criar_reserva(request, id_quarto)
        # redirecionar para as reservas do usuario
        return redirect('reservas')

    else:
        return HttpResponse('método não permitido')


@login_required
def excluir_reserva(request, id_quarto):
    # buscando a reserva para apagar
    reserva = Reserva.objects.get(quarto__id=id_quarto)

    id_user = request.user.id
    id_user_reserva = reserva.cliente.id

    if id_user == id_user_reserva:
        # apagando reserva
        reserva.delete()

    # redirecionando para a pagina de reservas do usuario
    return redirect('reservas')
