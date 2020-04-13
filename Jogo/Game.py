import pygame
from random import randint
from tkinter import  *

class Teste:
    def Main(self):
        pygame.init()
        #Variáveis
        x = int(randint(0, 255))
        y = int(randint(0, 255))
        z = int(randint(0, 255))
        janela = pygame.display.set_mode([300,300])
        relogio = pygame.time.Clock()
        surface = pygame.Surface((200,200))
        ret = pygame.Rect(10,10,45,45)
        ret2 = pygame.Rect(100,100,80,80)

        sair = False
        while sair != True:
            cor = (x,y,z)
            cor2 = (z,x,y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        ret = ret.move(-10,0)
                    if event.key == pygame.K_RIGHT:
                        ret = ret.move(10,0)
                    if event.key == pygame.K_UP:
                        ret = ret.move(0,-10)
                    if event.key == pygame.K_DOWN:
                        ret = ret.move(0,10)

            janela.fill(cor)
            surface.fill(cor2)
            janela.blit(surface,[50,50])

            (xant,yant) = (ret.left,ret.top)

            pygame.draw.rect(janela,(y,z,x),ret)
            pygame.draw.rect(janela,(x,z,y),ret2)
            (ret.left,ret.top) = pygame.mouse.get_pos()
            ret.left -= ret.width/2
            ret.top -= ret.height/2

            if ret.colliderect(ret2):
                (ret.left,ret.top) = (xant,yant)

            relogio.tick(30)
            pygame.display.update()

        pygame.quit()
class Snake:
    def __init__(self):
       self.Y = 0
       self.X = 0
    def Comida(self):
        x = int(randint(0,300))
        y = int(randint(0,300))
        comida = pygame.Rect(x,y,15,15)

        return comida

    def SetX(self,x):
        self.X = x
    def SetY(self,y):
        self.Y = y
    def Game(self):
        pygame.init()

        cor1 = (25, 251, 36)
        cor2 = (251, 180, 24)

        relogio = pygame.time.Clock()
        janela = pygame.display.set_mode([300, 300])

        TICK = 0
        body = []
        head = pygame.Rect(150, 150, 25, 25)
        color = []

        i = 0
        x = 20
        y = 0


        xconf = 150
        yconf = 150
        xfinal = 0
        yfinal = 0

        sair = False
        comeu = True


        while sair == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if y != 20:
                            x = 0
                            y = -20
                    if event.key == pygame.K_DOWN:
                        if y != -20:
                            x = 0
                            y = 20
                    if event.key == pygame.K_LEFT:
                        if x != 20:
                            x = -20
                            y = 0
                    if event.key == pygame.K_RIGHT:
                       if x != -20:
                           x = 20
                           y = 0

            i += 1
            if xconf > 280:
                xfinal = -300
                xconf = 0
            if xconf < 0:
                xfinal = 300
                xconf = 280

            if yconf > 280:
                yfinal = -300
                yconf = 0
            if yconf < 0:
                yfinal = 300
                yconf = 280

            janela.fill((255, 255, 255))
            if comeu == True:
                comida = self.Comida()
                TICK += 10
                comeu = False


            if head.colliderect(comida):
                comeu = True
                body.append(pygame.Rect(head.x,head.y ,20,20))
                color.append((int(randint(0,255)),int(randint(0,255)),int(randint(0,255))))

            cont = 0
            for cuerpo in body:
                pygame.draw.rect(janela,color[cont],cuerpo)
                cont += 1

            cont = 0

            if i == 20:
                self.SetX(head.x - x/3)
                self.SetY(head.y - y/3)
                head = head.move(x + xfinal,y + yfinal)
                for corpo in body:
                    (xant,yant) = (corpo.x,corpo.y)
                    (corpo.x, corpo.y) = (self.X,self.Y)
                    self.SetX(xant - x/3)
                    self.SetY(yant - y/3)


                xconf += x
                yconf += y
                xfinal = 0
                yfinal = 0
                i = 0
                cont = 0
                for buyld in body:
                    if cont > 1:
                        if head.colliderect(buyld):
                            sair = True
                    cont += 1

            pygame.draw.rect(janela, (250, 0, 0), comida)
            pygame.draw.rect(janela, cor1, head)
            relogio.tick(30 + TICK)
            pygame.display.update()

        pygame.quit
class Draw:


    def __init__(self):
        self.SelectedColor = (255, 255, 255)
        self.Button = []
        self.desenho = []
        self.Cor = []
        self.Rect = pygame.Rect(500, 0, 100, 100)
        self.janela = pygame.display.set_mode([600, 800])
        self.relogio = pygame.time.Clock()
        self.setButton()
        self.setCor()
        self.setSelectedColor((0,0,0))
        self.desenho.append(pygame.Rect(500,0,4,4))

    def getSelectedColor(self):
        return self.SelectedColor
    def setSelectedColor(self,cor):
        self.SelectedColor = cor

    def setCor(self):
        for botoes in self.Button:
            self.Cor.append((int(randint(0,255)),int(randint(0,255)),int(randint(0,255))))


    def setButton(self):
        l = 0
        c = 0
        while l < 300:
            c = 0
            while c < 300:
                self.Button.append(pygame.Rect(c,l,30,30))
                c += 30
            l += 30

    def RectColor(self,position):
        a = 0
        b = 0
        i = 0
        (x,y) = position
        for botao in self.Button:
            if ((x >= b) & (x <= b + 30) & (y >= a) & (y <= a + 30)):
                self.setSelectedColor(self.Cor[i])
                break
            i += 1
            b += 30
            if b == 300:
                b = 0
                a += 30

    def Game(self):
        sair = False
        teste = 0
        while sair == False:
            self.janela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                if event.type == pygame.MOUSEBUTTONUP:
                    teste += 1
                    pos = pygame.mouse.get_pos()
                    if teste == 2:
                        teste = 0
                    self.RectColor(pygame.mouse.get_pos())

            i = 0
            (x,y) = pygame.mouse.get_pos()
            if teste == 1:
                if pos != pygame.mouse.get_pos():
                    self.desenho.append(pygame.Rect(x,y,4,4))
            for draw in self.desenho:
                pygame.draw.rect(self.janela,self.getSelectedColor(),draw)
            for botao in self.Button:
                pygame.draw.rect(self.janela,self.Cor[i],botao)
                i += 1
            pygame.draw.rect(self.janela,self.getSelectedColor(),self.Rect)
            self.relogio.tick(120)
            pygame.display.update()
        pygame.quit()

class Main:
    desenho = Draw()
    cobrinha = Snake()
    cobrinha.Game()

