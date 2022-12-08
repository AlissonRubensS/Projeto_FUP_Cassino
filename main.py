import pygame       #Importa o Pygame
import Jackpot      #Importa o arquivo "Jackpot.py" feito por João Vitor 
import Blackjack    #Importa o arquivo "Blackjack.py" feito por Caio Lemos

#Funções para o dinheiro
def ReadMoney():                            #Ler o arquivo "money.txt" na pasta raiz e retorna o valor do dinheiro do jogador
    money_file = open("money.txt", "r")
    coin = int(money_file.readline()) 
    money_file.close()
    return coin

def SaveMoney():                            #Sobre escreve o arquivo "money.txt" na pasta raiz, inserindo o valor atual do dinheiro do jogador
    money_file = open("money.txt", "w")
    money_file.write(str(coin))

#Função para decidir o vencedor do jogo Blackjack
def BlackjackWinner():
    global coin 
    #Blackjack.get_total_maos()[1] => Mão do jogador
    #Blackjack.get_total_maos()[0] => Mão da mesa

    if Blackjack.get_total_maos()[1] > Blackjack.get_total_maos()[0] and Blackjack.get_total_maos()[1] < 22 and Blackjack.get_total_maos()[0] < 22:
        coin += bet * 2
        SaveMoney()
        txt = 'Você ganhou!'

    elif Blackjack.get_total_maos()[1] > 21 and Blackjack.get_total_maos()[0] > 21:
        txt = 'Você e a mesa perderam!'

    elif Blackjack.get_total_maos()[1] < 22 and Blackjack.get_total_maos()[0] > 21:
        coin += bet * 2
        SaveMoney()
        txt = 'Você ganhou!'

    elif Blackjack.get_total_maos()[1] == Blackjack.get_total_maos()[0] and Blackjack.get_total_maos()[1] < 22:
        txt = 'Você empatou com a mesa!'

    elif Blackjack.get_total_maos()[0] > Blackjack.get_total_maos()[1] and Blackjack.get_total_maos()[0] < 22 and Blackjack.get_total_maos()[1] < 22:
        coin += bet * 2
        SaveMoney()
        txt = 'A mesa ganhou!'

    elif Blackjack.get_total_maos()[0] < 22 and Blackjack.get_total_maos()[1] > 21:
        coin += bet * 2
        SaveMoney()
        txt = 'A mesa ganhou!'
    
    return txt

pygame.init()               #Inicia os métodos e classes do Pygame 

#Variáveis globais 
coin = ReadMoney()                                  #Armazena o valor da moeda
bet = 0                                             #Aposta

#Variaveis globais a serem usadas pelo pygame
height = 1024                                       #Define a altura da janela
width = 720                                         #Define a largura da janela 
white = (255, 255, 255)                             #Define a cor branco em RGB
black = (0, 0, 0)                                   #Define a cor preto em RGB
top_left = (0, 0)                                   #Define a borda superior esquerda da janela
small_font = pygame.font.SysFont('Georgia', 32)     #Define uma fonte para ser usada pelo pygame


#Criando a tela
screen = pygame.display.set_mode((height, width))   #Define a janela 
pygame.display.set_caption("Cassino's")             #Muda o nome da janela 


#Variáveis que controlam as telas do jogo
menu = True                                 #Tela do menu
blackjack_screen = False                    #Tela do Blackjack
roulette_screen = False                     #Tela do Roulette
jackpot_screen = False                      #Tela do Jackpot

