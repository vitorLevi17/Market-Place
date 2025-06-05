from decimal import Decimal
from django.shortcuts import render,redirect
from dotenv import load_dotenv
from sistema.models import Favoritos,FormaPag,Compra
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CompraForm
from sistema.validators import valida_cep
from sistema.requestsAux import requisitarFretes,requisitarProduto,requisitarProdutoCategoria,requisitarFreteId,requisitarFreteTempo
from .compra import pagar,forma_Pagamento
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
#@login_required(login_url='/entrar/')
#Adicionar complemento
def compra(request,produto):
    response = requisitarProduto(produto)
    preco = Decimal(str(response['preco']))
    quantidade = 1
    lista_Fretes = []
    total = preco
    form = CompraForm(request.POST)
    cep = form['cep'].value()
    complemento = form['complemento'].value()
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
        id = response['id']
        nome = response['Nome']
        request.session['produto_id'] = response['id']
        request.session['total'] = float(total)
        request.session['quantidade'] = int(quantidade)
        request.session['frete_id'] = frete_id
        request.session['cep'] = cep
        request.session['complemento'] = complemento
        link = pagar(id,nome,total)
        return redirect(link)

    return render(request,"produtos/compra.html",{'context': response,
                                                  'form': form ,
                                                  'fretes': lista_Fretes,
                                                  'total':total})
def pos_pagamento(request):
    usuario=request.user
    cep = request.session.get('cep')
    complemento = request.session.get('complemento')
    tipo_pagamento = request.GET.get('payment_type')
    id_forma_pag = forma_Pagamento(tipo_pagamento)
    forma_pag = FormaPag.objects.get(id=id_forma_pag)
    produto = request.session.get('produto_id')
    quantidade = request.session.get("quantidade")
    frete_id = request.session.get('frete_id')
    endereco = f'{cep} - {complemento}'
    tempo_previsto = requisitarFreteTempo(cep,frete_id)
    valor_compra = request.session.get('total')
    compra = Compra.objects.create(
         usuario=usuario,
         forma_pag=forma_pag,
         produto=produto,
         quantidade=quantidade,
         frete_id=frete_id,
         endereco=endereco,
         tempo_previsto=tempo_previsto,
         valor_compra=valor_compra,
    )
    compra.save()
    return render(request,'produtos/pos_pagamento.html')