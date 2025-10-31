# utils.py
import os
import sys
import pygame
from settings import TELA_LARGURA, TELA_ALTURA

def caminho_recurso(caminho_relativo):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, caminho_relativo)

def desenhar_tela(tela, passaros, canos, chao, pontos, assets):
    # --- Etapa 1
    tela.blit(assets['IMAGEM_BACKGROUND'], (0, 0))

    # --- Etapa 2
    for passaro in passaros:
        passaro.desenhar(tela)

    # --- Etapa 3
    for cano in canos:
        cano.desenhar(tela)

    # --- Etapa 4
    texto = assets['FONTE_PONTOS'].render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

    # --- Etapa 5
    chao.desenhar(tela)
    pygame.display.update()
