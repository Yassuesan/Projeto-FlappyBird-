# assets.py (draw version) - creates simple surfaces and no sounds
import pygame

def load_assets():
    assets = {}
    # Create simple surfaces to mimic images (sizes inspired by typical assets)
    assets['IMAGEM_CANO'] = pygame.Surface((80, 500), pygame.SRCALPHA)
    assets['IMAGEM_CANO'].fill((34, 139, 34))  # green

    assets['IMAGEM_CHAO'] = pygame.Surface((500, 100))
    assets['IMAGEM_CHAO'].fill((160, 82, 45))  # brown

    assets['IMAGEM_BACKGROUND'] = pygame.Surface((500, 800))
    assets['IMAGEM_BACKGROUND'].fill((135, 206, 235))  # sky color

    # Bird frames: small colored circles on transparent surfaces
    frames = []
    for color in [(255, 255, 0), (255, 200, 0), (255, 150, 0)]:
        s = pygame.Surface((34, 24), pygame.SRCALPHA)
        pygame.draw.ellipse(s, color, s.get_rect())
        frames.append(s)
    assets['IMAGENS_PASSARO'] = frames

    # No sounds in draw version
    assets['SOM_ASA'] = None
    assets['SOM_PONTO'] = None
    assets['SOM_COLISAO'] = None
    assets['MUSICA_FUNDO'] = None

    pygame.font.init()
    assets['FONTE_PONTOS'] = pygame.font.SysFont('arial', 50)
    return assets
