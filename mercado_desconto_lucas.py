valor = float(input("Bem vindo ao Supermercado Promotec, digite o valor total das suas compras para aplicarmos o desconto: "))
if valor < 200:
    desconto =0.05
elif valor >= 200 and valor < 300:
    desconto = 0.10
elif valor > 300:
    desconto = 0.15

valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print(f"Seu desconto será de {desconto * 100:.0f}%")
print(f"Com isso, o total a pagar será de {valor_final:.2f} reais")