def soma(a, b):
    resultado = a + b
    return resultado


resultado_soma = soma(5, 3)
print(resultado_soma)


def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = 1355989
if e_par(numero):
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")
