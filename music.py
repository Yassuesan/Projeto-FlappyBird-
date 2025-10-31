# music.py
import pygame

class MusicaFundo:
    def __init__(self, arquivo, volume=0.3, loop=True):
        self.arquivo = arquivo
        self.volume = volume
        self.loop = loop
        self._carregada = False

    def carregar(self):
        try:
            pygame.mixer.music.load(self.arquivo)
            pygame.mixer.music.set_volume(self.volume)
            self._carregada = True
        except Exception as e:
            print(f"Aviso: não foi possível carregar música: {e}")

    def tocar(self):
        if not self._carregada:
            self.carregar()
        if self._carregada:
            pygame.mixer.music.play(-1 if self.loop else 0)

    def parar(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def alterar_volume(self, novo_volume):
        self.volume = novo_volume
        pygame.mixer.music.set_volume(novo_volume)
