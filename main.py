import pygame       #Importa o Pygame
import Jackpot      #Importa o arquivo "Jackpot.py" feito por Joao Vitor 
import Blackjack    #Importa o arquivo "Blackjack.py" feito por Caio Lemos
import roulette     #Importa o arquivo "roulette.py" feito por Joao Marco

#Funções para o dinheiro
def ReadMoney():                            #Ler o arquivo "money.txt" na pasta raiz e retorna o valor do dinheiro do jogador
    money_file = open("money.txt", "r")
    coin = int(money_file.readline()) 
    money_file.close()
    return coin


def SaveMoney():                            #Sobre escreve o arquivo "money.txt" na pasta raiz, inserindo o valor atual do dinheiro do jogador
    money_file = open("money.txt", "w")
    money_file.write(str(coin))


pygame.init()                                       #Inicia os métodos e classes do Pygame 

#Variaveis globais
coin = ReadMoney()                                  #Armazena o valor da moeda
bet = 10                                            #Define a aposta
                                                    
#Variaveis globais a serem usadas pelo pygame       
white = (255, 255, 255)                             #Define a cor branco em RGB
black = (0, 0, 0)                                   #Define a cor preto em RGB
top_left = (0, 0)                                   #Define a borda superior esquerda da janela
small_font = pygame.font.SysFont('Georgia', 32)     #Define uma fonte para ser usada pelo pygame
text_winner = ""                                    #Texto que vai escrever se o usuario perdeu ou ganhou
total_player = 0                                    #Total da soma da mão do player no jogo "Blackjack" 
total_dealer = 0                                    #Total da soma da mão da mesa no jogo "Blackjack"


#Criando a tela
screen = pygame.display.set_mode((1024, 720))       #Define a janela por função do pygame
pygame.display.set_caption("Cassino's")             #Muda o nome da janela por função do pygame


#Variaveis que controlam as telas do jogo
menu = True                                         #Tela do menu
blackjack_screen = False                            #Tela do Blackjack
roulette_screen = False                             #Tela do Roulette
jackpot_screen = False                              #Tela do Jackpot

