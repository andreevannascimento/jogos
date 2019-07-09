from builtins import range
import random

def jogar():
    print("########################")
    print("Bem vindo no jogo de Adivinhação!")
    print("########################")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) facil (2) medio (3) dificil")

    nivel = int(input("Define o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Rodada {} de {}".format(rodada,total_de_tentativas))

        chute_str = input("Digite o seu número entre 1 e 100: ")

        print("Você digitou ",chute_str)

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve escolher um número entre 1 e 100.")
            continue

        acerto = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acerto):
            print("Você acertou! Você fez {} pontos.".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior.")
            elif(menor):
                print("Você errou! Seu chute foi menor.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()