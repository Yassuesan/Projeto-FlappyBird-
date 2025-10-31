# game.py (draw version)
import pygame
import sys
from base import Chao
from bird import Passaro
from pipe import Cano
from utils import desenhar_tela
from settings import TELA_LARGURA, TELA_ALTURA, FPS

def game_over(tela, pontos, assets, musica):
    texto_game_over = assets['FONTE_PONTOS'].render("Game Over", True, (255, 0, 0))
    texto_pontos = pygame.font.SysFont('arial', 35).render(f"Pontuação: {pontos}", True, (255, 255, 255))
    texto_instrucao = pygame.font.SysFont('arial', 25).render("Pressione ESPAÇO para voltar ao menu", True, (255, 255, 255))

    tela.blit(texto_game_over, (TELA_LARGURA // 2 - texto_game_over.get_width() // 2, 300))
    tela.blit(texto_pontos, (TELA_LARGURA // 2 - texto_pontos.get_width() // 2, 360))
    tela.blit(texto_instrucao, (TELA_LARGURA // 2 - texto_instrucao.get_width() // 2, 420))
    pygame.display.update()

    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                musica.parar()
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    musica.pause()
                    from menu import menu_inicial
                    menu_inicial()
                    aguardando = False

def main(assets, musica):
    passaros = [Passaro(230, 350, imagens=assets['IMAGENS_PASSARO'])]
    chao = Chao(730, assets['IMAGEM_CHAO'])
    canos = [Cano(700, assets['IMAGEM_CANO'])]
    tela = pygame.display.get_surface() or pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()
    musica.tocar()

    rodando = True
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                musica.parar()
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    game_over(tela, pontos, assets, musica)
                    return
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600, assets['IMAGEM_CANO']))
        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                game_over(tela, pontos, assets, musica)
                return

        desenhar_tela(tela, passaros, canos, chao, pontos, assets)
