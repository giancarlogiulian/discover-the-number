import random

numero_aleatorio = random.randint(1, 100)
numero_digitado = int(0)

while (True):

    numero_digitado = int(input("Digite um número: "))

    while True:

        if numero_digitado > numero_aleatorio:
            print(f"O número {numero_digitado} é MAIOR que o número aleatório. Tente novamente!")
            break

        elif numero_digitado < numero_aleatorio:
            print(f"O número {numero_digitado} é MENOR que o número aleatório. Tente novamente!")
            break

        else :
            print(f"Parabéns, o número digitado é igual ao número aleatório {numero_aleatorio}")
            break