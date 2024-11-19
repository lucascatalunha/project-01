import time
print('Esse é um jogo do pedra, papel, tesoura.\nVocê, jogador, tem 15 segundos pensar no que você vai escolher para jogar.\nAntes da partida escolham quantas partidas vão ter.\nBom jogo!')
time.sleep(7)
num_parts = input('Melhor de: ')


num_parts_passadas = 0
while True:
    if num_parts_passadas == num_parts:
        break
    while True:
        mao1 = input('jogador 1, pense na escolha: ')

        if (mao1 == 'pedra' and mao1 != 'papel' and mao1 != 'tesoura') or (mao1 != 'pedra' and mao1 == 'papel' and mao1 != 'tesoura') or (mao1 != 'pedra' and mao1 != 'papel' and mao1 == 'tesoura'):
            break
        elif (mao1 != 'pedra' and mao1 != 'papel' and mao1 != 'tesoura'):
            print('Por favor escolha pedra, papel ou tesoura.')

    while True:
        mao2 = input('jogador 2, pense na escolha: ')

        if (mao2 == 'pedra' and mao2 != 'papel' and mao2 != 'tesoura') or (mao2 != 'pedra' and mao2 == 'papel' and mao2 != 'tesoura') or (mao2 != 'pedra' and mao2 != 'papel' and mao2 == 'tesoura'):
            break
        elif (mao2 != 'pedra' and mao2 != 'papel' and mao2 != 'tesoura'):
            print('Por favor escolha pedra, papel ou tesoura.')

    print('Escolhas feitas!')
    time.sleep(2)
    print('Preparados?!')
    time.sleep(2)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print(f'{mao1} vs {mao2}')
    time.sleep(1.5)
    if (mao1 == 'pedra' and mao2 == 'tesoura') or (mao1 == 'tesoura' and mao2 == 'papel') or (mao1 == 'papel' and mao2 == 'pedra'):
        print('Jogador 1 vence a rodada!!!')
    elif (mao2 == 'pedra' and mao1 == 'tesoura') or (mao2 == 'tesoura' and mao1 == 'papel') or (mao2 == 'papel' and mao1 == 'pedra'):
        print('Jogador 2 vence a rodada!!!')
    elif (mao2 == 'pedra' and mao1 == 'pedra') or (mao2 == 'tesoura' and mao1 == 'tesoura') or (mao2 == 'papel' and mao1 == 'papel'):
        print('Empate!!!')
        num_parts_passadas += 1
