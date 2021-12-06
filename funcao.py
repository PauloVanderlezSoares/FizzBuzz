"""
Módulo que contém a função solução do problema.
"""


def aplicacao(num):
    """
    Função retorna: fizz se valor de entrada for múltiplo de 5
                    buzz se valor de entrada for múltiplo de 7
                    fizzbuzz se valor de entrada for múltiplo 5 e 7
                    miss se valor de entrada não for múltiplo de 5 e 7
    """

    if num % 5 == 0 and num % 7 == 0:
        resultado = "fizzbuzz"
        return resultado

    elif num % 5 == 0:
        resultado = "fizz"
        return resultado

    elif num % 7 == 0:
        resultado = "buzz"
        return resultado

    else:
        resultado = "miss"
        return resultado
