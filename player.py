"""
Este script implementa classes para representar jogadores e inimigos em um jogo de RPG,
juntamente com uma função de teste para simular um encontro entre eles.

"""

from dice import Dado
import main_name
from random import choice


class Player():
    """
    Classe que representa um jogador em um jogo de RPG.
    """

    def __init__(
        self, nome='Link', nivel=0, vida_base=80, vida=80, exp=0, atack=10, defesa=8
    ) -> None:
        """
        Inicializa um objeto Player com os atributos padrão ou personalizados.

        Args:
            nome (str): O nome do jogador. Padrão é 'Link'.
            nivel (int): O nível do jogador. Padrão é 0.
            vida_base (int): A quantidade de pontos de vida base do jogador. Padrão é 80
            vida (int): A quantidade de pontos de vida do jogador. Padrão é 80.
            exp (int): A quantidade de pontos de experiência do jogador. Padrão é 0.
            atack (int): O valor do ataque do jogador. Padrão é 10.
            defesa (int): O valor da defesa do jogador. Padrão é 8.
        """

        self.nome = nome
        self.nivel = nivel
        self.vida_base = vida_base
        self.vida = vida
        self.exp = exp
        self.atack = atack
        self.defesa = defesa

    def show_all(self):
        """
        Mostra todos os atributos do jogador.
        """

        print(
            '-' * 30, '\n'
            f'nome: {self.nome} \n'
            f'nível: {self.nivel} \n'
            f'vida: {self.vida} \n'
            f'exp: {self.exp} \n'
            f'ataque: {self.atack} \n'
            f'defesa: {self.defesa}'
        )

    def atacar(self, alvo):
        """
        Realiza um ataque ao alvo especificado.

        Args:
            alvo (Player): O jogador alvo a ser atacado.
        """

        roll = Dado.d10()
        print(f'rolagem: {roll}')
        if roll > 5:
            dano = choice(range(15, 21))
        else:
            dano = choice(range(10, 16))
        alvo.vida = max(0, alvo.vida - dano)
        print(f'ataque: {dano}')


class Enimie(Player):
    """
    Classe que representa um inimigo em um jogo de RPG.
    """

    def __init__(
        self,
        nome=choice(main_name.enimies_name),
        nivel=choice(range(1, 6)),
        vida_base=None,
        vida=choice(range(20, 61)),
        exp=choice(range(1, 11)),
        atack=choice(range(10, 21)),
        defesa=choice(range(5, 9))
    ) -> None:
        """
        Inicializa um objeto Enimie com atributos aleatórios.

        Args:
            nome (str): O nome do inimigo, selecionado aleatoriamente da lista de nomes de inimigos.
            nivel (int): O nível do inimigo, selecionado aleatoriamente entre 1 e 5.
            vida (int): A quantidade de pontos de vida do inimigo, selecionada aleatoriamente entre 20 e 60.
            exp (int): A quantidade de pontos de experiência que o inimigo concede ao ser derrotado, selecionada aleatoriamente entre 1 e 10.
            atack (int): O valor do ataque do inimigo, selecionado aleatoriamente entre 10 e 20.
            defesa (int): O valor da defesa do inimigo, selecionado aleatoriamente entre 5 e 8.
        """
        super().__init__(nome, nivel, vida_base, vida, exp, atack, defesa)

    def show_all(self):
        return super().show_all()

    def atacar(self, alvo):
        return super().atacar(alvo)

    def get_xp(self):
        """
        Retorna a quantidade de experiência concedida pelo inimigo ao ser derrotado.

        Returns:
            int: A quantidade de experiência do inimigo.
        """

        return self.exp


def _test():
    """
    Função de teste automatizado para simular um encontro entre um jogador e um inimigo.
    """

    p1 = Player()
    e1 = Enimie()
    e1.show_all()

    while True:
        if e1.vida <= 0:
            print('-' * 30)
            print('inimigo derrotado')
            print(f'exp obtida: {e1.get_xp()}')
            p1.exp += e1.get_xp()
            print(f'sua exp: {p1.exp}')
            print('-' * 30)
            break
        elif p1.vida <= 0:
            print('-' * 30)
            print('você morreu')
            print('-' * 30)
            break
        else:
            print('-' * 30)
            print('player atacou \n')
            p1.atacar(e1)
            print(f'vida inimigo: {e1.vida}')
            print('-' * 30, '\n')
            if e1.vida <= 0:
                continue
            print('-' * 30)
            print('inimigo atacou \n')
            e1.atacar(p1)
            print(f'vida player: {p1.vida}')
            print('-' * 30, '\n')
            if p1.vida <= 0:
                continue


if __name__ == '__main__':
    _test()
