"""
Arquivo que contém as fuções de teste do programa.
"""

from funcao import aplicacao


class TesteProjeto:
    """
    Objeto de teste.
    """

    def setup(self):
        """
        Inicializando objeto de teste
        """
        pass

    def teste_fizzbuzz(self):
        """
        Realiza o teste para múltiplo de 5 e 7 simultâneos
        """
        resultado = aplicacao(35)

        assert resultado == 'fizzbuzz'

    def teste_fizz(self):
        """
        Realiza o teste para múltiplo de 5
        """
        resultado = aplicacao(5)

        assert resultado == 'fizz'

    def teste_buzz(self):
        """
        Realiza o teste para múltiplo de 7
        """
        resultado = aplicacao(7)

        assert resultado == 'buzz'

    def teste_miss(self):
        """
        Realiza o teste para valores não múltiplos de 5 e 7
        """
        resultado = aplicacao(41)

        assert resultado == 'miss'
