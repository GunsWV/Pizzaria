#Voce estáem um processo seletivo para ser dev.jr, e recebeu o teste para desenovolver. Será um programa para pizzaria, no qual receberá: Nome do cliente, endereço,opções (mussarela, calabresa, portuguesa, marguerita), deverá imrprimiro nome do cliente, endereço e sabor escolhido

#Passo.1 nome do cliente
nome_do_cliente = input("Seja bem vindo! Qual seu nome por favor ? ")

#Passo.2 endereço
endereco = input("Endereço de entrega: ")

#Passo.3 Receber o Pedido
pedido = input("Digite qual o sabor para sua pizza: \n""(mussarela | calabresa | portuguesa | marguerita) : ")

print(f"Sr. {nome_do_cliente}, seu pedido será entregue no {endereco}, o sabor escolhido é {pedido}")

#Passo.4 opções (elif tradução para pt-br senão então)
if pedido == "Mussarela":
    print(f"Sr(a){nome_do_cliente}, o seu pedido será entregue no {endereco}, sabor escolhido é: {pedido}")
elif pedido == "calabresa":
    print(f"Muito obrigado pelo seu pedido, {nome_do_cliente}. Nosso motoboy já está a caminho do {endereco}, com sua pizza de {pedido}")
elif pedido == "portuguesa":
    print(f"Excelente escolha {nome_do_cliente}, a nossa pizza {pedido} chegará em breve no {endereco}")
else: print(f"Oba! A pizza {pedido}, chegará quentinha na sua casa {endereco}, agradecemos pelo pedido {nome_do_cliente}")
