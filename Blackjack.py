from random import *

baralho = []
baralho_usavel = []
naipes = {
    0:' de Copas',
    1:' de Ouros',
    2:' de Espadas',
    3:' de Paus'
}

mao_do_jogador = []
mao_da_mesa = []

# Definindo a criaçao do baralho:
def criar_baralho():
    for i in range(0,52):
        baralho.append((i%13+1,naipes[int(i/13)]))
        baralho_usavel.append((i%13+1,naipes[int(i/13)]))

# Definindo o reembaralhamento quando o baralho tiver menos de 5 cartas:
def reembaralhar():
    baralho_usavel.clear()
    for i in baralho:
        baralho_usavel.append(i)

# Definindo quem é o vencedor:
def vencedor():
    if total_jogador > total_mesa and total_jogador < 22 and total_mesa < 22:
        return "Você ganhou!"

    elif total_jogador > 21 and total_mesa > 21:
        return "Perderam!"

    elif total_jogador < 22 and total_mesa > 21:
        return "Você ganhou!"

    elif total_jogador == total_mesa and total_jogador < 22:
        return "Empataram!"

    elif total_mesa > total_jogador and total_mesa < 22 and total_jogador < 22:
        return "Você perdeu!"

    elif total_mesa < 22 and total_jogador > 21:
        return "Você perdeu!"

# Definindo a criaçao da mao do jogador:
def mao_jogador():
    global mao_do_jogador

    shuffle(baralho_usavel)

    for i in range(0,2):
        mao_do_jogador.append(baralho_usavel.pop())
    return mao_do_jogador

# Definindo a mao da mesa:
def mao_mesa():
    global mao_da_mesa

    for i in range(0,2):
        shuffle(baralho_usavel)
        mao_da_mesa.append(baralho_usavel.pop())
    return mao_da_mesa


# Definindo a compra de cartas do jogador:
def comprar_carta(devecomprar):
    global total_jogador, total_mesa
    mao_do_jogador = mao_jogador()
    mao_da_mesa = mao_mesa()
    nova_carta = []
    inicie_da_carta = 0
    total_jogador = calculo_total(mao_do_jogador)
    print(f'Sua mao é {mao_do_jogador} com o total de {total_jogador}')
    print(f'A mao da mesa é {mao_da_mesa[0]}')

    if total_jogador < 21:
        if devecomprar == 1:
            if len(baralho_usavel) <= 5:
                reembaralhar()

            shuffle(baralho_usavel)
            nova_carta.append(baralho_usavel.pop())
            mao_do_jogador.append(nova_carta[inicie_da_carta])
            total_jogador = calculo_total(mao_do_jogador)
            print(f'Sua mao é {mao_do_jogador} e sua nova carta é {nova_carta[inicie_da_carta][0]}{nova_carta[inicie_da_carta][1]}, sua mao tem o total de {total_jogador}.')
            inicie_da_carta +=1

        elif devecomprar == 0:
            print(f'O jogador para de comprar, sua mao é {mao_do_jogador}, com o total de {total_jogador}')
            return total_jogador

    elif total_jogador > 21:
        print('Você estorou!')
        return total_jogador

    elif total_jogador == 21:
        print('BLACKJACK!')
        return total_jogador

    return total_jogador

# Definindo o calculo total das maos:
def calculo_total(mao):
    total = 0
    for i in mao:
        if i[0] > 10:
            total += 10
        elif i[0] == 1:
            if total >= 11:
                total += 1
            elif total < 11:
                total += 11
        elif i[0] <= 10:
            total += i[0]
    return total

# Defininco como a mesa compra cartas:
def mesa_compra():
    global total_mesa
    total_mesa = calculo_total(mao_da_mesa)
    parâmetro = randint(0,3) + 15
    nova_carta = []
    índicie_ca_carta = 0
    print(f'A mao da mesa é {mao_da_mesa} com o total de {total_mesa}')
    while True:
        if total_mesa < parâmetro:
            if len(baralho_usavel) <= 5:
                reembaralhar()
            shuffle(baralho_usavel)
            nova_carta.append(baralho_usavel.pop())
            mao_da_mesa.append(nova_carta[índicie_ca_carta])
            if nova_carta[índicie_ca_carta][0] > 10:
                total_mesa += 10
            elif nova_carta[índicie_ca_carta][0] <= 10:
                total_mesa += nova_carta[índicie_ca_carta][0]
            elif nova_carta[índicie_ca_carta][0] == 1:
                if total_mesa >= 11:
                    total_mesa += 1
                elif total_mesa < 11:
                    total_mesa += 11
            print(f'A mesa compra {nova_carta[índicie_ca_carta]}')
            índicie_ca_carta += 1
        elif total_mesa >= parâmetro:
            print(f'A mesa para de comprar, a sua mao é {mao_da_mesa}, com total de {total_mesa}')
            return total_mesa


# Definindo a opçao de entregar as maos depois de uma rodada:
def resetar_maos():
    global mao_do_jogador,mao_da_mesa
    mao_do_jogador.clear()
    mao_da_mesa.clear()

#Retorna as mao, tanto do jogador, quanto da mesa para ser usado no arquivo "main"
def get_total_maos():
    t1 = calculo_total(mao_da_mesa)
    t2 = calculo_total(mao_do_jogador)
    return (t1, t2)

# A chamada do jogo:
criar_baralho()
mao_jogador()
mao_mesa()
