import mercadopago
from dotenv import load_dotenv
import os
load_dotenv()
sdk = mercadopago.SDK(os.getenv("TEST_ACESS_TOKEN"))

def pagar():
	payment_data = {
		"items":[
			{"id": "1234", #receber
			"title": "Dummy Title", #receber
			 "quantity": 1, #deixar 1 padrao
			 "currency_id": "BRL", #manter real
			 "unit_price": 10, #receber
			 },
			#para adicionar outro produto, adicionar outro dicionario desse a lista
		],
		"back_urls":{
			"success": "https://www.youtube.com/",
			"failure":"http://127.0.0.1:8000/",
			"pending":"http://127.0.0.1:8000/",
		},
		"auto_return": "all",
	}
	result = sdk.preference().create(payment_data)
	payment = result["response"]
	link_pagamento = payment["init_point"] #init_point ou sandbox_init_point
	print(payment)
	return link_pagamento
