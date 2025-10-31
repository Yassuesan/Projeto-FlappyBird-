# main.py (draw version)
import pygame
import sys
from menu import menu_inicial
from settings import TELA_LARGURA, TELA_ALTURA

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    menu_inicial()
    pygame.quit()
    sys.exit()
