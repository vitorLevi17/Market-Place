from decimal import Decimal
from django.shortcuts import render
from dotenv import load_dotenv
from sistema.models import Favoritos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Compra
from sistema.validators import valida_cep
from sistema.requestsAux import requisitarFretes,requisitarProduto,requisitarProdutoCategoria,requisitarFreteId
load_dotenv()
def produto(request,produto):
    response = requisitarProduto(produto)
    return render(request,'produtos/produto.html',{'context':response})
def categorias(request,categoria):
    response = requisitarProdutoCategoria(categoria)
    return render(request,'produtos/categorias.html',{'context':response})
@login_required(login_url='/entrar/')
def favoritos(request,produto):
    response = requisitarProduto(produto)
    usuario = request.user
    produto = produto

    if not Favoritos.objects.filter(usuario=usuario,produto=produto).exists():
        favoritos = Favoritos.objects.create(usuario = usuario,produto = produto)
        favoritos.save()
        messages.success(request,"Item favoritado com sucesso")
    else:
        messages.error(request,"Produto já salvo")
    return render(request,"produtos/produto.html",{'context':response})
@login_required(login_url='/entrar/')
def lista_favoritos(request):
    usuario = request.user
    favoritos = Favoritos.objects.filter(usuario=usuario)
    lista_favoritos = []
    for favorito in favoritos:
        response = requisitarProduto(favorito.produto)
        lista_favoritos.append(response)

    return render(request, 'produtos/lista_favoritos.html', {'context': lista_favoritos})
@login_required(login_url='/entrar/')
def desfavoritar(request,produto):
    response = requisitarProduto(produto)
    usuario = request.user
    try:
        favoritos = Favoritos.objects.get(usuario=usuario, produto=produto)
        favoritos.delete()
        messages.success(request,"Item excluido com sucesso")
    except Favoritos.DoesNotExist:
        messages.error(request,"Você não adicionou o item aos favoritos")
    return render(request,"produtos/produto.html",{'context':response})

def compra(request,produto):
    response = requisitarProduto(produto)
    preco = Decimal(str(response['preco']))
    lista_Fretes = []
    total = preco
    form = Compra(request.POST)
    cep = form['cep'].value()
    if not form.is_valid():
        messages.error(request,'A quantidade deve ser maior ou igual a 1')
    elif valida_cep(cep) != True:
        messages.error(request, 'CEP inválido')
    else:
        quantidade = Decimal(form.cleaned_data["quantidade"])
        fretes = requisitarFretes(cep)
        for frete in fretes:
            if "error" not in frete:
                lista_Fretes.append(frete)
                total = preco * quantidade

    frete_id = request.POST.get('frete_id')
    if frete_id:
        frete = requisitarFreteId(cep,frete_id)
        total += frete
    return render(request,"produtos/compra.html",{'context': response,
                                                  'form': form ,
                                                  'fretes': lista_Fretes,
                                                  'total':total})
# def preco_produto(request,preco_min,preco_max):
#     url = 'http://localhost:5000/Produto/'+str(preco_min)+'/'+str(preco_max)+'/'
#     token = os.getenv('TOKEN')
#     headers = {
#         'Authorization': f'Token {token}',
#         'Content-Type': 'application/json'
#
#     response = requests.get(url, headers=headers).json()
#     return render(request, 'sistema/index.html', {'context': response})