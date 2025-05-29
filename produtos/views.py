from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Cliente, Venda
from .forms import ProdutoForm, ClienteForm, VendaForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request,'produtos/list.html',{'produtos': produtos})

def cria_produto(request):
    if request.method =='POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})

def edita_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})

def remove_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request,'produtos/confirm_delete.html',{'produto':produto})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'produtos/cliente_list.html', {'clientes': clientes})

def cria_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'produtos/form.html', {'form': form})

def edita_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'produtos/form.html', {'form': form})

def remove_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'produtos/confirm_delete.html', {'obj': cliente})

def lista_vendas(request):
    vendas = Venda.objects.select_related('cliente', 'produto').all()
    cliente_id = request.GET.get('cliente')
    data_ini = request.GET.get('data_ini')
    data_fim = request.GET.get('data_fim')

    if cliente_id:
        vendas = vendas.filter(cliente_id=cliente_id)
    if data_ini and data_fim:
        vendas = vendas.filter(data_venda__range=[data_ini, data_fim])

    clientes = Cliente.objects.all()
    return render(request, 'produtos/venda_list.html', {
        'vendas': vendas,
        'clientes': clientes
    })

def cria_venda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_vendas')
    return render(request, 'produtos/form.html', {'form': form})

def edita_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    form = VendaForm(request.POST or None, instance=venda)
    if form.is_valid():
        form.save()
        return redirect('lista_vendas')
    return render(request, 'produtos/form.html', {'form': form})

def remove_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('lista_vendas')
    return render(request, 'produtos/confirm_delete.html', {'obj': venda})