while True:                                         #Laço principal
    while menu == True:
        text_winner = ""                            #Limpa a variavel 
        Blackjack.resetar_maos()                    #Limpa a mão

        #Carregando as imagens para poder usar.
        background_menu = pygame.image.load("Sprites/sprites do menu/fundo.png")

        #Desenhando na tela.
        screen.blit(background_menu, top_left)

        #Recebendo a posiçao do ponteiro do mouse.
        mouse = pygame.mouse.get_pos()

        #Texto do dinheiro
        text_money = small_font.render(f"{coin}", True, black)
        screen.blit(text_money, (875, 30))

        for event in pygame.event.get():    # Passa por todos os eventos possiveis do Pygame.
            if event.type == pygame.QUIT:   # Se o botao "X" for clicado.
                pygame.display.quit()       # Fecha o pygame
                quit()                      
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:    #Se o botao do mouse for pressionado.
                print(mouse)
            
                if 371 <= mouse[0] <= 638 and 226 <= mouse[1] <= 322:       #Abre o Blackjak.
                    screen.fill(white)
                    blackjack_screen = True
                    menu = False
                
                if 370 <= mouse[0] <= 650 and 350 <= mouse[1] <= 440:       #Abre o jackpot.
                    screen.fill(white)
                    jackpot_screen = True
                    menu = False 

                if 389 <= mouse[0] <= 628 and 471 <= mouse[1] <= 528:       #Abre o roulette.
                    screen.fill(white)
                    roulette_screen = True
                    menu = False

                if 392 <= mouse[0] <= 634 and 579 <= mouse[1] <= 634:       #Botao de sair.
                    pygame.display.quit()
                    quit()
                    break
                    
        pygame.display.flip()   #Atualiza toda a tela 

    while blackjack_screen == True:
        
        #Carregando as imagens para poder usar.
        background_blackjack = pygame.image.load("Sprites/Blackjack/fundo_blackjack.jpg")

        #Desenhando na tela.
        screen.blit(background_blackjack, top_left)

        #Escrevendo na tela
        text_bet = small_font.render(f'{bet}', True, black)
        screen.blit(text_bet, (840, 100))
        
        total_player = Blackjack.get_total_maos()[1]
        total_dealer = Blackjack.get_total_maos()[0]
        text_hands = small_font.render(f"Sua mao soma {total_player}. E a mesa soma {total_dealer} ", True, black)
        screen.blit(text_hands, (80, 270))

        text_money = small_font.render(f"{coin}", True, black)
        screen.blit(text_money, (875, 30))
        
        winner = small_font.render(text_winner, True, black)
        screen.blit(winner, (740, 582))
        
        #Recebendo a posiçao do ponteiro do mouse.
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():                                #Passa por todos os eventos possiveis do Pygame.
            if event.type == pygame.QUIT:                               #Se o botao "X" for clicado.
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:                    #Se o botao do mouse for precionado

                #Altera o valor da aposta
                if 755 <= mouse[0] <= 850 and 215 <= mouse[1] <= 275:       #Diminui a aposta em 1, apenas se isso nao deixar menor que a aposta mim
                    if bet - 1 >= 10:
                        bet -= 1

                elif 863 <= mouse[0] <= 965 and 240 <= mouse[1] <= 300:     #Aumenta a aposta em 1
                    bet += 1

                elif 752 <= mouse[0] <= 851 and 291 <= mouse[1] <= 347:     #Diminui a aposta em 10, apenas se isso nao deixar menor que a aposta mim
                    if bet - 10 >= 10:
                        bet -= 10

                elif 869 <= mouse[0] <= 958 and 291 <= mouse[1] <= 343:     #Aumenta a aposta em 10
                    bet += 10

                elif 755 <= mouse[0] <= 847 and 363 <= mouse[1] <= 414:     #Diminui a aposta em 100, apenas se isso nao deixar menor que a aposta mim
                    if bet - 100 >= 10:
                        bet -= 100

                elif 870 <= mouse[0] <= 952 and 366 <= mouse[1] <= 420:     #Aumenta a aposta em 100
                    bet += 100
                
                #Define o jogo
                if 130 <= mouse[0] <= 340 and 600 <= mouse[1] <= 670:   #Botao "Sim"
                    if coin <= 9:
                        coin = 200
                    elif coin - bet < coin:
                        bet = 10
                    
                    if total_player < 21:
                        total_player  = Blackjack.comprar_carta(1)
                    
                if 345 <= mouse[0] <= 555 and 603 <= mouse[1] <= 671:   #Botao "Nao"
                    total_dealer = Blackjack.mesa_compra()
                    text_winner = Blackjack.vencedor()
                    Blackjack.resetar_maos()

                    if text_winner == "Você ganhou!":
                        coin += bet * 2
                        SaveMoney()

                    elif text_winner == "Você perdeu!" or text_winner == "Perderam!":
                        coin -= bet
                        SaveMoney()
                    
                if 20 <= mouse[0] <= 85 and 15 <= mouse[1] <= 50:   #Botao de voltar.
                    screen.fill(white)
                    menu = True
                    blackjack_screen = False

        pygame.display.flip()

    while jackpot_screen == True:
        #Carregando as imagens para poder usar.
        background_jackpot = pygame.image.load("Sprites/Jackpot/fundo_jackpot_2.png")
        
        #Desenhando na tela.
        screen.blit(background_jackpot, top_left)
        
        #Recebendo a posiçao do ponteiro do mouse.
        mouse = pygame.mouse.get_pos()

        text_money = small_font.render(f"{coin}", True, black)
        screen.blit(text_money, (875, 30))
        
        winner = small_font.render(text_winner, True, black)
        screen.blit(winner, (290, 635))

        #Laço que pecorre a lista de eventos do pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:    #Caso o mouse seja precionado.     
                if coin <= 9:
                    coin = 200

                jackpot =  Jackpot.jackpots(coin)
                text_winner = jackpot[0]
                coin = jackpot[1]
                SaveMoney()

                if 20 <= mouse[0] <= 85 and 15 <= mouse[1] <= 50:   #Botao de voltar.
                    screen.fill(white)
                    menu = True
                    jackpot_screen = False

        pygame.display.flip()

    while roulette_screen == True:
        #Carregando as imagens para poder usar.
        background_blackjack = pygame.image.load("Sprites/Roulette/fundo_roulette.jpeg")

        #Desenhando na tela.
        screen.blit(background_blackjack, top_left)

        #Recebendo a posiçao do ponteiro do mouse.
        mouse = pygame.mouse.get_pos()
        
        text_bet = small_font.render(f'{bet}', True, black)
        screen.blit(text_bet, (840, 100))
    
        text_money = small_font.render(f"{coin}", True, black)
        screen.blit(text_money, (875, 30))

        winner = small_font.render(text_winner, True, black)
        screen.blit(winner, (330, 375))

        #Laço que pecorre a lista de eventos do pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                #Altera o valor da aposta
                if 755 <= mouse[0] <= 850 and 215 <= mouse[1] <= 275:       #Diminui a aposta em 1, apenas se isso nao deixar menor que a aposta mim
                    if bet - 1 >= 10:
                        bet -= 1

                elif 863 <= mouse[0] <= 965 and 240 <= mouse[1] <= 300:     #Aumenta a aposta em 1
                    bet += 1

                elif 752 <= mouse[0] <= 851 and 291 <= mouse[1] <= 347:     #Diminui a aposta em 10, apenas se isso nao deixar menor que a aposta mim
                    if bet - 10 >= 10:
                        bet -= 10

                elif 869 <= mouse[0] <= 958 and 291 <= mouse[1] <= 343:     #Aumenta a aposta em 10
                    bet += 10

                elif 755 <= mouse[0] <= 847 and 363 <= mouse[1] <= 414:     #Diminui a aposta em 100, apenas se isso nao deixar menor que a aposta mim
                    if bet - 100 >= 10:
                        bet -= 100

                elif 870 <= mouse[0] <= 952 and 366 <= mouse[1] <= 420:     #Aumenta a aposta em 100
                    bet += 100
                
                #Testa as apostas
                if 110 <= mouse[0] <= 295 and 610 <= mouse[1] <= 660:       #Botao que aposta na cor vermelho
                    if coin <= 9:
                        coin = 200
                    elif coin - bet < coin:
                        bet = 10

                    game = roulette.roulette("Red", bet, coin)
                    
                    if game[1] == "winner":
                        text_winner = "Você ganhou"
                    else:
                        text_winner = "Você perdeu"

                    coin = game[0]
                    SaveMoney()
                    
                elif 325 <= mouse[0] <= 510 and 610 <= mouse[1] <= 660:     #Botao que aposta na cor preto
                    if coin <= 9:
                        coin = 200
                    elif coin - bet < coin:
                        bet = 10

                    game = roulette.roulette("Black", bet, coin)
                    
                    if game[1] == "winner":
                        text_winner = "Você ganhou"
                    else:
                        text_winner = "Você perdeu"

                    coin = game[0]
                    SaveMoney()
                    
                elif 540 <= mouse[0] <= 720 and 610 <= mouse[1] <= 660:     #Botao que aposta nos números pares
                    if coin <= 9:
                        coin = 200
                    elif coin - bet < coin:
                        bet = 10

                    game = roulette.roulette("Odd", bet, coin)

                    if game[1] == "winner":
                        text_winner = "Você ganhou"
                    else:
                        text_winner = "Você perdeu"

                    coin = game[0]
                    SaveMoney()

                elif 755 <= mouse[0] <= 940 and 610 <= mouse[1] <= 655:     #Botao que aposta nos números impares
                    if coin <= 9:
                        coin = 200
                    elif coin - bet < coin:
                        bet = 10

                    game = roulette.roulette("Even", bet, coin)
                    print("game", game)

                    if game[1] == "winner":
                        text_winner = "Você ganhou"
                    else:
                        text_winner = "Você perdeu"

                    coin = game[0]
                    SaveMoney()

                elif 20 <= mouse[0] <= 85 and 15 <= mouse[1] <= 50:         #Botao de voltar.
                    screen.fill(white)
                    menu = True
                    roulette_screen = False

            
        pygame.display.flip()
