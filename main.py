import pygame

pygame.init()

height = 1024
width = 720
white = (255, 255, 255)

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Cassino's")

buttons = pygame.image.load("Sprites/sprites do menu/menu_botões.png")
watch = pygame.time.Clock()


menu = True
blackjack_screen = False
roulette_screen = False
jackpot_screen = False

while True: #Laço principal 
    while menu == True:
        background_menu = pygame.image.load("Sprites/sprites do menu/fundo_1.png")
        mouse = pygame.mouse.get_pos()
        screen.blit(background_menu, (0,0))
        screen.blit(buttons, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)
            
                if 371 <= mouse[0] <= 649 and 226 <= mouse[1] <= 305:   #Abre o Blackjak
                    screen.fill(white)
                    blackjack_screen = True
                    menu = False
                
                if 370 <= mouse[0] <= 650 and 350 <= mouse[1] <= 440:   #Abre o jackpot
                    screen.fill(white)
                    jackpot_screen = True
                    menu = False 

                if 370 <= mouse[0] <= 650 and 480 <= mouse[1] <= 570:   #Abre o roulette
                    screen.fill(white)
                    roulette_screen = True
                    menu = False

                if 369 <= mouse[0] <= 657 and 613 <= mouse[1] <= 695:   #Botão de sair
                    pygame.display.quit()
                    quit()
                    break

        pygame.display.flip()

    while blackjack_screen == True:
        background_blackjack = pygame.image.load("Sprites/Blackjack/fundo_blackjack.png")
        screen.blit(background_blackjack, (0, 0))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)
            
        pygame.display.flip()

    while roulette_screen == True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)
            
        pygame.display.flip()

    while jackpot_screen == True:
        
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)
            
        pygame.display.flip()
