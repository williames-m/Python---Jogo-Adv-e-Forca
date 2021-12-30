# JOGO DE ADIVINHAÇÃO
# Criado por Red Man

#importando biblioteca random
import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # numero_secreto = round(random.random() * 100) #Gerar numero de 0.0 a 1.0 multiplicado por 100

    numero_secreto = random.randrange(1,101) #Gerar numero de 1 a 100
    pontos = 1000
    # total_de_tentativas = 0

    print("Qual nível de dificuldade??")
    print("Nivel (1)Facil, (2)Medio, (3)Dificil:")

    nivel_str = input("Escolha o nível: ")
    nivel = int(nivel_str)

    facil   = nivel == 1
    medio   = nivel == 2
    dificil = nivel == 3

    if (facil):
        total_de_tentativas = 20
    if (medio):
        total_de_tentativas = 10
    if (dificil):
        total_de_tentativas = 5

    # rodada = 1

    # while(rodada <= total_de_tentativas): #utiliza loop while
    for rodada in range(1,total_de_tentativas +1): #utiliza loop for
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Deve digitar um numero entre 1 e 100!")
            # rodada = rodada
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto
        acabou_tentativas = rodada == total_de_tentativas

        if (acertou):
            print("*********************************")
            print("******    Você acertou!    ******")
            print("*****  Sua pontuação foi!  ******")
            print("********      {}      *********".format(pontos))
            print("*********************************")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Voce errou! O seu chute foi maior que o número secreto")
            if (acabou_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Voce errou! O seu chute foi menor que o número secreto")

        # rodada = rodada + 1

    print("  ***   END GAME   ***  ")

if(__name__ == "__main__"):
    jogar()