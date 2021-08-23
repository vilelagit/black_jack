

def imprimirCartas(cartas):
    lista = [cartaMedia(carta) for carta in cartas]
    for card in zip(*lista):
            print('   '.join(card))

def cartaMedia(carta):
    if carta == "back":
        visual = [
            '╔══════╗',
            '║░░░░░░║',
            '║░░░░░░║',
            '║░░░░░░║',
            '╚══════╝'
            ]
        return visual
    else:
        visual = [
            '╔══════╗',
            f'║ {carta:<3}  ║',
            f'║      ║',
            f'║  {carta:>3} ║',
            '╚══════╝'
            ]
        return visual


def placar(dados):
    if dados[10] == 0:
        print('\nO jogador {} zerou suas fichas'.format(dados[5]))
        print('Se perder essa rodada será eliminado\n')
    if dados[11] == 0:
        print('\nO jogador {} zerou suas fichas'.format(dados[7]))
        print('Se perder essa rodada está eliminado\n')

    print('╔══════════════════════════════════════════╗')
    print('  {} - vitorias: {}'.format(dados[5], dados[6]))
    print('  {} - vitorias: {}'.format(dados[7], dados[8]))
    print('  Banca - vitorias: {}'.format(dados[9]))
    print('╔══════════════════════════════════════════╗')
    print('  Total em fichas {} - Aposta atual: {}   '.format(dados[1], dados[2]))
    print('╚══════════════════════════════════════════╝\n')   
