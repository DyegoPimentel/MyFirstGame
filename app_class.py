from typing import List

import pygame, sys
from settings import *
from os import path

pygame.init()

pygame.display.set_caption("Pac Runner") #Titulo da tela
favicon = pygame.image.load("img/favicon.png") # Favicon
pygame.display.set_icon(favicon) # Favicon

# IMAGENS
logo_pac = pygame.image.load('img/Logo_pac_runner.png') # Logo da tela inicial
ghost_clyde = pygame.image.load('img/clyde.png') # Imagem do fantasma laranja.
ghost_blink = pygame.image.load('img/blinky.png') # Imagem do fantasma vermelho.
ghost_pinky = pygame.image.load('img/pinky.png') # Imagem do fantasma rosa.
ghost_ink = pygame.image.load('img/inky.png')    # Imagem do fantasma azul.

# Posições para o pacman
player_posC = [WIDTH // 2 -40, 540] # posição central do pacman
player_posL = [WIDTH // 2 -146, 540] # posição a esquerda do pacman
player_posR = [WIDTH // 2 +66, 540] # posição a direita do pacman
player_pac = [WIDTH // 2 -40, 540]

# Configurações das moedas
#pos_I = 80 # posição inicial da moeda no eixo Y
#pos_F = 540 # posição final da moeda no eixo Y
pos_y_C = 80
pos_y_L = 80
pos_y_R = 80
pos_y_C1 = -150
pos_y_L1 = -150
pos_y_R1 = -150

pos_c = WIDTH//2 # posição da moeda do eixo X
pos_L = WIDTH//2 - 106 # posição da moeda do eixo X
pos_R = WIDTH//2 + 106 # posição da moeda do eixo X

#pos_gL = 0 # Posição no eixo Y dos fantasmas.
#pos_gC = 0 # Posição no eixo Y dos fantasmas.
#pos_gR = 0 # Posição no eixo Y dos fantasmas.

gcl = 0
gcc = 0
gcr = 0
gpl = 0
gpc = 0
gpr = 0
gil = 0
gic = 0
gir = 0
gbl = 0
gbc = 0
gbr = 0

velocidade_y = 3

# Pontuação do jogo
score = 0
high_score = 0

# Background do menu superior na tela playing
menu_background = pygame.Rect(0, 0, 360, 60)


class App:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # variavel e tamanho da tela
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.player_pac = player_pac
        self.load()
        self.load_data()
        self.highscore = high_score


    def load_data(self):
        # Carrega o high score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, hs_file), 'w') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        if score > self.highscore:
            self.highscore = score





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
            elif self.state == 'game_over':
                self.game_over_events()
                self.game_over_update()
                self.game_over_draw()
            else:
                self.running = False
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()





########################################## HELPER FUNCTIONS ###########################################################

    def draw_text(self, words, screen, pos, size, colour, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        pos[0] = pos[0]-text_size[0]//2
        pos[0] = pos[0]-text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        global score, pos_y

        self.background = pygame.image.load('img/fundo.png')
        self.background = pygame.transform.scale(self.background, (WIDTH,HEIGHT))
        self.pacman = pygame.image.load('img/Pac2.png')
        self.pacman = pygame.transform.scale(self.pacman, (80, 80))
        self.pause_off = pygame.image.load('img/btn_pause_off.png')
        #self.pause_on = pygame.image.load('img/btn_pause_on.png')
        self.btn_exit = pygame.image.load('img/btn_exit.png')
        self.clyde = pygame.image.load('img/clyde.png')
        self.clyde = pygame.transform.scale(self.clyde, (80, 80))
        self.blinky = pygame.image.load('img/blinky.png')
        self.blinky = pygame.transform.scale(self.blinky, (80, 80))
        self.pinky = pygame.image.load('img/pinky.png')
        self.pinky = pygame.transform.scale(self.pinky, (80, 80))
        self.inky = pygame.image.load('img/inky.png')
        self.inky = pygame.transform.scale(self.inky, (80, 80))

# Posicionamento dos fantasmas
    def ghosts(self): # LARANJADO
        global player_posL, player_posC, player_posR, gcr, gbl, gpr, gic, gcl, gbr, gir,gcc, gpl, gbc, gpc,gil

        # blink da esquerda
        self.screen.blit(self.blinky, (pos_L - 40, gbl))
        gbl += velocidade_y - 1
        if self.player_pac == player_posL and gbl > 480:
            self.state = 'game_over'
        elif gbl > 640:
            gbl = -2500

        # Pinky da direita
        self.screen.blit(self.pinky, (pos_R - 40, gpr -250))
        gpr += velocidade_y - 1
        if self.player_pac == player_posR and gpr > 730:
            self.state = 'game_over'
        elif gpr > 890:
            gpr = -2750

        # inky do meio
        self.screen.blit(self.inky, (pos_c - 40, gic - 500))
        gic += velocidade_y - 1
        if self.player_pac == player_posC and gic > 980: # gbr = 480 + primeiro gir
            self.state = 'game_over'
        elif gic > 1140:
            gic = -3000

        # clyde da esquerda duo
        self.screen.blit(self.clyde, (pos_L - 40, gcl - 750))
        gcl += velocidade_y - 1
        if self.player_pac == player_posL and gcl > 1230:
            self.state = 'game_over'
        elif gcl > 1390:
             gcl = -3250

         # blink da direita duo
        self.screen.blit(self.blinky, (pos_R - 40, gbr - 750))
        gbr += velocidade_y - 1
        if self.player_pac == player_posR and gbr > 1230:
            self.state = 'game_over'
        elif gbr > 1390:
            gbr = -3250

         # inky da direita
        self.screen.blit(self.inky, (pos_R - 40, gir - 1000))
        gir += velocidade_y - 1
        if self.player_pac == player_posR and gir > 1480: # gbr = 480 + primeiro gir
            self.state = 'game_over'
        elif gir > 1640: # gir = 640 + primeiro gir
            gir = -3500

        # Clyde do centro
        self.screen.blit(self.clyde, (pos_c - 40, gcc - 1250))
        gcc += velocidade_y - 1
        if self.player_pac == player_posC and gcc > 1730: # gcc = 480 + primeiro gcc
            self.state = 'game_over'
        elif gcc > 1890: # gcc = 640 + primeiro gcc
            gcc = -3750

        # Pinky da esquerda
        self.screen.blit(self.pinky, (pos_L - 40, gpl - 1500))
        gpl += velocidade_y - 1
        if self.player_pac == player_posL and gpl > 1980: # gpl = 480 + primeiro gpl
            self.state = 'game_over'
        elif gpl > 2140: # gpl = 640 + primeiro gpl
            gpl = -4000

        # Blinky do centro
        self.screen.blit(self.blinky, (pos_c - 40, gbc - 1750))
        gbc += velocidade_y - 1
        if self.player_pac == player_posC and gbc > 2230: # gbc = 480 + primeiro gbc
            self.state = 'game_over'
        elif gbc > 2390: # gbc = 640 + primeiro gbc
            gbc = -4250

        # Pinky do centro duo
        self.screen.blit(self.pinky, (pos_c - 40, gpc - 2000))
        gpc += velocidade_y - 1
        if self.player_pac == player_posC and gpc > 2480: # gpc = 480 + primeiro gpc
            self.state = 'game_over'
        elif gpc > 2640: # gpc = 640 + primeiro gpc
            gpc = -4500

        # Inky da esquerda duo
        self.screen.blit(self.inky, (pos_L - 40, gil - 2000))
        gil += velocidade_y - 1
        if self.player_pac == player_posL and gil > 2480: # gil = 480 + primeiro gil
            self.state = 'game_over'
        elif gil > 2640: # gil = 640 + primeiro gil
            gil = -4500

         # Clyde da esquerda
        self.screen.blit(self.clyde, (pos_R - 40, gcr - 2250))
        gcr += velocidade_y - 1
        if self.player_pac == player_posR and gcr > 2730: # gcr = 480 + primeiro gcr
            self.state = 'game_over'
        elif gcr > 2890: # gcr = 640 + primeiro gcr
            gcr = -4750








    def coin_center(self):
        global pos_y, pos_L, pos_R, pos_c, score, pos_y_C, pos_y_C1, pos_y_L,pos_y_L1, pos_y_R

        # Contador de pontos das moeda do meio.
        if self.player_pac == player_posC and pos_y_C1 >= 539 or self.player_pac == player_posC and pos_y_C >= 539:
            score += 1

        # Primeira moeda
        pygame.draw.circle(self.screen, YELLOW,(pos_c, pos_y_C), 7)
        pos_y_C += velocidade_y  # Movimentação da moeda
        if self.player_pac == player_posC and pos_y_C > 540 or pos_y_C > 640:
            pos_y_C = 80

        # Segunda moeda
        pygame.draw.circle(self.screen, YELLOW, (pos_c, pos_y_C1), 7)
        pos_y_C1 += velocidade_y  # Movimentação da moeda
        if self.player_pac == player_posC and pos_y_C1 > 540 or pos_y_C1 > 640:
            pos_y_C1 = -150

    def coin_right(self):
        global pos_y, pos_L, pos_R, pos_C, score, pos_y_C, pos_y_C1, pos_y_L,pos_y_L1, pos_y_R, pos_y_R1

        # Contador de pontos das moeda da direita.
        if self.player_pac == player_posR and pos_y_R1 >= 539 or self.player_pac == player_posR and pos_y_R >= 539:
            score += 1

        # Primeira moeda da direita.
        pygame.draw.circle(self.screen, YELLOW,(pos_R, pos_y_R), 7)
        pos_y_R += velocidade_y  # Movimentação da moeda
        if self.player_pac == player_posR and pos_y_R > 540:
            pos_y_R = - 180
        elif pos_y_R > 640:
            pos_y_R = 100

        # Segunda moeda
        pygame.draw.circle(self.screen, YELLOW, (pos_R, pos_y_R1), 7)
        pos_y_R1 += velocidade_y  # Movimentação da moeda
        if self.player_pac == player_posR and pos_y_R1 > 540:
            pos_y_R1 = -330
        elif pos_y_R1 > 640:
            pos_y_R1 = -230

    def coin_left(self):
        global pos_y, pos_L, pos_R, pos_C, score, pos_y_C, pos_y_C1, pos_y_L, pos_y_L1, pos_y_R

        # Contador de pontos das moeda da esquerda.
        if self.player_pac == player_posL and pos_y_L1 >= 539 or self.player_pac == player_posL and pos_y_L >= 539:
            score += 1

        # Primeira moeda
        pygame.draw.circle(self.screen, YELLOW, (pos_L, pos_y_L), 7)
        pos_y_L += velocidade_y  # Movimentação da moeda
        if self.player_pac == player_posL and pos_y_L > 540 or pos_y_L > 640:
            pos_y_L = 80

        # Segunda moeda
        pygame.draw.circle(self.screen, YELLOW, (pos_L, pos_y_L1), 7)
        pos_y_L1 += velocidade_y  # Movimentação da moeda
        if self.player_pac == player_posL and pos_y_L1 > 540 or pos_y_L1 > 640:
            pos_y_L1 = -150

    # Velocidade de movimento das moedas e dos fantasmas
    def velocidade(self):
        global score, velocidade_y

        if score > 5:
            velocidade_y = 4
        if score > 10:
            velocidade_y = 5
        if score > 15:
            velocidade_y = 6
        if score > 20:
            velocidade_y = 7
        if score > 30:
            velocidade_y = 8
        if score > 40:
            velocidade_y = 9
        if score > 50:
             velocidade_y = 10



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
        self.draw_text(str(self.highscore), self.screen, [WIDTH // 2 + 10, 30], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)

        self.screen.blit(logo_pac, [75, HEIGHT//2-50])

        self.draw_text('PARA INICIAR APERTE ESPAÇO', self.screen, [WIDTH//2+10, 580], START_TEXT_SIZE,
                       (210, 150, 20), START_FONT)

        pygame.display.update()



#### PLAYING FUNCTIONS ####

    def playing_events(self):
        global pos_y

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


    def playing_update(self):
               pass

    def playing_draw(self):
        global pos_y, score, velocidade_y

        self.screen.fill(BLACK)
        self.screen.blit(self.background,(0,0)) # Aqui representa as barras laterais do fundo.

        self.coin_center()  # Moedas do meio
        self.coin_left()    # Moedas da esquerda.
        self.coin_right()   # Moedas da direita.


        self.ghosts()  # Fantasmas

        pygame.draw.rect(self.screen, BLACK, menu_background) # Background do menu superior da "tela playing".

        self.draw_text('PONTOS', self.screen, [WIDTH // 2 + 10, 10], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)
        # Melhor pontuação do jogo, precisa criar o contador
        self.draw_text('{}'.format(score), self.screen, [WIDTH // 2 + 10, 30], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)

        self.screen.blit(self.pacman, self.player_pac)  # Aqui representa o pacman.

        self.screen.blit(self.pause_off, (15,15)) # Aqui representa o botão pause, mas ainda não esta ativado.
        self.screen.blit(self.btn_exit, (320, 15))  # Aqui representa o botão pause, mas ainda não esta ativado.
        self.velocidade() # Aqui faz com que as moedas e fantasmas se movimentem, o codigo referente a essa funcionalidade esta na linha 179

        pygame.display.update()

################################################# GAME OVER ############################################################

    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # No menu inicial "start" ao abertar a barra de espaço, inicia o jogo indo para a tela "playing".
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset() # Falta definir
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def game_over_update(self):
        pass

    def game_over_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('MAIOR PONTUAÇÃO', self.screen, [WIDTH // 2 + 10, 10], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)
        # Melhor pontuação do jogo, precisa criar o contador
        self.draw_text(str(self.highscore), self.screen, [WIDTH // 2 + 10, 30], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)

        self.draw_text('GAME OVER', self.screen, [WIDTH//2+10, HEIGHT//2-50], GAME_OVER_SIZE,
                       (255, 0, 0), GAME_OVER_FONT)

        self.draw_text('PARA JOGAR NOVAMENTE', self.screen, [WIDTH//2+10, 540], START_TEXT_SIZE,
                       (210, 150, 20), START_FONT)
        self.draw_text('APERTE ESPAÇO', self.screen, [WIDTH // 2 + 10, 580], START_TEXT_SIZE,
                       (210, 150, 20), START_FONT)

        pygame.display.update()