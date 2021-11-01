import random
import time
import os
import math

sentimentos = ['alegria', 'amor', 'cidadania', 'esperança','felicidade', 'harmonia',  'paz', 'perseverança', 'saudades','solidariedade',  'tristeza', 'odio', 'raiva']
frutas = ['abacate', 'abacaxi', 'acerola', 'banana', 'caju''igo','framboesa', 'goiaba', 'kiwi', 'laranja', 'limão', 'maçã', 'mamão', 'melão', 'pêssego', 'tangerina', 'manga']
times = ['atlético', 'botafogo', 'corinthians', 'coritiba', 'cruzeiro', 'flamengo','fluminense', 'goiás','grêmio','internacional', 'náutico', 'palmeiras',  'santos',  'vasco', 'avaí', 'figueirense']


# Desenha o boneco a cada erro
# @params error
def drawDoll (error):
    if error == 0:
        print("  _______     ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if error == 1:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if error == 2:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if error == 3 :
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if error == 4:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
    if error == 5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    if error == 6:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    if error == 7:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    if error == 8:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if error >= 9:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print("    ACABOU!   ")
        time.sleep(2)
        clear = lambda: os.system('clear')
        clear()

while True:       
    while True:
        print('TIPO DE JOGO\n')
        print('[1]SENTIMENTOS')
        print('[2]FRUTAS')
        print('[3]TIMES')
    
        menu_1 = input('Digite o número do tipo escolhido: ')
        if menu_1 not in('1','2','3'):
            print('Digite apenas um número de 1 a 3.\n')
        else:
            break

    if menu_1 == '1':
        escolha_1 = sentimentos[:]
    elif menu_1 == '2':
        escolha_1 = frutas[:]
    elif menu_1 == '3':
        escolha_1 = times[:]
    index = random.randint(0,len(escolha_1))
    
    while True:
        print('\nDIFICULDADE DO JOGO\n')
        print('[1] FÁCIL(9 CHANCES)')
        print('[2] MÉDIO(6 CHANCES)') 
        print('[3] DIFÍCIL(3 CHANCES)')
        menu_2 = input('Digite o número da dificuldade escolhida: ')
        if menu_2 not in ('1','2','3'):
            print('Digite apenas um número de 1 a 3.\n')
        else:
            break
    
    palavra = escolha_1[index]
    errors = 0
    resposta = ["_"] * len(palavra)
    while errors <= 9:
        drawDoll(errors)
        if errors < 9:
            for i in range(len(resposta)):
                if i != len(resposta) - 1:
                    print(resposta[i], end=" ")
                else:
                    print(resposta[i])
            
            checkAcerto = list(palavra)
            if checkAcerto == resposta:
                print("ACERTOU!")
                break

            entrada = input('Digite uma letra: ').lower()          
        if entrada not in palavra:
            if menu_2 == '3':
                errors += 3        
            elif menu_2 == '2':
                errors += 2     
                # pensando ainda em uma forma de implementar 
                # essa parte da dificuldade 2
            else:
                errors += 1
        else:
            temp = list(palavra)
            for i in range(len(temp)):
                if entrada == temp[i]:
                    resposta[i] = entrada
    
    while True:
        restart = input('\nDeseja jogar novamente [S/N]?\n').upper()
        if restart not in ('S', 'N'):
            print("Digite apenas 'S' ou 'N'.\n")
        else:
            break
    if restart == 'N':
        break



