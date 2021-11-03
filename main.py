import random
import time
import os
import math

sentimentos = ['alegria', 'amor', 'cidadania', 'esperança','felicidade', 'harmonia',  'paz', 'perseverança', 'saudades','solidariedade',  'tristeza', 'ódio', 'raiva']
frutas = ['abacate', 'abacaxi', 'acerola', 'banana', 'caju','figo','framboesa', 'goiaba', 'kiwi', 'laranja', 'limão', 'maçã', 'mamão', 'melão', 'pêssego', 'tangerina', 'manga']
times = ['atlético', 'botafogo', 'corinthians', 'coritiba', 'cruzeiro', 'flamengo','fluminense', 'goiás','grêmio','internacional', 'náutico', 'palmeiras',  'santos',  'vasco', 'avaí', 'figueirense']

sentimentos_sa = ['alegria', 'amor', 'cidadania', 'esperança','felicidade', 'harmonia',  'paz', 'perseverança', 'saudades','solidariedade',  'tristeza', 'odio', 'raiva']
frutas_sa = ['abacate', 'abacaxi', 'acerola', 'banana', 'caju','figo','framboesa', 'goiaba', 'kiwi', 'laranja', 'limao', 'maça', 'mamao', 'melao', 'pessego', 'tangerina', 'manga']
times_sa = ['atletico', 'botafogo', 'corinthians', 'coritiba', 'cruzeiro', 'flamengo','fluminense', 'goias','grêmio','internacional', 'nautico', 'palmeiras',  'santos',  'vasco', 'avai', 'figueirense']

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
    if error == 1 or error == 1.5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if error == 2 :
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
    if error == 4 or error == 4.5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
    if error == 5 :
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
    if error == 7 or error == 7.5:
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
        Clear = lambda: os.system('clear')
        Clear()

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
        escolha_1 = sentimentos_sa[:]
        escolha_1_2 = sentimentos[:]
    elif menu_1 == '2':
        escolha_1 = frutas_sa[:]
        escolha_1_2 = frutas[:]
    elif menu_1 == '3':
        escolha_1 = times_sa[:]
        escolha_1_2 = times[:]
    index = random.randint(0,len(escolha_1)-1)
    
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
    palavra_print = escolha_1_2[index]
    #Funciona junto com o temp print
    #Um é para conferência e outro para mostrar no console
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
            
            checkAcerto = list(palavra_print)
            if checkAcerto == resposta:
                print("ACERTOU!")
                break

            entrada = input('Digite uma letra: ').lower()          
        if entrada not in palavra:
            if menu_2 == '3':
                errors += 3        
            elif menu_2 == '2':
                errors += 1.5
                # pensando ainda em uma forma de implementar 
                # essa parte da dificuldade 2
                # Kalleo -- Troquei o valor para 1.5 e modifiquei
                # dando a opção de números quebrados na função
            elif menu_2 == '1':
                errors += 1
        else:
            temp = list(palavra)
            temp_print = list(palavra_print)
            #o temp é para conferência e o temp_print
            #é enviado para a resposta para depois ser printado
            for i in range(len(temp)):
                if entrada == temp[i]:
                    resposta[i] = temp_print[i]
    
    while True:
        restart = input('\nDeseja jogar novamente [S/N]?\n').upper()
        if restart not in ('S', 'N'):
            print("Digite apenas 'S' ou 'N'.\n")
        else:
            break
    if restart == 'N':
        break



