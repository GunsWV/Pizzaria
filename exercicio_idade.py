#Voce foi contrato para criar um programa de verificação de idade para clientes que consumem bebida alcoolica

nome = input("input o seu nome:")
idade = int(input("Digite sua idade:"))

#if e SE em pt-br e else é SENÃO
if idade >= 18:
    print("Autorizado, maior de idade", idade)
else:
    print(f"Não autorizado, menor de idade: {idade} anos")
    
