import random
import os
import time

#Escolhendo os jogos
def intro_game():
    print(f'''
    Olá, bem vindo ao painel de games!
    
    Selecione as opções de jogo que deseja: 
    [1] - Jogo da adivinhação
    [2] - Jogo de impar ou par{os.linesep}''')
    
    global select
    select = int(input('Informe qual jogo deseja: '))
    return select

#Selecionando a opção de alcance dos números 
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
        
        Insira como deseja tentar:{os.linesep}
        [1] - Do número 1 até o 20
        [2] - Do número 1 até o número 50
        [3] - Do número 1 até o número 99
        [4] - Personalizar{os.linesep}''')
    global cond
    cond = int(input('Selecione o valor listado acima: '))

#Colocando as condições de números
def nivelamento():
    global valor1
    global valor2
    if cond == 1:
        valor1 = 1
        valor2 = 20
    elif cond == 2:
        valor1 = 1
        valor2 = 50
    elif cond == 3:
        valor1 = 1
        valor2 = 99
    elif cond == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
    Para personalizar o resultado, precisa seguir os seguintes passos:
    Precisa decidir o primeiro valor e o segundo valor!
    E automaticamente será sorteado um valor entre os dois extremos
    Lembrando que o primeiro valor deve ser menor que o segundo.
        ''')
        valor1 = int(input('Informe o 1º valor: '))
        valor2 = int(input('Informe o 2º valor: '))
    global nivel
    nivel = random.randint(valor1, valor2)
    return valor1, valor2

#Criando uma função para tentativas
def tentativas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Os números sorteados serão entre os valores {valor1} e {valor2}')
    global qtd_tentativas
    qtd_tentativas = int(input('Quando tentativas você deseja ter? '))
    cont = 1
    for x in range(1, qtd_tentativas+1):
        user = int(input('Informe o número que você acha que seja: '))
        if user == nivel:
            print('Parabéns, você acertou! O número sorteado foi ', nivel)
            break
        elif user < nivel:
            print('Errou, o valor inserido é maior do que o número sorteado!')
            time.sleep(1.75)
        elif user > nivel:
            print('Errou, o valor inserido é menor do que o número sorteado!')
            time.sleep(1.75)          
        print('Tentativa número', cont)
        time.sleep(1.75)
        os.system('cls' if os.name == 'nt' else 'clear')
        cont += 1
        if cont == qtd_tentativas+1:
            print(f'Você errou e acabou as tentativas! O valor sorteadora era {nivel} {os.linesep}')
            time.sleep(2)
            quest = str(input('Deseja tentar novamente? [SIM / NÃO]: '))
            while quest == "SIM":
                os.system('cls' if os.name == 'nt' else 'clear')
                intro_game()
            else:
                print('Obrigado por jogar!')
                time.sleep(2)
                break

#Jogo de impar ou par
def impar_par():
    
    print('''
    Jogo de impar ou par!
    
    Será sorteado um número entre 1 a 100 e você deve adivinhar se o número sortado é impar ou par!
    Simples assim
    
    Vamos lá!''')
    
    global select_imp_par
    select_imp_par = str(input('Você acha que o valor é impar ou par? '))
    select_imp_par = select_imp_par.upper()
    nivel_imp_par = random.randint(0, 101)
    resultado_impar_par = nivel_imp_par % 2
    
    if resultado_impar_par == 0 and select_imp_par == 'PAR':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Analisando ...')
        time.sleep(1.75)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Parabéns, você acertou !!! O valor sorteado foi', nivel_imp_par)
        
    elif resultado_impar_par == 1 and select_imp_par == 'IMPAR':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Analisando ...')
        time.sleep(1.75)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Parabéns, você acertou !!! O valor sorteado foi', nivel_imp_par)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Analisando ...')
        time.sleep(1.75)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Uma pena, você errou ! O valor sorteado foi', nivel_imp_par)
intro_game()

if select == 1:
    intro()
    nivelamento()
    tentativas()
else:
    impar_par() 
        
        