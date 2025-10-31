# 🐦 Flappy Bird (Python + Pygame)

Um remake do clássico **Flappy Bird**, desenvolvido em **Python** com **Pygame**, totalmente **modularizado em classes** e pronto para estudos ou melhorias.

---

## 🚀 Funcionalidades
- Estrutura de código orientada a objetos.  
- Menu inicial e tela de game over.  
- Colisão com canos e chão.  
- Sistema de pontuação.  
- Sons e imagens personalizáveis.  
- Versão alternativa *draw* (sem dependência de imagens).  

---

## 🧩 Estrutura do Projeto

```
flappybird/
│
├── main.py           # Arquivo principal - inicializa o jogo
├── game.py           # Loop principal do jogo
├── menu.py           # Menu inicial e tela de game over
├── bird.py           # Classe Bird (controle do jogador)
├── pipe.py           # Classe Pipe (cano)
├── base.py           # Classe Base (chão)
├── assets.py         # Carregamento dos sprites e sons
├── music.py          # Controle de sons e música
├── settings.py       # Configurações globais (FPS, telas, cores)
├── utils.py          # Funções auxiliares (colisão, pontuação)
└── README.md         # Este arquivo
```

---

## ⚙️ Requisitos

- Python 3.8 ou superior  
- Biblioteca `pygame`

Instale as dependências com:

```bash
pip install pygame
```

---

## ▶️ Como Executar

No terminal do VS Code ou prompt de comando, dentro da pasta do projeto:

```bash
python main.py
```

Caso o terminal abra fora da pasta correta, use:
```bash
cd caminho/para/flappybird
```

---

## 🎨 Versões Disponíveis

- **Versão Original:** utiliza imagens e sons externos (`imgs/`, `sons/`).  
- **Versão Draw:** usa apenas `pygame.draw` — não depende de arquivos externos.

Para alternar entre versões, substitua os arquivos `.py` conforme o pacote desejado.

---

## 🧠 Personalizações

Você pode ajustar facilmente:
- FPS (em `settings.py`)
- Teclas de controle (em `bird.py`)
- Volume (em `music.py`)
- Cores e tamanhos (em `assets.py`)

---

## 📚 Créditos

Desenvolvido por **Charles** com base em exercícios de programação python na hashtag treinamentos sendo uma adaptação educacional do clássico *Flappy Bird*. 

---

## 🐍 Licença

Este projeto é livre para fins educacionais.  
Você pode modificá-lo, redistribuí-lo e aprimorá-lo com os devidos créditos.
