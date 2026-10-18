excelente = 0
ruim = 0

print("Bem vindo a parte de Avaliação de atendimento da TudoWeb!")

for i in range(10):
    nome = input("Digite o seu nome: ")
    idade = int(input("Agora, digite a sua idade: "))
    opiniao = int(input("Digite sua opinião pelo atendimento (1- excelente, 2- bom e 3- ruim): "))
    
    if opiniao == 1:
        excelente += 1
    if opiniao == 3:
        ruim += 1

print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)