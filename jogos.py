# MAIN DOS JOGOS
# Criado por Red Man

import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("* Bem vindo aos Jogos em Python! *")
    print("***** Escolha o seu jogo!  ******")
    print("*********************************")

    print("(1)FORCA (2)ADVINHAÇÃO")

    jogo = int(input("Qual jogo será escolhido?"))

    if(jogo == 1):
        print("Jogando FORCA")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando ADIVINHAÇÃO")
        adivinhacao.jogar()

    print("  ***   END GAME   ***  ")

if(__name__ == "__main__"):
    escolhe_jogo()