def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 10)

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    # Verifica diagonais
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador) or \
       (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador):
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" "]*3 for _ in range(3)]
    jogador = "X"
    jogadas_restantes = 9

    while jogadas_restantes > 0:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador}")
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            jogadas_restantes -= 1
            if verificar_vitoria(tabuleiro, jogador):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                break
            jogador = "O" if jogador == "X" else "X"
        else:
            print("Essa posição já está ocupada. Escolha outra.")

    if jogadas_restantes == 0:
        imprimir_tabuleiro(tabuleiro)
        print("O jogo terminou em empate.")

# Iniciar o jogo
jogo_da_velha()