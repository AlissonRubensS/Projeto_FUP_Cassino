import random

money = open("money.txt", "r")

moeda_inicial = money.readline()
moeda_inicial = int(moeda_inicial)

money.close()

def get_moeda_inicial():    #Retorna o valor da moeda inicial para que possa ser usado em outro arquivo
    return moeda_inicial

def set_moeda_initial(money):   #Altera o valor da moeda inicial a partir de outro arquivo
    global moeda_inicial
    moeda_inicial = money

def salvar_moeda():
    moeda = open("money.txt", "w")
    moeda.write(str(moeda_inicial))
    moeda.close()

def jackpots(): 
    global moeda_inicial
    lista = ["diamante", "tesouro", "moeda"]

    a = (str(random.choice(lista)))
    b = (str(random.choice(lista)))
    c = (str(random.choice(lista)))

    jackpot = a==b==c or a==c==b or b==c==a or b==a==c or c==a==b or c==b==a

    print(a,b,c)
    if jackpot:
        print("JACKPOT!")
        moeda_inicial += 200
    else:
        print("Tente novamente")
        moeda_inicial -= 10
    print("O seu saldo e:", moeda_inicial)

    salvar_moeda()
