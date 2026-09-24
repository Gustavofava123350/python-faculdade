while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        print("O número é par!!")
    else:
        print("O número é ímpar!!")
