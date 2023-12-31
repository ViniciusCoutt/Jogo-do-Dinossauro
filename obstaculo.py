from status import Status
from tupy import BaseImage
import random
from animacao import Animacao, Frame

class Obstaculo(BaseImage):
    """
        Classe que base dos obstáculos
    """
    posicao_inicial_x: int = 920
    posicao_inicial_y: int = 440
    
    def __init__(self, deve_spawnar = False) -> None:
        self._x: int = Obstaculo.posicao_inicial_x
        self._y: int = Obstaculo.posicao_inicial_y
        self.velocidade = 20
        self.deve_spawnar: bool = deve_spawnar

    def reset(self) -> None:
        self._hide()
    
    def update(self) -> None:
        if (Status.executando):
            if (self.deve_spawnar):
                self._x -= self.velocidade
                if (self._x <= -50):
                    self._destroy()

class Passaro(Obstaculo):
    """
        Subclasse obstáculo de tipo Passaro
    """
    posicoes=[330,460,370]
    def __init__(self) -> None:
        super().__init__(True)
        self._y: int = random.choice(Passaro.posicoes)
        self._animacao: Animacao = Animacao(2)
        self._file: str = self._animacao.definir_frame(Frame.Passaro)
    
    def update(self) -> None:
        self._file = self._animacao.definir_frame(Frame.Passaro)
        super().update()

class Cacto(Obstaculo):
    """
        Subclasse obstáculo de tipo Cacto
    """    
    def __init__(self) -> None:
        super().__init__(True)
        self._file = random.choice(Frame.Cacto)
