# pipe.py (draw version)
import pygame
import random

class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x, imagem_cano):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        # imagem_cano is a surface - draw uses it as color reference
        self.CANO_BASE = imagem_cano
        self.CANO_TOPO = pygame.transform.flip(self.CANO_BASE, False, True)
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        # Draw rectangles representing pipes (using the surface color)
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        return bool(topo_ponto or base_ponto)
