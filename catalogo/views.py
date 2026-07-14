from django.shortcuts import render, get_object_or_404
from .models import Veiculo, Marca

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    marcas = Marca.objects.all()

    termo_pesquisa = request.GET.get('pesquisa')
    marca_selecionada = request.GET.get('marca')
    estado_selecionado = request.GET.get('estado')

    if termo_pesquisa:
        veiculos = veiculos.filter(modelo__icontains=termo_pesquisa) | veiculos.filter(versao__icontains=termo_pesquisa)

    if marca_selecionada:
        veiculos = veiculos.filter(marca_id=marca_selecionada)

    if estado_selecionado:
        veiculos = veiculos.filter(estado=estado_selecionado)

    contexto = {
        'veiculos': veiculos,
        'marcas': marcas,
    }
    return render(request, 'lista.html', contexto)


# Nova função para carregar um carro específico
def detalhe_veiculo(request, pk):
    # Busca o veículo pelo ID (pk). Se não existir, exibe um erro 404 de página não encontrada.
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, 'detalhe.html', {'veiculo': veiculo})
