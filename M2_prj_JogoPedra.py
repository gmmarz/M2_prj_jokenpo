import random

def jogar_pc()-> str:
    lst_opcoes = ['pedra','papel','tesoura']
    return random.choice(lst_opcoes)

def pegar_opcao_usuario()-> str:
    jogador_opcao = ''
    while True:
        try:
            op_num = int(input('Digite uma das opções:(1)Pedra (2)Papel (3)Tesoura:'))
            match op_num:
                case 1:
                   jogador_opcao = 'pedra'
                   break
                case 2:
                   jogador_opcao = 'papel'
                   break
                case 3:
                    jogador_opcao = 'tesoura'
                    break
                case _:
                   print('Digite apenas uma das opções indicadas')
        except ValueError:
            print('Digite apenas uma das opções indicadas')
    return jogador_opcao
        
        
def definir_ganhador(jogador_op:str,pc_op:str)->str:
    
    resultado = ''
    
    regra = {'pedra': 'tesoura',
             'tesoura':'papel',
             'papel':'pedra'
            }

    if jogador_op == pc_op:
        resultado = 'empate'
    elif regra[jogador_op] == pc_op:
        resultado = 'jogador'
    else:
        resultado = 'computador'
    return resultado


print('JOGO DO JOKENPO')
print('-'*30)

placar = {'partidas':1,'jogador':0,'computador':0,'empates':0}

while True:
    flg_partida = input(f'{placar["partidas"]}º partida, deseja iniciar: (s)sim, (n) não: ').lower()
    if flg_partida == 's':
        op_oc = jogar_pc()
        jogador =  pegar_opcao_usuario()
        ganhador = definir_ganhador(jogador,op_oc)
        
        match ganhador:
            case 'jogador':
                print(f'\nVocê jogou: {jogador}, computador jogou: {op_oc}, !!você ganhou!!')
                placar['jogador'] += 1
            case 'empate':
                print(f'\nVocê jogou: {jogador} o computador jogou: {op_oc}, !!empatou!!')
                placar['empates'] += 1
            case 'computador':
                print(f'\nVocê jogou: {jogador} o computador jogou: {op_oc}, !!Vc perdeu!!')
                placar['computador'] += 1
        placar['partidas'] += 1
        print('-'*30)        
    elif flg_partida == 'n':
        placar['partidas'] -= 1
        break
    else:
        print('Favor digitar apenas uma das opções')

print('-'*30)
print('Jogo finalizado')
print(f'Quantidade de partidas {placar["partidas"]}\
      \nPontos do jogador foram: {placar["jogador"]}\
      \nPontos do computador foram: {placar["computador"]}\
      \nQuantidade de empates:{placar["empates"]}')


    
    