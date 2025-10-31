# utils.py (draw version)
import pygame
from settings import TELA_LARGURA, TELA_ALTURA

def desenhar_tela(tela, passaros, canos, chao, pontos, assets):
    # Background (solid gradient-like rectangle)
    tela.fill((135, 206, 235))  # sky blue

    # Draw pipes and birds and base
    for cano in canos:
        cano.desenhar(tela)
    for passaro in passaros:
        passaro.desenhar(tela)

    # HUD
    fonte = assets['FONTE_PONTOS']
    texto = fonte.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

    chao.desenhar(tela)
    pygame.display.update()
