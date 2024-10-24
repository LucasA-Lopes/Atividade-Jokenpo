import random
import time
print('*-'*35)
opcao = str(input('Vamos Jogar Jokenpô? \nDigite Sim ou Não: ')).strip()

if opcao == 'Sim' or opcao == 'S' or opcao == 'SIM':
    print('OK')
    print('Processando minha escolha...')
    time.sleep(3)
    pc = ['PEDRA', 'PAPEL', 'TESOURA']
    pc = random.choice(pc)

    print('Pronto, Tente ganhar de Mim: ')
    jogador = str(input('Escreva sua escolha em letra maiúscula: ')).strip()
    print('JO')
    time.sleep(1.5)
    print('KEN')
    time.sleep(1.5)
    print('PÔ')
    time.sleep(2.5)
    print('*-' *25)
    time.sleep(1.5)
    print('Computador escolheu {}'.format(pc))
    print('Jogador escolheu {}'.format(jogador))
    print('*-' *25)
    if (pc == "PEDRA"):
        if jogador == 'PEDRA':
            print('EMPATE')
        elif jogador == 'TESOURA':
            print('HAHAHAH VOCÊ PERDEU')
        elif jogador == 'PAPEL':
            print('PARABÉNS VOCÊ VENCEU')
        else:
            print('JOGADA INVÀLIDA')
    if pc == 'PAPEL':
        if jogador == 'PEDRA':
            print('HAHAJA VOCÊ PERDEU')
        elif jogador == 'PAPEL':
            print('EMPATE')
        elif jogador == 'TESOURA':
            print('PARABÈNS VOCÊ VENCEU')
        else:
            print('JOGADA INVÁLIDA')

    if pc == 'TESOURA':
        if jogador == 'PEDRA':
            print('PARABÉNS VOCÊ VENCER')
        if jogador == 'PAPEL':
            print('JHAHAHA VOCÊ PERDEU')
        if jogador == 'TESOURA':
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')


elif opcao == 'Não' or opcao == 'N' or opcao == 'NÃO' or opcao == 'NAO':
    print('Ok')
    time.sleep(1.5)
    print('Encerrando...')
    time.sleep(3)
    print('Encerrado.')
else:
    print('Inválido. Tente Novamente!')