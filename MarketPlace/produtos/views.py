import os
import requests
from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()
def categorias(request,categoria):
    url = 'http://127.0.0.1:5000/ProdutoCategoria/'+str(categoria)
    token = os.getenv('TOKEN')
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url,headers=headers).json()
    return render(request,'produtos/categorias.html',{'context':response})

