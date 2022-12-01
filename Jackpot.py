import random

moedainicial = 200

def jackpots():
    global moedainicial
    lista = ["diamante", "tesouro", "moeda"]
    input("Para Girar o Jackpot basta apertar o Botao Enter, Ate que Fique com 0 ou 1000!")

    a = (str(random.choice(lista)))
    b = (str(random.choice(lista)))
    c = (str(random.choice(lista)))

    jackpot = a==b==c or a==c==b or b==c==a or b==a==c or c==a==b or c==b==a

    print(a,b,c)
    if jackpot:
        print("JACKPOT!")
        moedainicial += 200
    else:
        print("Tente novamente")
        moedainicial -= 10
    print("O seu saldo e:", moedainicial)

while True:
    if moedainicial > 0:
        jackpots()
    if moedainicial <= 0:
        moedainicial = 0
        break
    if moedainicial >= 1000:
        moedainicial = 1000
        print("VOCE VENCEU O JACKPOT!!")
        break
