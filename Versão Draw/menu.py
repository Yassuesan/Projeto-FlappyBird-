# menu.py (draw version)
import pygame
import sys
from music import MusicaFundo
from assets import load_assets
from base import Chao
from bird import Passaro
from utils import desenhar_tela
from settings import TELA_LARGURA, TELA_ALTURA, FPS
import time

def contagem_regressiva(tela, assets):
    for i in range(3, 0, -1):
        tela.fill((135,206,235))
        texto = assets['FONTE_PONTOS'].render(str(i), True, (255, 255, 255))
        tela.blit(texto, (TELA_LARGURA // 2 - texto.get_width() // 2, TELA_ALTURA // 2 - texto.get_height() // 2))
        pygame.display.update()
        time.sleep(1)

def menu_inicial():
    pygame.display.set_caption('Flappy Bird (draw)')
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))

    assets = load_assets()
    musica = MusicaFundo(assets.get('MUSICA_FUNDO'))
    musica.tocar()

    chao = Chao(730, assets['IMAGEM_CHAO'])
    passaro = Passaro(230, 350, imagens=assets['IMAGENS_PASSARO'])
    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        relogio.tick(FPS)
        chao.mover()
        passaro.mover()

        tela.fill((135,206,235))
        passaro.desenhar(tela)
        chao.desenhar(tela)

        titulo = assets['FONTE_PONTOS'].render("Flappy Bird", True, (255, 255, 255))
        instrucao = pygame.font.SysFont('arial', 30).render("Pressione ESPAÇO para jogar", True, (255, 255, 255))
        sair = pygame.font.SysFont('arial', 25).render("Pressione ESC para sair", True, (255, 255, 255))

        tela.blit(titulo, (TELA_LARGURA // 2 - titulo.get_width() // 2, 150))
        tela.blit(instrucao, (TELA_LARGURA // 2 - instrucao.get_width() // 2, 350))
        tela.blit(sair, (TELA_LARGURA // 2 - sair.get_width() // 2, 400))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                musica.parar()
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    musica.pause()
                    contagem_regressiva(tela, assets)
                    from game import main
                    main(assets, musica)
                    rodando = False
                elif evento.key == pygame.K_ESCAPE:
                    musica.parar()
                    pygame.quit()
                    sys.exit()
