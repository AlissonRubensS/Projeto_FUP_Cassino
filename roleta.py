from random import randint

Black = [4,2,15,11,17,6,10,13,20,22,8,33,26,24,31,35,28,29]
Red = [1,3,18,7,5,21,9,16,24,14,12,26,30,27,19,32,23,25]

mult = 0
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
    
        else:
            aposta() #chama novamente a aposta

def BetTypeEvenOrOdd(BetCoins, EvenOrOdd):  #chama a função da aposta de impar ou par
    
    if BetCoins > 0 and BetCoins <= Coins: #checa se a apostá é possivel
        Bet['BetValue'] = BetCoins # define o valor da aposta no dicionario
        
        if EvenOrOdd == 'Even': #caso a aposta seja par
            Bet.update({'EvenorOdd': 'Even'}) #adicina o tipo da aposta no dicionario
            EvenOrOddCheck() #chama a wincondition
       
        elif EvenOrOdd == 'Odd': # caso a aposta seja impar, faz a mesma coisa
            Bet.update({'EvenorOdd': 'Odd'})
            EvenOrOddCheck()
       
        else:
            aposta() #caso a aposta nãa seja definida chama a função de aposta novamente, para que seja resetado
        
def BetTypeDozen(BetCoins, Dozens): #DUZIAS
    
    if BetCoins > 0 and BetCoins <= Coins: #checa se a aposta é possivel
        Bet['BetValue'] = BetCoins #define o valor da aposta no dicionario

        if Dozens == 1: # caso a aposta seja feita no 1, ela vai fazer na primeira duzia 1 a 12
            Bet.update({'Dozen': 'First'}) #adiciona a informação no dicionario
            Dozencheck() #puxa a wincondition
        
        if Dozens == 2: # caso a aposta seja feita no 2, ela vai fazer na primeira duzia 13 a 24
            Bet.update({'Dozen': 'Second'}) #adiciona a informação no dicionario
            Dozencheck()#puxa a wincondition
        
        if Dozens == 3: # caso a aposta seja feita no 3, ela vai fazer na primeira duzia 25 a 36
            Bet.update({'Dozen': 'Third'}) #adiciona a informação no dicionario
            Dozencheck()#puxa a wincondition
        
        else:
            aposta()#caso a aposta nãa seja definida chama a função de aposta novamente, para que seja resetado
        
    
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
  
def Dozencheck(): #wincondition das duzias
    
    NumSort = randint(1,36) #sorteia  o numero
    print(NumSort)
    if Bet['Dozen'] == 'First' and 1 <= NumSort <= 12: # checa a duzia apostada
        Bet.update({'WinOrLose':'Win'}) # faz o update do dicionar
        
    elif Bet['Dozen'] == 'Second' and 13 <= NumSort <= 24:
        Bet.update({'WinOrLose':'Win'})
    
    elif Bet['Dozen'] == 'Third' and 25 <= NumSort <= 36:
        Bet.update({'WinOrLose' : 'Win'})
    
    else:
        Bet.update({'WinOrLose':'Lose'})
        
    
def result():
    global mult, Coins
    
    if Bet['WinOrLose'] == 'Win':
        
        if Bet['BetType'] == 'Colors':
            mult = 2
        
        elif Bet['BetType'] == 'EvenOrOdd':
            mult = 3
        
        elif Bet['BetType'] == 'Dozens':
            print('vezes 5')
            mult = 5
        
        Coins = Bet['BetValue'] * mult + Coins
        print(Coins)
    
    elif Bet['WinOrLose'] == 'Lose':
        
        Coins = Coins - Bet['BetValue']
        print(Coins)
    
    else:
        print('Erro')
    
def aposta():
    global Bet
    BetType = int(input('a: '))
    Bet = {
    'BetType':'none',
    'BetValue': 0,
      }
    
    if BetType == 1:
        Bet['BetType'] = 'Colors'
        BetTypeColors(100, 'Black')
    
    elif BetType == 2:
        Bet['BetType'] = 'EvenOrOdd'
        BetTypeEvenOrOdd(100, 'Even')
        
    elif BetType == 3:
        Bet['BetType'] = 'Dozens'
        BetTypeDozen(100, 1)
    
while True:
        aposta()
        result()
