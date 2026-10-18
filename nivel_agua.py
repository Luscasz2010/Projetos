VERMELHO = '\033[91m'
AMARELO = '\033[93m'
VERDE = '\033[92m'
CIANO = '\033[96m'
AZUL = '\033[94m'
RESET = '\033[0m' 

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

cores = [
    VERMELHO,
    AMARELO,
    VERDE,
    CIANO,
    AZUL
]

def mostrar_nivel(nivel):
    if 1 <= nivel <= 5:
        mensagem = niveis[nivel - 1]
        cor = cores[nivel - 1]
        # Exibe colorido e depois reseta a cor
        print(f"{cor}Nível {nivel}: {mensagem}{RESET}")
    else:
        print("Nível inválido!")

# Simulação do sistema
for nivel in range(1, 6):
    mostrar_nivel(nivel)
