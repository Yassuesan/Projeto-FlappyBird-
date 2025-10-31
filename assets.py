# assets.py
import pygame
import os
from utils import caminho_recurso
from settings import PASTA_IMGS, PASTA_SONS

def load_assets():
    assets = {}
    assets['IMAGEM_CANO'] = pygame.transform.scale2x(pygame.image.load(caminho_recurso(os.path.join(PASTA_IMGS, 'pipe.png'))))
    assets['IMAGEM_CHAO'] = pygame.transform.scale2x(pygame.image.load(caminho_recurso(os.path.join(PASTA_IMGS, 'base.png'))))
    assets['IMAGEM_BACKGROUND'] = pygame.transform.scale2x(pygame.image.load(caminho_recurso(os.path.join(PASTA_IMGS, 'bg.png'))))
    assets['IMAGENS_PASSARO'] = [
        pygame.transform.scale2x(pygame.image.load(caminho_recurso(os.path.join(PASTA_IMGS, 'bird1.png')))),
        pygame.transform.scale2x(pygame.image.load(caminho_recurso(os.path.join(PASTA_IMGS, 'bird2.png')))),
        pygame.transform.scale2x(pygame.image.load(caminho_recurso(os.path.join(PASTA_IMGS, 'bird3.png')))),
    ]

    try:
        assets['SOM_ASA'] = pygame.mixer.Sound(caminho_recurso(os.path.join(PASTA_SONS, 'wing.wav')))
        assets['SOM_PONTO'] = pygame.mixer.Sound(caminho_recurso(os.path.join(PASTA_SONS, 'point.wav')))
        assets['SOM_COLISAO'] = pygame.mixer.Sound(caminho_recurso(os.path.join(PASTA_SONS, 'hit.wav')))
        assets['MUSICA_FUNDO'] = caminho_recurso(os.path.join(PASTA_SONS, 'musica_fundo.mp3'))
        assets['SOM_ASA'].set_volume(0.6)
        assets['SOM_PONTO'].set_volume(0.6)
        assets['SOM_COLISAO'].set_volume(0.7)
    except Exception as e:
        print(f"Aviso: não foi possível carregar um ou mais sons: {e}")
        assets['SOM_ASA'] = None
        assets['SOM_PONTO'] = None
        assets['SOM_COLISAO'] = None
        assets['MUSICA_FUNDO'] = None

    pygame.font.init()
    assets['FONTE_PONTOS'] = pygame.font.SysFont('arial', 50)
    return assets
