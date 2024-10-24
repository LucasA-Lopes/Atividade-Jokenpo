import random
import time
print('*-'*35)
opcao = str(input('Vamos Jogar Jokenpô? \nDigite Sim ou Não: ')).strip() #Pergunta ao usuário se deseja jogar

if opcao == 'Sim' or opcao == 'S' or opcao == 'SIM': #se SIM vai carregar o código com as Opções
    print('OK')
    print('Processando minha escolha...')
    time.sleep(3)                                   #o modulo time e a função sleep é para fazer uma simulação de contagem de carregamento
    pc = ['PEDRA', 'PAPEL', 'TESOURA']              #fiz uma lista simples das opções para o pc escolher
    pc = random.choice(pc)                          #O pc ira usar a função choice do modulo random para escolher a opção aleatoria da lista acima

    print('Pronto, Tente ganhar de Mim: ')
    jogador = str(input('Escreva sua escolha em letra maiúscula: ')).strip()        #O usuário irá entrar com a opção com letras maiúsculas
    print('JO')                                                                     #Essa contagem vai fazer com que o usuário espere
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
    if (pc == "PEDRA"):                  #Se o pc escolher PEDRA no aleatorio vai fazer a logica do jokenpo e declarar o vencedor, logica utilizando o if, elif, e else                                          
        if jogador == 'PEDRA':
            print('EMPATE')
        elif jogador == 'TESOURA':
            print('HAHAHAH VOCÊ PERDEU')
        elif jogador == 'PAPEL':
            print('PARABÉNS VOCÊ VENCEU')
        else:
            print('JOGADA INVÀLIDA')
    if pc == 'PAPEL':                      #Se o pc escolher PAPAEL no aleatorio vai fazer a logica do jokenpo e declarar o vencedor, logica utilizando o if, elif, e els
        if jogador == 'PEDRA':
            print('HAHAJA VOCÊ PERDEU')
        elif jogador == 'PAPEL':
            print('EMPATE')
        elif jogador == 'TESOURA':
            print('PARABÈNS VOCÊ VENCEU')
        else:
            print('JOGADA INVÁLIDA')

    if pc == 'TESOURA':                   #Se o pc escolher TESOURA no aleatorio vai fazer a logica do jokenpo e declarar o vencedor, logica utilizando o if, elif, e els
        if jogador == 'PEDRA':
            print('PARABÉNS VOCÊ VENCER')
        if jogador == 'PAPEL':
            print('JHAHAHA VOCÊ PERDEU')
        if jogador == 'TESOURA':
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')


elif opcao == 'Não' or opcao == 'N' or opcao == 'NÃO' or opcao == 'NAO':     #Se o usuário digitar a OPÇÂO NÂO no inicio do programa, irá carregar esses comandos para encerrar o programa
    print('Ok')
    time.sleep(1.5)
    print('Encerrando...')
    time.sleep(3)
    print('Encerrado.')
else:
    print('Inválido. Tente Novamente!')
