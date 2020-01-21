from typing import List

import pygame, sys
from settings import *
from os import path

pygame.init()

pygame.display.set_caption("Pac Runner")  # Titulo da tela
favicon = pygame.image.load("img/favicon.png")  # Favicon
pygame.display.set_icon(favicon)  # Favicon

# IMAGENS
logo_pac = pygame.image.load('img/Logo_pac_runner.png')  # Logo da tela inicial
ghost_clyde = pygame.image.load('img/clyde.png')  # Imagem do fantasma laranja.
ghost_blink = pygame.image.load('img/blinky.png')  # Imagem do fantasma vermelho.
ghost_pinky = pygame.image.load('img/pinky.png')  # Imagem do fantasma rosa.
ghost_ink = pygame.image.load('img/inky.png')  # Imagem do fantasma azul.

# Posições para o pacman!
player_posC = [WIDTH // 2 - 40, 540]  # posição central do pacman
player_posL = [WIDTH // 2 - 146, 540]  # posição a esquerda do pacman
player_posR = [WIDTH // 2 + 66, 540]  # posição a direita do pacman
player_pac = [WIDTH // 2 - 40, 540]

# Configurações das moedas!
# pos_I = 80 # posição inicial da moeda no eixo Y
# pos_F = 540 # posição final da moeda no eixo Y
pos_y_C = 80
pos_y_L = 80
pos_y_R = 80
pos_y_C1 = -150
pos_y_L1 = -150
pos_y_R1 = -150

pos_c = WIDTH // 2  # posição da moeda do eixo X
pos_L = WIDTH // 2 - 106  # posição da moeda do eixo X
pos_R = WIDTH // 2 + 106  # posição da moeda do eixo X

# Posições dos fantasmas, as iniciais representa o nome do fantasma e a posição em que esta.
gcl = 0  # Fantasma Clyde da Esquerta
gcc = 0  # Fantaspa Clyde do Centro
gcr = 0  # Fantasma Clyde da Direita
gpl = 0  # Fantasma Pinky da Esquerda
gpc = 0  # Fantasma Pinky do Centro
gpr = 0  # Fantasma Pinky da Direita
gil = 0  # Fantasma Inky da Esquerda
gic = 0  # Fantasma Inky do Centro
gir = 0  # Fantasma Inky da Direita
gbl = 0  # Fantasma Blinky da Esquerda
gbc = 0  # Fantasma Blinky do Centro
gbr = 0  # Fantasma Blinky da direita

velocidade_y = 3

# Pontuação do jogo
score = 0
high_score = 0

# Background do menu superior na tela playing
menu_background = pygame.Rect(0, 0, 360, 60)


class App:

    def __init__(self):
        global score

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # variavel e tamanho da tela
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.player_pac = player_pac
        self.load()
        self.load_data()
        self.ghost_pos_ini()
        self.coin_pos_ini()
        self.speed()
        self.score = score = 0

    def speed(self): # esta função define a velocidade inicial.
        global velocidade_y

        velocidade_y = 3

    def coin_pos_ini(self): # Esta função define a posição inicial das moedas.
        global  pos_y_C, pos_y_L, pos_y_R, pos_y_C1, pos_y_L1, pos_y_R1
        pos_y_C = 80
        pos_y_L = 80
        pos_y_R = 80
        pos_y_C1 = -150
        pos_y_L1 = -150
        pos_y_R1 = -150

    def ghost_pos_ini(self): # Esta função define a posição inicial dos fantasmas.
        global gcr, gbl, gpr, gic, gcl, gbr, gir, gcc, gpl, gbc, gpc, gil

        gcl = 0  # Fantasma Clyde da Esquerta
        gcc = 0  # Fantaspa Clyde do Centro
        gcr = 0  # Fantasma Clyde da Direita
        gpl = 0  # Fantasma Pinky da Esquerda
        gpc = 0  # Fantasma Pinky do Centro
        gpr = 0  # Fantasma Pinky da Direita
        gil = 0  # Fantasma Inky da Esquerda
        gic = 0  # Fantasma Inky do Centro
        gir = 0  # Fantasma Inky da Direita
        gbl = 0  # Fantasma Blinky da Esquerda
        gbc = 0  # Fantasma Blinky do Centro
        gbr = 0  # Fantasma Blinky da direita

    def load_data(self):
        # Carrega o high score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, hs_file), 'r') as f:
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
        pos[0] = pos[0] - text_size[0] // 2
        pos[0] = pos[0] - text_size[1] // 2
        screen.blit(text, pos)

    def load(self):
        global score, pos_y

        self.background = pygame.image.load('img/fundo.png')
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.pacman = pygame.image.load('img/Pac2.png')
        self.pacman = pygame.transform.scale(self.pacman, (80, 80))
        self.pause_off = pygame.image.load('img/btn_pause_off.png')
        # self.pause_on = pygame.image.load('img/btn_pause_on.png')
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
    def ghosts(self):
        global player_posL, player_posC, player_posR, gcr, gbl, gpr, gic, gcl, gbr, gir, gcc, gpl, gbc, gpc, gil

        # blink da esquerda - Vermelho
        self.screen.blit(self.blinky, (pos_L - 40, gbl))
        gbl += velocidade_y - 1
        if self.player_pac == player_posL and gbl > 480:
            self.state = 'game_over'
        elif gbl > 640:
            gbl = -1860

        # Pinky da direita - rosa
        self.screen.blit(self.pinky, (pos_R - 40, gpr - 250))
        gpr += velocidade_y - 1
        if self.player_pac == player_posR and gpr > 730:
            self.state = 'game_over'
        elif gpr > 890:
            gpr = -1610

        # inky do meio - Azul
        self.screen.blit(self.inky, (pos_c - 40, gic - 500))
        gic += velocidade_y - 1
        if self.player_pac == player_posC and gic > 980:  # gbr = 480 + primeiro gir
            self.state = 'game_over'
        elif gic > 1140:
            gic = -1360

        # clyde da esquerda duo - Laranja
        self.screen.blit(self.clyde, (pos_L - 40, gcl - 750))
        gcl += velocidade_y - 1
        if self.player_pac == player_posL and gcl > 1230:
            self.state = 'game_over'
        elif gcl > 1390:
            gcl = -1110

        # blink da direita duo - Vermelho
        self.screen.blit(self.blinky, (pos_R - 40, gbr - 750))
        gbr += velocidade_y - 1
        if self.player_pac == player_posR and gbr > 1230:
            self.state = 'game_over'
        elif gbr > 1390:
            gbr = -1110

        # inky da direita - Azul
        self.screen.blit(self.inky, (pos_R - 40, gir - 1000))
        gir += velocidade_y - 1
        if self.player_pac == player_posR and gir > 1480:  # gbr = 480 + primeiro gir
            self.state = 'game_over'
        elif gir > 1640:  # gir = 640 + primeiro gir
            gir = -860

        # Clyde do centro - Laranja
        self.screen.blit(self.clyde, (pos_c - 40, gcc - 1250))
        gcc += velocidade_y - 1
        if self.player_pac == player_posC and gcc > 1730:  # gcc = 480 + primeiro gcc
            self.state = 'game_over'
        elif gcc > 1890:  # gcc = 640 + primeiro gcc
            gcc = -610

        # Pinky da esquerda - Rosa
        self.screen.blit(self.pinky, (pos_L - 40, gpl - 1500))
        gpl += velocidade_y - 1
        if self.player_pac == player_posL and gpl > 1980:  # gpl = 480 + primeiro gpl
            self.state = 'game_over'
        elif gpl > 2140:  # gpl = 640 + primeiro gpl
            gpl = -360

        # Blinky do centro - Vermelho
        self.screen.blit(self.blinky, (pos_c - 40, gbc - 1750))
        gbc += velocidade_y - 1
        if self.player_pac == player_posC and gbc > 2230:  # gbc = 480 + primeiro gbc
            self.state = 'game_over'
        elif gbc > 2390:  # gbc = 640 + primeiro gbc
            gbc = -110

        # Pinky do centro duo - Rosa
        self.screen.blit(self.pinky, (pos_c - 40, gpc - 2000))
        gpc += velocidade_y - 1
        if self.player_pac == player_posC and gpc > 2480:  # gpc = 480 + primeiro gpc
            self.state = 'game_over'
        elif gpc > 2640:  # gpc = 640 + primeiro gpc
            gpc = 140

        # Inky da esquerda duo - Azul
        self.screen.blit(self.inky, (pos_L - 40, gil - 2000))
        gil += velocidade_y - 1
        if self.player_pac == player_posL and gil > 2480:  # gil = 480 + primeiro gil
            self.state = 'game_over'
        elif gil > 2640:  # gil = 640 + primeiro gil
            gil = 140

        # Clyde da esquerda - Laranja
        self.screen.blit(self.clyde, (pos_R - 40, gcr - 2250))
        gcr += velocidade_y - 1
        if self.player_pac == player_posR and gcr > 2730:  # gcr = 480 + primeiro gcr
            self.state = 'game_over'
        elif gcr > 2890:  # gcr = 640 + primeiro gcr
            gcr = 390

    def coin_center(self):
        global pos_y, pos_L, pos_R, pos_c, score, pos_y_C, pos_y_C1, pos_y_L, pos_y_L1, pos_y_R

        # Contador de pontos das moeda do meio.
        if self.player_pac == player_posC and pos_y_C1 >= 539 or self.player_pac == player_posC and pos_y_C >= 539:
            score += 1

        # Primeira moeda
        pygame.draw.circle(self.screen, YELLOW, (pos_c, pos_y_C), 7)
        pos_y_C += velocidade_y  # Movimentação da moeda
        if self.player_pac == player_posC and pos_y_C > 540 or pos_y_C > 640:
            pos_y_C = 80

        # Segunda moeda
        pygame.draw.circle(self.screen, YELLOW, (pos_c, pos_y_C1), 7)
        pos_y_C1 += velocidade_y  # Movimentação da moeda
        if self.player_pac == player_posC and pos_y_C1 > 540 or pos_y_C1 > 640:
            pos_y_C1 = -150

    def coin_right(self):
        global pos_y, pos_L, pos_R, pos_C, score, pos_y_C, pos_y_C1, pos_y_L, pos_y_L1, pos_y_R, pos_y_R1

        # Contador de pontos das moeda da direita.
        if self.player_pac == player_posR and pos_y_R1 >= 539 or self.player_pac == player_posR and pos_y_R >= 539:
            score += 1

        # Primeira moeda da direita.
        pygame.draw.circle(self.screen, YELLOW, (pos_R, pos_y_R), 7)
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

    def velocidade(self): # Velocidade de movimento das moedas e dos fantasmas
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

        self.screen.blit(logo_pac, [75, HEIGHT // 2 - 50])

        self.draw_text('PARA INICIAR APERTE ESPAÇO', self.screen, [WIDTH // 2 + 10, 580], START_TEXT_SIZE,
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
        self.screen.blit(self.background, (0, 0))  # Aqui representa as barras laterais do fundo.

        self.coin_center()  # Moedas do meio
        self.coin_left()  # Moedas da esquerda.
        self.coin_right()  # Moedas da direita.

        self.ghosts()  # Fantasmas

        pygame.draw.rect(self.screen, BLACK, menu_background)  # Background do menu superior da "tela playing".

        self.draw_text('PONTOS', self.screen, [WIDTH // 2 + 10, 10], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)
        # Melhor pontuação do jogo, precisa criar o contador
        self.draw_text('{}'.format(score), self.screen, [WIDTH // 2 + 10, 30], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)

        self.screen.blit(self.pacman, self.player_pac)  # Aqui representa o pacman.

        self.screen.blit(self.pause_off, (15, 15))  # Aqui representa o botão pause, mas ainda não esta ativado.
        self.screen.blit(self.btn_exit, (320, 15))  # Aqui representa o botão pause, mas ainda não esta ativado.
        self.velocidade()  # Aqui faz com que as moedas e fantasmas se movimentem, o codigo referente a essa funcionalidade esta na linha 179

        pygame.display.update()

################################################# GAME OVER ############################################################

    def game_over_events(self):
        global score, gcr, gbl, gpr, gic, gcl, gbr, gir, gcc, gpl, gbc, gpc, gil

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Na tela de game over "game_over" ao apertar a barra de espaço, inicia o jogo indo para a tela "playing".
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.__init__()
                self.score # Reinicia a pontuação
                self.ghost_pos_ini() # Reinicia a posição dos fantasmas
                self.coin_pos_ini() # Reinicia a posição das moedas.
                self.speed() # Reinicia a velocidade
                self.state = 'playing' # chama a tela do jogo

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.__init__()
                self.score  # Reinicia a pontuação
                self.ghost_pos_ini()  # Reinicia a posição dos fantasmas
                self.coin_pos_ini()  # Reinicia a posição das moedas.
                self.speed()  # Reinicia a velocidade
                self.state = 'start'  # chama a tela inicial

    def game_over_update(self):
        pass

    def game_over_draw(self):
        global score

        self.screen.fill(BLACK)
        #self.draw_text('SUA PONTUAÇÃO', self.screen, [WIDTH // 2 + 10, 10], START_TEXT_SIZE, (255, 255, 255), START_FONT)
        # Melhor pontuação do jogo, precisa criar o contador
        #self.draw_text(str(self.highscore), self.screen, [WIDTH // 2 + 10, 30], START_TEXT_SIZE,
                       #(255, 255, 255), START_FONT)

        if score >= self.highscore:
            self.draw_text('NOVO RECORDE', self.screen, [WIDTH // 2 + 10, 10], START_TEXT_SIZE, (255, 255, 255),
                           START_FONT)
            self.highscore = score
            with open(path.join(self.dir, hs_file), 'w') as f:
                f.write(str(score))
        elif score < self.highscore:
            self.draw_text('SUA PONTUAÇÃO', self.screen, [WIDTH // 2 + 10, 10], START_TEXT_SIZE, (255, 255, 255),
                           START_FONT)




        self.draw_text('{}'.format(score), self.screen, [WIDTH // 2 + 10, 30], START_TEXT_SIZE,
                       (255, 255, 255), START_FONT)

        self.draw_text('GAME OVER', self.screen, [WIDTH // 2 + 10, HEIGHT // 2 - 50], GAME_OVER_SIZE,
                       (255, 0, 0), GAME_OVER_FONT)

        self.draw_text('PARA JOGAR NOVAMENTE', self.screen, [WIDTH // 2 + 10, 540], START_TEXT_SIZE,
                       (210, 150, 20), START_FONT)
        self.draw_text('APERTE ESPAÇO', self.screen, [WIDTH // 2 + 10, 580], START_TEXT_SIZE,
                       (210, 150, 20), START_FONT)

        pygame.display.flip()


