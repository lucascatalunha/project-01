
# verificacao = True
# while True:
#     mao1 = input('jogador 1, pense na escolha: ')
#     if mao1 == 'pedra' or 'papel' or 'tesoura':
#         break
#     else:
#         print('Por favor escolha pedra, papel ou tesoura.')
# if mao1 == 'pedra' or 'papel' or 'tesoura':
#     verificacao = False
#     break


while True:

    mao1 = input('jogador 1, pense na escolha: ')

    if (mao1 == 'pedra' and mao1 != 'papel' and mao1 != 'tesoura') or (mao1 != 'pedra' and mao1 == 'papel' and mao1 != 'tesoura') or (mao1 != 'pedra' and mao1 != 'papel' and mao1 == 'tesoura'):
        break
    elif (mao1 != 'pedra' and mao1 != 'papel' and mao1 != 'tesoura'):
        print('Por favor escolha pedra, papel ou tesoura.')

    # if mao1 == 'pedra' or 'papel' or 'tesoura':
    #  break

    # mao2 = str(input('jogador 2, pense na escolha: '))

    # if mao2 != "pedra" or 'papel' or 'tesoura':
    #  print('Por favor escolha pedra, papel ou tesoura.')
