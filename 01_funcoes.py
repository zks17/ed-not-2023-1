"""
    Função para calcular o ìndice de massa corpórea de uma pessoa,
    dados o seu peso e sua altura.
"""

def imc(peso, altura):
    # Peso, dividido pela altura, ao quadrado.
    return peso / altura ** 2

resultado = imc(65, 1.78)
print (resultado)

from math import pi

def area(base, altura, tipo):
    if tipo == "R":    # Retângulo
        return base * altura
    elif tipo == "T":  # Triângulo
        return base * altura / 2
    elif tipo == "E":  # Elipse
        return ( base / 2 ) * ( altura/ 2 ) * pi
    else:
        return None

    print('')