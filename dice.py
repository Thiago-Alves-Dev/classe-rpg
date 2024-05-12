"""_summary_

    Este código é uma implementação de um lançador de dados
    para diferentes tipos de dados comuns em jogos de RPG.

    Returns:
        _type_: _description_
    """

from random import choice


class Dado:
    """
    Classe para lançar diferentes tipos de dados comuns em jogos de RPG.
    """

    def d4():
        return choice(range(1, 5))

    def d6():
        return choice(range(1, 7))

    def d8():
        return choice(range(1, 9))

    def d10():
        return choice(range(1, 11))

    def d12():
        return choice(range(1, 13))

    def d14():
        return choice(range(1, 15))

    def d16():
        return choice(range(1, 17))

    def d20():
        return choice(range(1, 21))

    def d100():
        return choice(range(1, 101))


def _test():
    """
    Função de teste para verificar se os métodos da classe
    Dado funcionam corretamente.
    """
    print(Dado.d4())
    print(Dado.d6())
    print(Dado.d8())
    print(Dado.d10())
    print(Dado.d12())
    print(Dado.d14())
    print(Dado.d16())
    print(Dado.d20())
    print(Dado.d100())


if __name__ == '__main__':
    _test()
