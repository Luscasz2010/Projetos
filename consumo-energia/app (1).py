n = input("Digite o nome do produto:")
p = float(input("Digite a potência em watts do aparelho: "))
t = float(input("Agora, digite o tempo médio de uso diário em horas: "))
cm = (p * t * 30) / 1000
print(f"Aparelho: {n}, consumo estimado: {cm} kWh/mês.")