import random

def play_game():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação! Estou pensando em um número entre 1 e 100.")

    while True:
        numero = int(input("Digite seu palpite: "))
        tentativas += 1

        if numero < numero_secreto:
            print("Tente um número maior!")
        elif numero > numero_secreto:
            print("Tente um número menor!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

play_game()