import pygame
class Head(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite)
        self.head = []
        self.xant = 150
        self.yant = 1504

        self.head.append(pygame.image.load("Head/esquerda.png"))
        self.head.append(pygame.image.load("Head/direita.png"))
        self.head.append(pygame.image.load("Head/cima.png"))
        self.head.append(pygame.image.load("Head/baixo.png"))
        self.rect = []
        self.rect.append(self.head[0].get_rect())
        self.rect.append(self.head[1].get_rect())
        self.rect.append(self.head[2].get_rect())
        self.rect.append(self.head[3].get_rect())
        self.rect[0].x = 150
        self.rect[0].y = 150
        self.rect[1].x = 150
        self.rect[1].y = 150
        self.rect[2].x = 150
        self.rect[2].y = 150
        self.rect[3].x = 150
        self.rect[3].y = 150
        self.I = 0
    def Colidiu(self,parede,i):
        x = False
        if parede.colliderect(self.rect[i]):
            x = True
        return x
    def Show(self,superficie,x,y,i,colidiu):
        cont = 0
        for ret in self.rect:
            if cont != i:
                self.rect[cont].x = self.xant
                self.rect[cont].y = self.yant
            cont += 1
        if not colidiu:
            self.xant = self.rect[i].x
            self.yant = self.rect[i].y
            self.rect[self.I].x = self.xant
            self.rect[self.I].y = self.yant
            self.rect[i].x += x
            self.rect[i].y += y
            self.I = i
        else:
            self.rect[i].x = self.xant
            self.rect[i].y = self.yant

        superficie.blit(self.head[i],self.rect[i])

class PacMan:
    def __init__(self):
        self.janela = pygame.display.set_mode([300,300])
        self.relogio = pygame.time.Clock()
        self.paredes = []
        self.setParede()
    def setParede(self):
        self.paredes.append(pygame.Rect(0,0,300,10))
        self.paredes.append(pygame.Rect(0,290,300,10))
        self.paredes.append(pygame.Rect(0, 0, 10, 300))
        self.paredes.append(pygame.Rect(290, 0, 10, 300))

        self.paredes.append(pygame.Rect(40,250,80,10))
        self.paredes.append(pygame.Rect(90,230,10,20))
        self.paredes.append(pygame.Rect(180, 250, 80, 10))
        self.paredes.append(pygame.Rect(200, 230, 10, 20))

        self.paredes.append(pygame.Rect(40, 40, 80, 10))
        self.paredes.append(pygame.Rect(90, 50, 10, 20))
        self.paredes.append(pygame.Rect(180, 40, 80, 10))
        self.paredes.append(pygame.Rect(200, 50, 10, 20))

        self.paredes.append((pygame.Rect(40,170,10,60)))
        self.paredes.append((pygame.Rect(40, 70, 10, 60)))
        self.paredes.append((pygame.Rect(250, 170, 10, 60)))
        self.paredes.append((pygame.Rect(250, 70, 10, 60)))

        self.paredes.append((pygame.Rect(145,190,10,70)))
        self.paredes.append((pygame.Rect(145, 40, 10, 70)))


    def Game(self):
        sair = False
        sprite = Head()
        x = 0
        y = 0
        head = 0

        while sair == False:

            self.janela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x = -10
                        y = 0
                        head = 0
                    if event.key == pygame.K_RIGHT:
                        x = 10
                        y = 0
                        head = 1
                    if event.key == pygame.K_UP:
                        y = -10
                        x = 0
                        head = 2
                    if event.key == pygame.K_DOWN:
                        y = 10
                        x = 0
                        head = 3
                if event.type == pygame.KEYUP:
                    y = 0
                    x = 0





            colidiu = False
            for parede in self.paredes:
                pygame.draw.rect(self.janela,(0,0,0),parede)
                colidiu = sprite.Colidiu(parede,head)


            sprite.Show(self.janela,x,y,head,colidiu)


            self.relogio.tick(30)
            pygame.display.update()
        pygame.quit()
class Main:
    game = PacMan()
    game.Game()