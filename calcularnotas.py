# Sistema de Notas dos Alunos

# Função para calcular a média
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# Função para verificar a aprovação
def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


# Função para gerar o relatório
def gerar_relatorio(relatorio):
    print("\n===== RELATÓRIO DE DESEMPENHO =====")

    for resultado in relatorio:
        print(resultado)

    print("===== FIM DO RELATÓRIO =====")


# Programa principal
relatorio = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):

    print("\nAluno", i + 1)

    nome = input("Nome do aluno: ")

    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    n3 = float(input("Terceira nota: "))

    media = calcular_media(n1, n2, n3)

    situacao = verificar_aprovacao(media)

    resultado = f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}"

    relatorio.append(resultado)
#Exibir o Relatório
gerar_relatorio(relatorio)