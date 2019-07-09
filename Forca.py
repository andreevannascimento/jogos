import random

def msg():
    print("###########################")
    print("Bem vindo no jogo da Forca!")
    print("###########################")

def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra = palavras[numero].upper()

    return palavra

def inicializar_letras(palavra):
    return ["_" for letra in palavra]

def recebe_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(palavra,chute,letras_acertadas):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def jogar():

    msg()

    palavra = carrega_palavra()

    letras_acertadas = inicializar_letras(palavra)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0



    while(not acertou and not enforcou):

        chute = recebe_chute()

        if(chute in palavra):
            marca_chute_correto(palavra,chute,letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você acertou!")
    else:
        print("Você errou!")
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()