# O jogo

tabuleiro = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

### Colocando colunas e números:
linhas_e_colunas = {
    'A': 0,  
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
}

### Função de pergunta.
def pergunta_posicao_tabuleiro():
    coluna = input("Coluna (A-H): ")
    while coluna not in "ABCDEFGH":
        print("A coluna está errada! Deve ser entre A a H.")
        coluna = input("Coluna (A-H): ")
    
    linha = input("Linha (1-8): ")
    while linha not in "12345678":
        print("A linha está errada! Deve ser entre 1 a 8.")
        linha = input("Linha (1-8): ")


    return int(linha) -1, linhas_e_colunas[coluna]


### Adicionando as letras e números para facilitar a localização.
def print_tabuleiro(tabuleiro):
    print('\n')
    print("  A B C D E F G H")
    print(" +-+-+-+-+-+-+-+-+")
    linha_numero = 1
    for linhas in tabuleiro:
        print("%d|%s|" % (linha_numero, "|".join(linhas)))
        print(" +-+-+-+-+-+-+-+-+")
        linha_numero = linha_numero + 1



### Adicionando os navios no programa:
for navios in range(5):
    print("\nOnde quer colocar seu navio", navios+1, "?\n")
    linha_numero, coluna_numero = pergunta_posicao_tabuleiro()

    if tabuleiro[linha_numero][coluna_numero] == "X":
        print("\nJá possui um navio de batalha nesse local!\n")

    tabuleiro[linha_numero][coluna_numero] = 'X'
    print_tabuleiro(tabuleiro)


### Pra limpar o Terminal na vez de quem tenta adivinhar.
import os
clear = lambda: os.system('cls')
clear()



tabuleiro_convidado = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]




tentativas = 0
acertos = 0

### Loop para até 10 tentativas.
while tentativas < 10:
    print("Chute o local de um navio de batalha")
    linha_numero, coluna_numero = pergunta_posicao_tabuleiro()

    if tabuleiro_convidado[linha_numero][coluna_numero] != ' ':
        print("Você já chutou esse local!")
        continue

    if tabuleiro[linha_numero][coluna_numero] == 'X':
        print("\nACERTO!")
        tentativas = tentativas+1
        tabuleiro_convidado[linha_numero][coluna_numero] = 'X'
        acertos = acertos + 1

    if acertos == 5:
        print("\nVOCÊ GANHOU!")
        tentativas = 10

    else:
        print("\nERROU!")
        tabuleiro_convidado[linha_numero][coluna_numero] = '*'

    print_tabuleiro(tabuleiro_convidado)

print("\nFIM DE JOGO!\n")
