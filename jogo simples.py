import pygame
import random

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
largura_janela = 500
altura_janela = 500
janela = pygame.display.set_mode((largura_janela, altura_janela))

# Defina o título da janela
pygame.display.set_caption("Jogo Simples em Python")

# Defina as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Defina as dimensões do jogador
tamanho_jogador = 50

# Defina a posição do jogador
x_jogador = largura_janela / 2
y_jogador = altura_janela - tamanho_jogador

# Defina a velocidade do jogador
velocidade_jogador = 10

# Defina a posição dos inimigos
x_inimigo = random.randint(0, largura_janela - tamanho_jogador)
y_inimigo = -tamanho_jogador

# Defina a velocidade dos inimigos
velocidade_inimigo = 5

# Defina a fonte para a pontuação
fonte = pygame.font.SysFont(None, 25)

# Defina a pontuação inicial
pontuacao = 0

# Defina o loop principal do jogo
while True:
    # Lide com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Lide com as teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and x_jogador > 0:
        x_jogador -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and x_jogador < largura_janela - tamanho_jogador:
        x_jogador += velocidade_jogador

    # Atualize a posição do inimigo
    y_inimigo += velocidade_inimigo

    # Verifique se o jogador colidiu com o inimigo
    if y_inimigo > altura_janela:
        x_inimigo = random.randint(0, largura_janela - tamanho_jogador)
        y_inimigo = -tamanho_jogador
        pontuacao += 1
        velocidade_inimigo += 1
    elif y_inimigo + tamanho_jogador > y_jogador and x_inimigo + tamanho_jogador > x_jogador and x_inimigo < x_jogador + tamanho_jogador:
        pygame.quit()
        quit()

    # Desenhe o jogador
    janela.fill(branco)
    pygame.draw.rect(janela, preto, [x_jogador, y_jogador, tamanho_jogador, tamanho_jogador])

    # Desenhe o inimigo
    pygame.draw.rect(janela, vermelho, [x_inimigo, y_inimigo, tamanho_jogador, tamanho_jogador])

    # Desenhe a pontuação
    texto_pontuacao = fonte.render("Pontuação: " + str(pontuacao), True, preto)
    janela.blit(texto_pontuacao, [10, 10])

    # Atualize a tela
    pygame.display.update()
