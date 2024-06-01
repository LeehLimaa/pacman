import pygame
pygame.init()


#Constantes - escritas com letras letras maiusculas
AMARELO=(255,255,0)
PRETO=(0,0,0)
AZUL=(0,0,255)
TAMANHO_TELA= 644
VELOCIDADE= 1


screen = pygame.display.set_mode((TAMANHO_TELA, TAMANHO_TELA), 0)


class Cenario:
    def __init__(self, tamanho, pac):
        self.tamanho = tamanho
        self.pacman = pac
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]


    def pintar(self, tela):
        #enumerate devolve o número da linha e o conteúdo da linha
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)


    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna*self.tamanho
            y = numero_linha*self.tamanho
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho),0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + self.tamanho/2, y + self.tamanho/2), self.tamanho//10, 0)


    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao
        if (col>0 and col<=28) and (0 <=lin <29):
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()




class Pacman:
    def __init__(self, tamanho_celula):
        self.linha = 1
        self.coluna = 1


        self.centro_x = 0
        self.centro_y = 0
        self.tamanho = tamanho_celula
        self.raio = self.tamanho/2
        self.vel_x = 0
        self.vel_y = 0


        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha


    def calcular_regras(self):


        #Eixo x - coluna
        self.coluna_intencao = self.coluna + self.vel_x
        self.centro_x = (self.coluna * self.tamanho + self.raio)


        #Eixo y - linha
        self.linha_intencao = self.linha + self.vel_y
        self.centro_y = (self.linha * self.tamanho + self.raio)


    def aceitar_movimento(self):
        self.coluna = self.coluna_intencao
        self.linha = self.linha_intencao


    def processar_eventos(self, eventos):
            for e in eventos:
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_RIGHT:
                        self.vel_x= VELOCIDADE
                    if e.key==pygame.K_LEFT:
                        self.vel_x= -VELOCIDADE


                if e.type==pygame.KEYUP:
                    if e.key==pygame.K_RIGHT:
                        self.vel_x= 0
                    if e.key==pygame.K_LEFT:
                        self.vel_x= 0


                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_DOWN:
                        self.vel_y= VELOCIDADE
                    if e.key==pygame.K_UP:
                        self.vel_y= -VELOCIDADE


                if e.type==pygame.KEYUP:
                    if e.key==pygame.K_DOWN:
                        self.vel_y= 0
                    if e.key==pygame.K_UP:
                        self.vel_y= 0


    #função do mouse
    def processar_eventos_mouse(self, eventos):
        for e in eventos:
            if e.type==pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                print(mouse_x, mouse_y)


    def pintar(self, tela):


        #corpo
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)


        #boca
        canto_boca=(self.centro_x, self.centro_y)
        labio_inferior=(self.centro_x + self.raio, self.centro_y)
        labio_superior=(self.centro_x + self.raio, self.centro_y - self.raio)
        pontos_boca=[canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos_boca, 0)


        #olho
        pygame.draw.circle(tela, PRETO, (self.centro_x, self.centro_y-self.raio/2), self.raio/8, 0)


if __name__ == '__main__':


    n_colunas = 28
    bloco_labirinto = int(TAMANHO_TELA//n_colunas)
    pacman=Pacman(bloco_labirinto)
    cenario=Cenario(bloco_labirinto, pacman)


    while True:


        #Regras
        pacman.calcular_regras()
        cenario.calcular_regras()


        #Pintar tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()


        pygame.time.delay(100)


        #Eventos
        eventos = pygame.event.get()
        for e in  eventos:
            if e.type == pygame.QUIT:
                exit()


        pacman.processar_eventos(eventos)



