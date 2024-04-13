cinema = {
    'salas': {
        'sala001': {
            'numero': 1,
            'capacidade': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'reservas': [],
            'filmes_em_cartaz': ['Filme A', 'Filme B', 'Filme C']
        },
        'sala002': {
            'numero': 2,
            'capacidade': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'reservas': [],
            'filmes_em_cartaz': ['Filme A', 'Filme B', 'Filme C']
        },
        'sala003': {
            'numero': 3,
            'capacidade': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'reservas': [],
            'filmes_em_cartaz': ['Filme A', 'Filme B', 'Filme C']
        },
        'sala004': {
            'numero': 4,
            'capacidade': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'reservas': [],
            'filmes_em_cartaz': ['Filme A', 'Filme B', 'Filme C']
        }
    }
}

def compra_ingresso(sala, cadeira_reservada):
    if cadeira_reservada in cinema['salas'][sala]['capacidade']:
        if cadeira_reservada not in cinema['salas'][sala]['reservas']:
            cinema['salas'][sala]['reservas'].append(cadeira_reservada)
            print("Ingresso comprado com sucesso!")
        else:
            print("Esta cadeira já está reservada!")
    else:
        print("Cadeira inválida!")

print("MENU:\nEscolha uma sala :\n\t(a)Sala 1\n\t(b)Sala 2\n\t(c)Sala 3\n\t(d)Sala 4\n\t Digite 0 para sair")
while True:
    res = input('=>')
    if res == 'a':
        print(f'Cadeiras disponíveis na sala 1: {cinema["salas"]["sala001"]["capacidade"]}')
        reserva = int(input('Escolha uma cadeira: '))
        compra_ingresso("sala001", reserva)
    elif res == 'b':
        print(f'Cadeiras disponíveis na sala 2: {cinema["salas"]["sala002"]["capacidade"]}')
        reserva = int(input('Escolha uma cadeira: '))
        compra_ingresso("sala002", reserva)
    elif res == 'c':
        print(f'Cadeiras disponíveis na sala 3: {cinema["salas"]["sala003"]["capacidade"]}')
        reserva = int(input('Escolha uma cadeira: '))
        compra_ingresso("sala003", reserva)
    elif res == 'd':
        print(f'Cadeiras disponíveis na sala 4: {cinema["salas"]["sala004"]["capacidade"]}')
        reserva = int(input('Escolha uma cadeira: '))
        compra_ingresso("sala004", reserva)
    elif res == '0':
        break
    else:
        print("Opção inválida. Escolha novamente.")