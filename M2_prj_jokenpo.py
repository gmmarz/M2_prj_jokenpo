#Aluno - Guilherme
#Neste projeto você desenvolverá o jogo pedra, papel e tesoura.
# Os jogadores serão o usuário e o computador.
# O jogo deve iniciar pedindo ao usuário para escolher entre "pedra", "papel"ou "tesoura" e então o computador irá fazer a escolha aleatoriamente,após isso,
# o jogo deve informar quem venceu.
# Para recordar:

# Pedra > tesoura
# Tesoura > Papel
# Papel > Pedra

# Utilize funções para separar cada funcionalidade do jogo!
# Dica : Utilize a função
# random.choice(lista)
# do pacote
# random
# pararealizar a escolha do computador.

import random

def pegar_jogada_pc() -> str:
    lst_opcoes = ['pedra','papel','tesoura']
    return random.choice(lst_opcoes)

def pegar_jogada_humano() -> str:
    jogada = 0
    jogada_str = ''
    while True:
        print('Digite uma das opções para sua jogada:\n1:pedra\n2:tesoura\n3:papel ')
        try:
            jogada = int(input('Digite uma das opções: '))
            match jogada:
                case 1:
                    jogada_str = 'pedra'
                    break
                case 2:
                    jogada_str = 'tesoura'
                    break
                case 3:
                    jogada_str = 'papel'
                    break
                case _:
                    print('Por favor digite apenas uma das opções')
        except ValueError:
            print('Por favor digite apenas uma das opções.')
    return jogada_str

def verificar_vencedor(jogador:str,pc:str)->str:
    regras = {
            'pedra':'tesoura',
            'papel':'pedra',
            'tesoura':'papel'
        }
    resultado = ''
    if jogador == pc:
        resultado = 'Empate'
    elif regras[jogador] == pc:
        resultado = 'Jogador'
    else:
        resultado = 'pc'
    return resultado

print('-'*30)
print('Jokenpo')
i = 1
placar = {'partidas':1,'jogador':0,'computador':0,'empates':0}

while True:
    print('-'*30)
    print(f'{i}º Partida')
    flg_jogada = input('Começar partida (s)sim n(não)? ').lower()
    if flg_jogada == 's':
        i += 1
        placar['partidas'] += 1
        jogador = pegar_jogada_humano()
        pc_jogada = pegar_jogada_pc()
        ganhador = verificar_vencedor(jogador,pc_jogada)

        match ganhador:
            case 'Empate':
                print(f'Houve um empate, Sua escolha: {jogador}, escolha do computador: {pc_jogada} ')
                placar['empates'] += 1
            case 'Jogador':
                print(f'Você ganhou, Sua escolha: {jogador}, escolha do computador: {pc_jogada} ')
                placar['jogador'] +=1
            case 'pc':
                print(f'você perdeu, Sua escolha: {jogador}, escolha do computador: {pc_jogada} ')
                placar['computador'] +=1
    elif flg_jogada == 'n':
        break
    else:
        print('Digite apenas uma das opções')
print('-'*30)
print('Jogo finalizado')
print('Placar final')
print(f"Em um total de: {placar['partidas'] }partidas o placar foi:\nJogador: {placar['jogador']}, computador: {placar['computador']}, empates: {placar['empates']} ")
    


