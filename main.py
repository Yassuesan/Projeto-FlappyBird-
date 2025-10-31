# main.py
# Ponto de entrada do jogo
import pygame
import sys
from menu import menu_inicial
from settings import TELA_LARGURA, TELA_ALTURA

if __name__ == "__main__":
    pygame.init()
    try:
        pygame.mixer.init()
    except Exception:
        pass

    pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    menu_inicial()
    pygame.quit()
    sys.exit()
