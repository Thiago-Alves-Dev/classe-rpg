from player import Player


class Potions(Player):
    """
    Classe que representa poções em um jogo de RPG.
    Herda da classe Player.
    """
    def __init__(
        self, nome='Link', nivel=0, vida_base=80, vida=80, exp=0, atack=10, defesa=8
    ) -> None:
        super().__init__(nome, nivel, vida_base, vida, exp, atack, defesa)
        """
        Inicializa um objeto Potions com os atributos padrão ou personalizados.
        """


class Cure(Potions):
    """
    Classe que representa uma poção de cura em um jogo de RPG.
    Herda da classe Potions.

    Methods:
        curar(player): Cura o jogador passado como argumento.
    """
    def curar(self, player):
        """
        Cura o jogador passado como argumento.

        Args:
            player (Player): O jogador a ser curado.
        """
        player.vida += 30  # Aumenta a vida do jogador em 30 pontos
        if player.vida > player.vida_base:  # Verifica se a vida excede o máximo possível
            player.vida = player.vida_base  # Define a vida para o máximo permitido
        print('vida curada')


def _test():
    """
    Função de teste para verificar a funcionalidade da classe Cure.
    """
    p1 = Player()
    pocao_de_cura_pequena = Cure()
    p1.vida = 70
    print(f'vida anterior: {p1.vida}')
    pocao_de_cura_pequena.curar(p1)
    print(f'vida atual: {p1.vida}')


if __name__ == '__main__':
    _test()
