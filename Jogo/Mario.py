import pygame

class Teste:
    def __init__(self):
        pygame.init()
        #Variáveis

        self.Boneco = pygame.Rect(20,260,30,30)
        self.janela = pygame.display.set_mode([400,400])
        self.relogio = pygame.time.Clock()
        self.piso = pygame.Rect(-50,300,500,100)
        self.enemy = pygame.Rect(270,260,25,25)
        self.list = []
        self.list.append(self.Boneco)
        self.list.append(self.enemy)

    def Fisica(self,y):
        for item in self.list:
            item.y += 10 + y
            if item.colliderect(self.piso):
                item.y = 300 - item.width
            if item.x == 400:
                item.x -= 400
            if item.x <= 0:
                item.x = 0

    def Game(self):
        sair = False
        x = 0
        y = 0
        contpulo = 0
        while sair != True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                       x = 10
                    if event.key == pygame.K_LEFT:
                            x = -10
                    if event.key == pygame.K_SPACE:
                        if contpulo == 0:
                            if self.Boneco.y == 270:
                                contpulo += 1
                        if contpulo == 1:
                            y = -20
                            contpulo += 1
                        elif contpulo == 2:
                            y = -20
                            contpulo = 0


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                       x = 0
                    if event.key == pygame.K_LEFT:
                        x = 0

            if y < 0:
                y += 1

            self.Fisica(y)
            if self.Boneco.x > self.enemy.x:
                self.enemy.x += -10
            else:
                self.enemy.x += 10

            self.Boneco.x += x
            self.janela.fill((255,255,255))
            #Draws
            pygame.draw.rect(self.janela,(0,0,0),self.piso)
            pygame.draw.rect(self.janela,(255,0,0),self.Boneco)
            pygame.draw.rect(self.janela,(0,255,0),self.enemy)

            self.relogio.tick(30)
            pygame.display.update()

        pygame.quit()
class Main:
    teste = Teste()
    teste.Game()