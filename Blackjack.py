from random import *

baralho = []
baralho_usável = []

naipes = {
    0:' de Copas',
    1:' de Ouros',
    2:' de Espadas',
    3:' de Paus'
}


# Definindo a criação do baralho:
def criar_baralho():
    for i in range(0,52):
        baralho.append((i%13+1,naipes[int(i/13)]))
        baralho_usável.append((i%13+1,naipes[int(i/13)]))

# Definindo o reembaralhamento quando o baralho tiver menos de 5 cartas:
def reembaralhar():
    baralho_usável.clear()
    for i in baralho:
        baralho_usável.append(i)

# Definindo quem é o vencedor:
def vencedor():
    if total_jogador > total_mesa and total_jogador < 22 and total_mesa < 22:
        print('Você ganhou!')
    elif total_jogador > 21 and total_mesa > 21:
        print('Você e a mesa perderam!')
    elif total_jogador < 22 and total_mesa > 21:
        print('Você ganhou!')
    elif total_jogador == total_mesa and total_jogador < 22:
        print('Você empatou com a mesa!')
    elif total_mesa > total_jogador and total_mesa < 22 and total_jogador < 22:
        print('A mesa ganhou!')
    elif total_mesa < 22 and total_jogador > 21:
        print('A mesa ganhou!')

# Definindo a criação da mão do jogador:
def mão_jogador():
    global mão_do_jogador
    mão_do_jogador = []
    shuffle(baralho_usável)
    for i in range(0,2):
        mão_do_jogador.append(baralho_usável.pop())
    return mão_do_jogador

# Definindo a compra de cartas do jogador:
def comprar_carta():
    global total_jogador, total_mesa
    mão_do_jogador = mão_jogador()
    mão_da_mesa = mão_mesa()
    nova_carta = []
    inicie_da_carta = 0
    total_jogador = cálculo_total(mão_do_jogador)
    print(f'Sua mão é {mão_do_jogador} com o total de {total_jogador}')
    print(f'A mão da mesa é {mão_da_mesa[0]}')
    while True:
        if total_jogador < 21:
            devecomprar = int(input('Deseja comprar uma carta?: '))
            if devecomprar == 1:
                if len(baralho_usável) <= 5:
                    reembaralhar()
                shuffle(baralho_usável)
                nova_carta.append(baralho_usável.pop())
                mão_do_jogador.append(nova_carta[inicie_da_carta])
                total_jogador = cálculo_total(mão_do_jogador)
                print(f'Sua nova carta é {nova_carta[inicie_da_carta][0]}{nova_carta[inicie_da_carta][1]}, sua mão tem o total de {total_jogador}.')
                inicie_da_carta +=1
            elif devecomprar == 0:
                print(f'O jogador para de comprar, sua mão é {mão_do_jogador}, com o total de {total_jogador}')
                break
        elif total_jogador >= 21:
            if total_jogador > 21:
                print('Você estorou!')
                break
            elif total_jogador == 21:
                print('BLACKJACK!')
                break

# Definindo a mão da mesa:
def mão_mesa():
    global mão_da_mesa
    mão_da_mesa = []
    for i in range(0,2):
        shuffle(baralho_usável)
        mão_da_mesa.append(baralho_usável.pop())
    return mão_da_mesa

# Definindo o cálculo total das mãos:
def cálculo_total(mão):
    total = 0
    for i in mão:
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
    total_mesa = cálculo_total(mão_da_mesa)
    parâmetro = randint(0,3) + 15
    nova_carta = []
    índicie_ca_carta = 0
    print(f'A mão da mesa é {mão_da_mesa} com o total de {total_mesa}')
    while True:
        if total_mesa < parâmetro:
            if len(baralho_usável) <= 5:
                reembaralhar()
            shuffle(baralho_usável)
            nova_carta.append(baralho_usável.pop())
            mão_da_mesa.append(nova_carta[índicie_ca_carta])
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
            print(f'A mesa para de comprar, a sua mão é {mão_da_mesa}, com total de {total_mesa}')
            break

# Definindo a opção de iniciar o jogo:
def inciar_jogo():
    começar = int(input('Deseja começar a jogar BLACKJACK?: '))
    return começar

# Definindo a opção de re-jogar:
def jogarnovamente():
    resposta = int(input('Deseja jogar novamente?: '))
    return resposta

# Definindo a opção de entregar as mãos depois de uma rodada:
def resetar_mãos():
    global mão_do_jogador,mão_da_mesa
    mão_do_jogador.clear()
    mão_da_mesa.clear()

# Laço principal do jogo:
def jogo():
    contador = 1
    print(f'Você está jogando BLACKJACK!')
    while True:
        if contador == 1:
            começar = inciar_jogo()
            if começar == 1:
                contador += 1
                criar_baralho()
                comprar_carta()
                mesa_compra()
                vencedor()
                
            if começar == 0:
                break
        if contador > 1:
            novamente = jogarnovamente()
            if novamente == 1:
                resetar_mãos()
                comprar_carta()
                mesa_compra()
                vencedor()
            elif novamente == 0:
                print('Que pena...')
                break
        
# A chamada do jogo:
jogo()