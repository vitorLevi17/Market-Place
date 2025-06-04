import mercadopago
from dotenv import load_dotenv
import os
load_dotenv()
sdk = mercadopago.SDK(os.getenv("TEST_ACESS_TOKEN"))

def pagar(id,titulo,preco):
	payment_data = {
		"items":[
			{"id": id,
			"title": titulo,
			 "quantity": 1, #deixar 1 padrao
			 "currency_id": "BRL", #manter real
			 "unit_price": float(preco),
			 },
			#para adicionar outro produto, adicionar outro dicionario desse a lista
		],
		"back_urls":{
			"success":"https://40fb-191-22-68-79.ngrok-free.app/fim_compra/",
			"failure":"https://40fb-191-22-68-79.ngrok-free.app",
			"pending":"https://40fb-191-22-68-79.ngrok-free.app",
		},
		"auto_return": "all",
	}
	result = sdk.preference().create(payment_data)
	print("Resposta da API Mercado Pago:", result)
	payment = result["response"]
	link_pagamento = payment["init_point"] #init_point ou sandbox_init_point
	print(payment)
	return link_pagamento

def forma_Pagamento(tipo):
	if tipo == 'account_money': #Dinheiro	na	conta	do	Mercado	Pago.
		return 4
	elif tipo == 'bank_transfer': #Pix	e	PSE(Pagos	Seguros	en	Línea).
		return 3
	elif tipo == 'credit_card': #Pagamento	com	cartão	de	crédito.
		return 2
	elif tipo == 'debit_card': #Pagamento	com	cartão	de	débito.
		return 1
	else:
		return 1000
	# prepaid_card #Pagamento	com	cartão	pré - pago.
	# digital_currency #Purchases	with Linha de Crédito.	voucher_card: Alelo	benefícios	e	Sodexo.