text_winner = ""
while True: #Laço principal.
    while menu == True:
        #Carregando as imagens para poder usar.
        background_menu = pygame.image.load("Sprites/sprites do menu/fundo.png")
        buttons = pygame.image.load("Sprites/sprites do menu/menu_botões.png")

        #Desenhando na tela.
        screen.blit(background_menu, top_left)
        screen.blit(buttons, top_left)

        #Recebendo a posição do ponteiro do mouse.
        mouse = pygame.mouse.get_pos()

        #Texto do dinheiro
        text_money = small_font.render(f"{coin}", True, black)
        screen.blit(text_money, (865, 640))

        for event in pygame.event.get():    # Passa por todos os eventos possiveis do Pygame.
            if event.type == pygame.QUIT:   # Se o botão "X" for clicado.
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:    #Se o botão do mouse for pressionado.
                print(mouse)
            
                if 371 <= mouse[0] <= 649 and 226 <= mouse[1] <= 305:   #Abre o Blackjak.
                    screen.fill(white)
                    blackjack_screen = True
                    menu = False
                
                if 370 <= mouse[0] <= 650 and 350 <= mouse[1] <= 440:   #Abre o jackpot.
                    screen.fill(white)
                    jackpot_screen = True
                    menu = False 

                if 370 <= mouse[0] <= 650 and 480 <= mouse[1] <= 570:   #Abre o roulette.
                    screen.fill(white)
                    roulette_screen = True
                    menu = False

                if 369 <= mouse[0] <= 657 and 613 <= mouse[1] <= 695:   #Botão de sair.
                    pygame.display.quit()
                    quit()
                    break

        pygame.display.flip()

    while blackjack_screen == True:
        
        #Carregando as imagens para poder usar.
        background_blackjack = pygame.image.load("Sprites/Blackjack/fundo_blackjack.jpg")

        #Desenhando na tela.
        screen.blit(background_blackjack, top_left)

        #Escrevendo na tela
        text_bet = small_font.render(f'{bet}', True, black)
        screen.blit(text_bet, (840, 173))
        
        text_money = small_font.render(f"{coin}", True, black)
        screen.blit(text_money, (865, 640))
        
        total_hands = (Blackjack.get_total_maos())
        text_hands = small_font.render(f"Sua mão soma {total_hands[1]}. E a mesa soma {total_hands[0]} ", True, black)
        screen.blit(text_hands, (80, 270))

        
        winner = small_font.render(text_winner, True, black)
        screen.blit(winner, (105, 560))
        
        #Recebendo a posição do ponteiro do mouse.
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():                                #Passa por todos os eventos possiveis do Pygame.
            if event.type == pygame.QUIT:                               #Se o botão "X" for clicado.
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:                    #Se o botão do mouse for precionado
                print(f"x = {mouse[0]} e y = {mouse[1]} ")              

                if 765 <= mouse[0] <= 950 and 275 <= mouse[1] <= 340:   #Aumenta a aposta em 1
                    bet += 1
                #    print("+1", bet)
                
                if 765 <= mouse[0] <= 950 and 355 <= mouse[1] <= 415:   #Aumenta a aposta em 10
                    bet += 10
                #    print("+10", bet)

                if 765 <= mouse[0] <= 950 and 430 <= mouse[1] <= 490:   #Aumenta a aposta em 100
                    bet += 100
                #    print("+100", bet)

                if 130 <= mouse[0] <= 300 and 640 <= mouse[1] <= 686:   #Botão "Sim"
                    if coin <= 0:
                        coin = 200
                    Blackjack.comprar_carta(1)
                    text_winner = BlackjackWinner()
                    print(BlackjackWinner())

                if 375 <= mouse[0] <= 554 and 630 <= mouse[1] <= 695:   #Botão "Não"
                    Blackjack.comprar_carta(0)
                    text_winner = BlackjackWinner()
                    print(BlackjackWinner())

                if 15 <= mouse[0] <= 150 and 20 <= mouse[1] <= 100:   #Botão de voltar.
                    screen.fill(white)
                    menu = True
                    blackjack_screen = False
        
        pygame.display.flip()


    while jackpot_screen == True:
        #Carregando as imagens para poder usar.
        background_jackpot = pygame.image.load("Sprites/Jackpot/fundo_jackpot.png")
        
        #Desenhando na tela.
        screen.blit(background_jackpot, top_left)
        
        #Recebendo a posição do ponteiro do mouse.
        mouse = pygame.mouse.get_pos()

        text_money = small_font.render(f"{coin}", True, black)
        screen.blit(text_money, (865, 640))
        
        #Laço que pecorre a lista de eventos do pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:    #Caso o mouse seja precionado.     
                if coin <= 0:
                    coin = 200

                elif Jackpot.jackpots():
                    print("JACKPOTS!!!!")
                    coin += 200
                    SaveMoney()

                else:
                    coin -= 10
                    SaveMoney()

        pygame.display.flip()

    while roulette_screen == True:
        #Recebendo a posição do ponteiro do mouse.
        mouse = pygame.mouse.get_pos()

        text_money = small_font.render(f"{coin}", True, black)
        screen.blit(text_money, (865, 640))
        
        #Laço que pecorre a lista de eventos do pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)
            
        pygame.display.flip()
