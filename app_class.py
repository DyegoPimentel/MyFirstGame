from typing import List

import pygame, sys
from settings import *

pygame.init()

pygame.display.set_caption("Pac Runner") #Titulo da tela
favicon = pygame.image.load("img/favicon.png") # Favicon
pygame.display.set_icon(favicon) # Favicon

logo_pac = pygame.image.load('img/Logo_pac_runner.png') # Logo da tela inicial

# Posições para o pacman
player_posC = [WIDTH // 2 -40, 540] # posição central do pacman
player_posL = [WIDTH // 2 -146, 540] # posição a esquerda do pacman
player_posR = [WIDTH // 2 +66, 540] # posição a direita do pacman
player_pac = [WIDTH // 2 -40, 540]

# Configurações das moedas
pos_I = 80 # posição inicial da moeda no eixo Y
pos_F = 540 # posição final da moeda no eixo Y
pos_y = pos_I
pos_x = WIDTH//2 # posição da moeda do eixo X
velocidade_y = 10


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # variavel e tamanho da tela
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.player_pac = player_pac
        self.load()


    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)



        pygame.quit()
        sys.exit()





#### HELPER FUNCTIONS ####
    def draw_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        pos[0] = pos[0]-text_size[0]//2
        pos[0] = pos[0]-text_size[1]//2
        screen.blit(text, pos)




    def load(self):
        self.background = pygame.image.load('img/fundo.png')
        self.background = pygame.transform.scale(self.background, (WIDTH,HEIGHT))
        self.pacman = pygame.image.load('img/Pac2.png')
        self.pacman = pygame.transform.scale(self.pacman, (80, 80))
        self.pause_off = pygame.image.load('img/btn_pause_off.png')
        #self.pause_on = pygame.image.load('img/btn_pause_on.png')
        self.btn_exit = pygame.image.load('img/btn_exit.png')





#### INTRO FUNCTIONS ####

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # No menu inicial "start" ao abertar a barra de espaço, inicia o jogo indo para a tela "playing".
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('MAIOR PONTUAÇÃO', self.screen, [WIDTH // 2 + 10, 10], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)
        # Melhor pontuação do jogo, precisa criar o contador
        self.draw_text('199.999', self.screen, [WIDTH // 2 + 10, 30], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)

        self.screen.blit(logo_pac, [75, HEIGHT//2-50])

        self.draw_text('PARA INICIAR APERTE ESPAÇO', self.screen, [WIDTH//2+10, 580], START_TEXT_SIZE,
                       (210, 150, 20), START_FONT)

        pygame.display.update()



#### PLAYING FUNCTIONS ####

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

             # No jogo ao apertar ESC, retorna para o menu inicial "start"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.state = 'start'

# Movimentação do Pacman.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if self.player_pac == player_posC:
                    self.player_pac = player_posR
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if self.player_pac == player_posC:
                    self.player_pac = player_posL
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if self.player_pac == player_posR:
                    self.player_pac = player_posC
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if self.player_pac == player_posL:
                    self.player_pac = player_posC

            #if (pos_y <= 540):
               # pos_y = 80

            #pos_y += velocidade_y



    def playing_update(self):
               pass

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background,(0,0)) # Aqui representa as barras laterais do fundo.
        self.draw_text('PONTOS', self.screen, [WIDTH // 2 + 10, 10], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)
        # Melhor pontuação do jogo, precisa criar o contador
        self.draw_text('0', self.screen, [WIDTH // 2 + 10, 30], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)

        self.screen.blit(self.pacman, self.player_pac)  # Aqui representa o pacman.

        self.screen.blit(self.pause_off, (15,15)) # Aqui representa o botão pause, mas ainda não esta ativado.
        self.screen.blit(self.btn_exit, (320, 15))  # Aqui representa o botão pause, mas ainda não esta ativado.

        # Moedas
        #pos_y += velocidade_y
        pygame.draw.circle(self.screen, YELLOW, (pos_x, pos_y), 7)



        pygame.display.update()

