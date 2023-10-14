import pygame
from sys import exit
from random import randint, choice

# Inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

# Define o Titulo da Janela
pygame.display.set_caption("Zombie2.0")

# Carrega o plano de fundo
plano_fundo = pygame.image.load('assets/10.png').convert()

# Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)

# Carrega as imagens do personagem
jogador_index = 0
jogador_parado = []

zumbi_index = 0
zumbi_andando = []

# Carrega o jogador parado
img = pygame.image.load('assets/jogador_atirando.png').convert_alpha()
jogador_parado.append(img)
jogador_retangulo = jogador_parado[jogador_index].get_rect( center = (480,470))

# Carrega o Projetil
projetil_superficies = []
projetil_index = 0
img = pygame.image.load('assets/projetil.png').convert_alpha()
projetil_superficies.append(img)

projetil_retangulo = projetil_superficies[projetil_index].get_rect(center = (550, 500))

# Controla se o personagem está andando (negativo esquerda, positivo direita)
direcao_personagem = 1
movimento_projetil = 0

#LOOP DO JOGO
while True:
    # EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()  

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                direcao_personagem = 1

            if evento.key == pygame.K_LEFT:
                direcao_personagem = -1


        if direcao_personagem == 1:
            jogador = pygame.transform.flip(jogador_parado[int(jogador_index)], True, False)
        else:
            jogador = jogador_parado[int(jogador_index)]
        

    # Desenha o fundo na tela
    tela.blit(plano_fundo, (0, 0))
    tela.blit(jogador, jogador_retangulo)
    tela.blit(projetil_superficies[projetil_index], projetil_retangulo)


    relogio = pygame.time.Clock()
    # Atualiza a tela com o conteudo
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)