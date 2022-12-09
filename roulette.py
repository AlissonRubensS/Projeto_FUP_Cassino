from random import randint

Black = [4,2,15,11,17,6,10,13,20,22,8,33,26,24,31,35,28,29]
Red = [1,3,18,7,5,21,9,16,24,14,12,26,30,27,19,32,23,25]

Coins = 1000


def BetTypeColors(BetCoins, Color): # aposta por cores 2x    
    
    if BetCoins > 0 and BetCoins <= Coins: # checa se a aposta é valida
        Bet['BetValue'] = BetCoins #define o valor da aposta e joga para o dicionario
    
        if Color == 'Red': #checa a cor apostada
            Bet.update({'Color':'Red'}) #joga a cor para o dicionario
            ColorsCheck() #chama a função de win condition
    
        elif Color == 'Black': #checa a cor apostada
            Bet.update({'Color':'Black'}) #joga a cor para o dicionario
            ColorsCheck() #chama a wincondition

def BetTypeEvenOrOdd(BetCoins, EvenOrOdd):  #chama a função da aposta de impar ou par

    if BetCoins > 0 and BetCoins <= Coins: #checa se a apostá é possivel
        Bet['BetValue'] = BetCoins # define o valor da aposta no dicionario
        
        if EvenOrOdd == 'Even': #caso a aposta seja par
            Bet.update({'EvenorOdd': 'Even'}) #adicina o tipo da aposta no dicionario
            EvenOrOddCheck() #chama a wincondition
       
        elif EvenOrOdd == 'Odd': # caso a aposta seja impar, faz a mesma coisa
            Bet.update({'EvenorOdd': 'Odd'})
            EvenOrOddCheck()

def ColorsCheck(): # wincondition das cores
    
    NumSort = randint(1,36) # sorteia os numeros
    
    if  Bet['Color'] == 'Red' and NumSort in Red:
            Bet.update({'WinOrLose':'Win'}) #caso esteja ele adiciona o estado de vitoria
    
    elif Bet['Color'] == 'Black' and NumSort in Black:
            Bet.update({'WinOrLose':'Win'})
    
    else:
        Bet.update({'WinOrLose':'Lose'})
    
def EvenOrOddCheck(): # wincondition do impar ou par

    NumSort = randint(1,36) #sorteia o numero
    
    if Bet['EvenorOdd'] == 'Even' and NumSort % 2 == 0: #checa se o numero é par   
        Bet.update({'WinOrLose':'Win'}) #se sim, ele adiciona a condição de vitoria

    elif Bet['EvenorOdd'] == 'Odd' and NumSort %2 != 0:
        Bet.update({'WinOrLose': 'Win'})
            
    else:
         Bet.update({'WinOrLose':'Lose'})
  
def result(Coins): #calcula o resultado

    if Bet['WinOrLose'] == 'Win':
        if Bet['BetType'] == 'Colors': #checa o tipo de aposta e a condição de vitoria
            win_or_lose = "winner"
            mult = 2 #muda o multiplicador

        elif Bet['BetType'] == 'EvenOrOdd':   #checa o tipo de aposta e a condição de vitoria
            win_or_lose = "winner"
            mult = 4 #muda o multiplicador

        Coins = Coins + (mult * Bet['BetValue'])
        return (Coins, win_or_lose)
    
    else:
        win_or_lose = "loser"
        Coins = Coins - Bet['BetValue']
        
        return (Coins, win_or_lose) 
    
def roulette(BetType, BetCoins, Money): #Parte principal
    global Bet, NumSort #globais

    #define o dicionario
    Bet = {
    'BetType':'none',
    'BetValue': 0,
    'WinOrLose': 'none'
      }
    
    if BetType == "Red": # aposta de cores
        Bet['BetType'] = 'Colors'
        BetTypeColors(BetCoins= BetCoins, Color= "Red")
    
    elif BetType == "Black": # aposta de cores
        Bet['BetType'] = 'Colors'
        BetTypeColors(BetCoins= BetCoins, Color= "Black")

    elif BetType == "Even": # aposta de impar ou par
        Bet['BetType'] = 'EvenOrOdd'
        BetTypeEvenOrOdd(BetCoins= BetCoins, EvenOrOdd= "Even")
    
    elif BetType == 'Odd': # aposta de impar ou par
        Bet['BetType'] = 'EvenOrOdd'
        BetTypeEvenOrOdd(BetCoins= BetCoins, EvenOrOdd= 'Odd')
    
    return result(Money)

# for i in range(10):
#     Main('Odd', 100, 1000)
