import random

def jackpots(coin): 
    global moeda
    lista = ["diamante", "tesouro", "moeda"]

    a = (str(random.choice(lista)))
    b = (str(random.choice(lista)))
    c = (str(random.choice(lista)))

    jackpot = a==b==c or a==c==b or b==c==a or b==a==c or c==a==b or c==b==a
    print(a, b, c)
    
    if jackpot:
        text = "VOCÊ GANHOU!!!!"
        coin += 200
    else:
        text = "VOCÊ PERDEU!!!!"
        coin -= 10

    return (text, coin)
