# python standard library
import os
import time

# django
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

# local django
from core.models import Reserva
from .models import Quarto, ImagemQuarto
from pousada.settings import BASE_DIR


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


@login_required
def imagem(request):
    # usuários 'comuns' não podem acessar essa página
    if request.user.is_superuser == False:
        return redirect('home')

    # caminho para todas as imagens enviadas
    MEDIA = os.path.abspath(os.path.join(
        BASE_DIR, '../pousada/static/media/quarto_imagens/')
    )

    # irá conter todas as imagens contidas  no diretorio `MEDIA`
    arquivos = []

    # irá conter todas as informações necessárias para ser renderizado no navegador
    arquivos_template = []

    # r: raiz
    # d: diretorio
    # f: arquivo (file)
    for r, d, f in os.walk(MEDIA):
        for arquivo in f:
            # adiciona todos os arquivos na lista
            arquivos.append(os.path.join(r, arquivo))

        # percorre a lista de caminhos
        for caminho in arquivos:
            # corta a string para vizualizar a imagem na tag `img` do HTML
            # slice(inicio, parada)
            url = slice(81, len(caminho))

            # corta a string para retorna somente o nome do arquivo (com sua extensão)
            # slice(inicio, parada)
            nome = slice(110, len(caminho))

            # coloca dentro de uma lista todas as informações para renderizar no navegador
            arquivos_template.append({
                'path': caminho,  # caminho completo
                'url': caminho[url],  # caminho para renderizar a imagem
                'nome': caminho[nome]  # nome do arquivo
            })

        # verifica se o admin clicou no checkbox `apagar`
        if request.POST.get('option') == 'apagar':
            # remove o arquivo do diretorio
            os.remove(request.POST.get('path'))

        # verifica se o admin clicou no checkbox `renomear_check`
        if request.POST.get('option') == 'renomear':
            # captura o caminho completo do arquivo
            path = request.POST.get('path')

            # corta a string para retonar o caminho em que o arquivo está contido
            # (não retorna o nome do arquivo)
            # slice(inicio)
            path_wo_file = slice(109)

            # captura o nome enviado pelo admin através do `input:text`
            novo_nome = request.POST.get('renomear')

            # renomeia o arquivo
            # os.rename(arquivo_com_nome_antigo, arquivo_com_novo_nome)
            os.rename(path, path[path_wo_file] + '/' + novo_nome)

    return render(request, 'imagem.html', {'imagem': arquivos_template})
