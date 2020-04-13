from tkinter import *
from random import randint

#Meu Primeiro Programa em Python
#By ThiDiamond

class Tabuleiro(object):
    janela = Tk()

    B_Verde = PhotoImage(file="verde.png")
    B_Vermelho = PhotoImage(file="vermelho.png")
    damaRed = PhotoImage(file = "damavermelha.png")
    damaGreen = PhotoImage(file = "damaverde.png")
    casa = []
    botao = []
    Fundo = PhotoImage(file = "preto.png")
    selected = -1
    destiny = -1

    B = []
    i = 0
    while i < 64:
        B.append(PhotoImage(file = "preto.png"))
        i += 1







    def SetCasa(self):
        self.SetTable()
        i = 0
        while i < 65:
            self.botao.append(Button(self.janela))
            i += 1

        self.botao[0] = Button(self.casa[0],bg = "black", image=self.B_Verde, command=self.C_0)
        self.botao[0].pack()
        self.B[0] = self.B_Verde
        self.botao[2] = Button(self.casa[2],bg = "black", image=self.B_Verde, command=self.C_2)
        self.botao[2].pack()
        self.B[2] = self.B_Verde
        self.botao[4] = Button(self.casa[4],bg = "black", image=self.B_Verde, command=self.C_4)
        self.botao[4].pack()
        self.B[4] = self.B_Verde
        self.botao[6] = Button(self.casa[6],bg = "black", image=self.B_Verde, command=self.C_6)
        self.botao[6].pack()
        self.B[6] = self.B_Verde

        self.botao[9] = Button(self.casa[9],bg = "black", image=self.B_Verde, command=self.C_9)
        self.botao[9].pack()
        self.B[9] = self.B_Verde
        self.botao[11] = Button(self.casa[11],bg = "black", image=self.B_Verde, command=self.C_11)
        self.botao[11].pack()
        self.B[11] = self.B_Verde
        self.botao[13] = Button(self.casa[13],bg = "black", image=self.B_Verde, command=self.C_13)
        self.botao[13].pack()
        self.B[13] = self.B_Verde
        self.botao[15] = Button(self.casa[15],bg = "black", image=self.B_Verde, command=self.C_15)
        self.botao[15].pack()
        self.B[15] = self.B_Verde

        self.botao[16] = Button(self.casa[16],bg = "black", image=self.B_Verde, command=self.C_16)
        self.botao[16].pack()
        self.B[16] = self.B_Verde
        self.botao[18] = Button(self.casa[18],bg = "black", image=self.B_Verde, command=self.C_18)
        self.botao[18].pack()
        self.B[18] = self.B_Verde
        self.botao[20] = Button(self.casa[20],bg = "black", image=self.B_Verde, command=self.C_20)
        self.botao[20].pack()
        self.B[20] = self.B_Verde
        self.botao[22] = Button(self.casa[22],bg = "black", image=self.B_Verde, command=self.C_22)
        self.botao[22].pack()
        self.B[22] = self.B_Verde


        self.botao[25] = Button(self.casa[25],bg = "black", image=self.Fundo, command=self.C_25)
        self.botao[25].pack()
        self.B[25] = self.Fundo
        self.botao[27] = Button(self.casa[27],bg = "black", image=self.Fundo, command=self.C_27)
        self.botao[27].pack()
        self.B[27] = self.Fundo
        self.botao[29] = Button(self.casa[29],bg = "black", image=self.Fundo, command=self.C_29)
        self.botao[29].pack()
        self.B[29] = self.Fundo
        self.botao[31] = Button(self.casa[31],bg = "black", image=self.Fundo, command=self.C_31)
        self.botao[31].pack()
        self.B[31] = self.Fundo

        self.botao[32] = Button(self.casa[32],bg = "black", image=self.Fundo, command=self.C_32)
        self.botao[32].pack()
        self.B[32] = self.Fundo
        self.botao[34] = Button(self.casa[34],bg = "black", image=self.Fundo, command=self.C_34)
        self.botao[34].pack()
        self.B[34] = self.Fundo
        self.botao[36] = Button(self.casa[36],bg = "black", image=self.Fundo, command=self.C_36)
        self.botao[36].pack()
        self.B[36] = self.Fundo
        self.botao[38] = Button(self.casa[38],bg = "black", image=self.Fundo, command=self.C_38)
        self.botao[38].pack()
        self.B[38] = self.Fundo

        self.botao[41] = Button(self.casa[41],bg = "black", image=self.B_Vermelho, command=self.C_41)
        self.botao[41].pack()
        self.B[41] = self.B_Vermelho
        self.botao[43] = Button(self.casa[43],bg = "black", image=self.B_Vermelho, command=self.C_43)
        self.botao[43].pack()
        self.B[43] = self.B_Vermelho
        self.botao[45] = Button(self.casa[45],bg = "black", image=self.B_Vermelho, command=self.C_45)
        self.botao[45].pack()
        self.B[45] = self.B_Vermelho
        self.botao[47] = Button(self.casa[47],bg = "black", image=self.B_Vermelho, command=self.C_47)
        self.botao[47].pack()
        self.B[47] = self.B_Vermelho

        self.botao[48] = Button(self.casa[48],bg = "black", image=self.B_Vermelho, command=self.C_48)
        self.botao[48].pack()
        self.B[48] = self.B_Vermelho
        self.botao[50] = Button(self.casa[50],bg = "black", image=self.B_Vermelho, command=self.C_50)
        self.botao[50].pack()
        self.B[50] = self.B_Vermelho
        self.botao[52] = Button(self.casa[52],bg = "black", image=self.B_Vermelho, command=self.C_52)
        self.botao[52].pack()
        self.B[52] = self.B_Vermelho
        self.botao[54] = Button(self.casa[54],bg = "black", image=self.B_Vermelho, command=self.C_54)
        self.botao[54].pack()
        self.B[54] = self.B_Vermelho

        self.botao[57] = Button(self.casa[57],bg = "black", image=self.B_Vermelho, command=self.C_57)
        self.botao[57].pack()
        self.B[57] = self.B_Vermelho
        self.botao[59] = Button(self.casa[59],bg = "black", image=self.B_Vermelho, command=self.C_59)
        self.botao[59].pack()
        self.B[59] = self.B_Vermelho
        self.botao[61] = Button(self.casa[61],bg = "black", image=self.B_Vermelho, command=self.C_61)
        self.botao[61].pack()
        self.B[61] = self.B_Vermelho
        self.botao[63] = Button(self.casa[63],bg = "black", image=self.B_Vermelho, command=self.C_63)
        self.botao[63].pack()
        self.B[63] = self.B_Vermelho

    def Possibilidades(self):
        l = 0
        x = 0
        simples = []
        tipo = []


        while l < 64:

                if ((self.B[l] == self.B_Verde)|(self.B[l] == self.damaGreen)):
                    if l + 14 < 64:
                        if self.B[l] == self.damaGreen:
                            peca = self.damaGreen
                        elif l + 14 < 55:
                            peca = self.B_Verde
                        else:
                            peca = self.damaGreen
                        if ((self.B[l+7] == self.B_Vermelho)|(self.B[l+7] == self.damaRed))&( self.B[l+14] == self.Fundo):
                            self.botao[l]["image"] = self.Fundo
                            self.B[l] = self.Fundo
                            self.botao[l+7]["image"] = self.Fundo
                            self.B[l+7] = self.Fundo
                            self.botao[l+14]["image"] = peca
                            self.B[l+14] = peca
                            print("COMI!!!")
                            return
                    if l - 14 >= 0:
                        if (self.B[l] == self.damaGreen)&((self.B[l-7] == self.B_Vermelho)|(self.B[l-7] == self.damaRed))&( self.B[l-14] == self.Fundo):
                            self.botao[l]["image"] = self.Fundo
                            self.B[l] = self.Fundo
                            self.botao[l-7]["image"] = self.Fundo
                            self.B[l-7] = self.Fundo
                            self.botao[l-14]["image"] = self.damaGreen
                            self.B[l-14] = self.damaGreen
                            return
                    if l + 18 < 64:
                        if self.B[l] == self.damaGreen:
                            peca = self.damaGreen
                        elif l + 18 < 55:
                            peca = self.B_Verde
                        else:
                            peca = self.damaGreen
                        if ((self.B[l+9] == self.B_Vermelho)|(self.B[l+9] == self.damaRed))&(self.B[l+18] == self.Fundo)&(l + 18 < 64 ):
                            self.botao[l]["image"] = self.Fundo
                            self.B[l] = self.Fundo
                            self.botao[l+9]["image"] = self.Fundo
                            self.B[l+9] = self.Fundo
                            self.botao[l+18]["image"] = peca
                            self.B[l+18] = peca
                            print("COMI")
                            return
                    if l - 18 >= 0:
                        if (self.B[l] == self.damaGreen)&((self.B[l-9] == self.B_Vermelho)|(self.B[l-9] == self.damaRed))&( self.B[l-18] == self.Fundo):
                            self.botao[l]["image"] = self.Fundo
                            self.B[l] = self.Fundo
                            self.botao[l-9]["image"] = self.Fundo
                            self.B[l-9] = self.Fundo
                            self.botao[l-18]["image"] = peca
                            self.B[l-18] = peca
                            return

                    if l + 7 < 64:
                        if self.B[l+7] == self.Fundo:
                            simples.append(l)
                            tipo.append(1)
                            x += 1
                    if l + 9 < 64:
                        if self.B[l+9] == self.Fundo:
                            simples.append(l)
                            tipo.append(2)
                            x += 1
                    if self.B[l] == self.damaGreen:
                        if l - 7 >= 0:
                            if self.B[l - 7] == self.Fundo:
                                simples.append(l)
                                tipo.append(3)
                                x += 1
                        if l - 9 >= 0:
                            if self.B[l - 9] == self.Fundo:
                                simples.append(l)
                                tipo.append(4)
                                x += 1
                l += 1

        sorte = int(randint(0,x-1))
        print(tipo[sorte])
        if tipo[sorte] == 1:
            if self.B[simples[sorte]] == self.B_Verde:
                if simples[sorte] + 7 < 55:
                    peca = self.B_Verde
                else:
                    peca = self.damaGreen
            else:
                peca = self.damaGreen
            self.botao[simples[sorte]]["image"] = self.Fundo
            self.B[simples[sorte]] = self.Fundo
            self.botao[simples[sorte]+7]["image"] = peca
            self.B[simples[sorte]+7] = peca

        if tipo[sorte] == 2:
            if self.B[simples[sorte]] == self.B_Verde:
                if simples[sorte] + 9 < 55:
                    peca = self.B_Verde
                else:
                    peca = self.damaGreen
            else:
                peca = self.damaGreen
            self.botao[simples[sorte]]["image"] = self.Fundo
            self.B[simples[sorte]] = self.Fundo
            self.botao[simples[sorte]+9]["image"] = peca
            self.B[simples[sorte]+9] = peca

        if tipo[sorte] == 3:
            self.botao[simples[sorte]]["image"] = self.Fundo
            self.B[simples[sorte]] = self.Fundo
            self.botao[simples[sorte] - 7]["image"] = self.damaGreen
            self.B[simples[sorte] - 7] = self.damaGreen

        if tipo[sorte] == 4:
            self.botao[simples[sorte]]["image"] = self.Fundo
            self.B[simples[sorte]] = self.Fundo
            self.botao[simples[sorte] - 9]["image"] = self.damaGreen
            self.B[simples[sorte] - 9] = self.damaGreen




    def Jogada(self,selected, destiny):

        x = selected - destiny
        if self.B[selected] == self.B_Vermelho:
            if destiny > 6:
                peca = self.B_Vermelho
            else:
                peca = self.damaRed
        elif self.B[selected] == self.damaRed:
            peca = self.damaRed
        if((self.B[destiny] == self.Fundo)):
            if x == 7:
                self.botao[destiny]["image"] = peca
                self.botao[selected]["image"] = self.Fundo
                self.B[destiny] = peca
                self.B[selected] = self.Fundo
                self.destiny = -1
                self.selected = -1
                self.Possibilidades()
            if x == 9:
                self.botao[destiny]["image"] = peca
                self.botao[selected]["image"] = self.Fundo
                self.B[destiny] = peca
                self.B[selected] = self.Fundo
                self.destiny = -1
                self.selected = -1
                self.Possibilidades()
            if x == 14:
                if (self.B[destiny + 7] == self.B_Verde)|(self.B[destiny + 7] == self.damaGreen):
                    self.botao[destiny]["image"] = peca
                    self.botao[destiny+7]["image"] = self.Fundo
                    self.botao[selected]["image"] = self.Fundo
                    self.B[destiny] = peca
                    self.B[selected] = self.Fundo
                    self.B[destiny+7] = self.Fundo
                    self.destiny = -1
                    self.selected = -1
                    self.Possibilidades()
            if x == 18:
                if (self.B[destiny + 9] == self.B_Verde)|(self.B[destiny + 9] == self.damaGreen):
                    self.botao[destiny]["image"] = peca
                    self.botao[destiny + 9]["image"] = self.Fundo
                    self.botao[selected]["image"] = self.Fundo
                    self.B[destiny] = peca
                    self.B[selected] = self.Fundo
                    self.B[destiny + 9] = self.Fundo
                    self.destiny = -1
                    self.selected = -1
                    self.Possibilidades()
            if x == 28:
                if(self.B[destiny+7] == self.B_Verde) & (self.B[destiny+14] == self.Fundo) & (self.B[destiny+21] == self.B_Verde):
                    self.botao[destiny]["image"] = peca
                    self.botao[destiny + 7]["image"] = self.Fundo
                    self.botao[destiny + 21]["image"] = self.Fundo
                    self.botao[selected]["image"] = self.Fundo
                    self.B[destiny] = peca
                    self.B[selected] = self.Fundo
                    self.B[destiny + 7] = self.Fundo
                    self.B[destiny + 21] = self.Fundo
                    self.destiny = -1
                    self.selected = -1
                    self.Possibilidades()
            if x == 36:
                if(self.B[destiny+9] == self.B_Verde) & (self.B[destiny+18] == self.Fundo) &( self.B[destiny+27] == self.B_Verde):
                    self.botao[destiny]["image"] = peca
                    self.botao[destiny + 9]["image"] = self.Fundo
                    self.botao[destiny + 27]["image"] = self.Fundo
                    self.botao[selected]["image"] = self.Fundo
                    self.B[destiny] = peca
                    self.B[selected] = self.Fundo
                    self.B[destiny + 9] = self.Fundo
                    self.B[destiny + 27] = self.Fundo
                    self.destiny = -1
                    self.selected = -1
                    self.Possibilidades()
            if x == 32:
                if (self.B[destiny + 7] == self.B_Verde) & (self.B[destiny + 14] == self.Fundo) & (self.B[destiny + 23] == self.B_Verde):
                    self.botao[destiny]["image"] = peca
                    self.botao[destiny + 7]["image"] = self.Fundo
                    self.botao[destiny + 23]["image"] = self.Fundo
                    self.botao[selected]["image"] = self.Fundo
                    self.B[destiny] = peca
                    self.B[selected] = self.Fundo
                    self.B[destiny + 7] = self.Fundo
                    self.B[destiny + 23] = self.Fundo
                    self.destiny = -1
                    self.selected = -1
                    self.Possibilidades()
                elif (self.B[destiny + 9] == self.B_Verde) & (self.B[destiny + 18] == self.Fundo) & (self.B[destiny + 25] == self.B_Verde):
                    self.botao[destiny]["image"] = peca
                    self.botao[destiny + 9]["image"] = self.Fundo
                    self.botao[destiny + 25]["image"] = self.Fundo
                    self.botao[selected]["image"] = self.Fundo
                    self.B[destiny] = peca
                    self.B[selected] = self.Fundo
                    self.B[destiny + 9] = self.Fundo
                    self.B[destiny + 25] = self.Fundo
                    self.destiny = -1
                    self.selected = -1
                    self.Possibilidades()
            if self.B[selected] == self.damaRed:
                if x == -7:
                    self.botao[destiny]["image"] = peca
                    self.botao[selected]["image"] = self.Fundo
                    self.B[destiny] = peca
                    self.B[selected] = self.Fundo
                    self.destiny = -1
                    self.selected = -1
                    self.Possibilidades()
                if x == -9:
                    self.botao[destiny]["image"] = peca
                    self.botao[selected]["image"] = self.Fundo
                    self.B[destiny] = peca
                    self.B[selected] = self.Fundo
                    self.destiny = -1
                    self.selected = -1
                    self.Possibilidades()
                if x == -14:
                    if self.B[destiny - 7] == self.B_Verde:
                        self.botao[destiny]["image"] = peca
                        self.botao[destiny - 7]["image"] = self.Fundo
                        self.botao[selected]["image"] = self.Fundo
                        self.B[destiny] = peca
                        self.B[selected] = self.Fundo
                        self.B[destiny - 7] = self.Fundo
                        self.destiny = -1
                        self.selected = -1
                        self.Possibilidades()
                if x == -18:
                    if self.B[destiny - 9] == self.B_Verde:
                        self.botao[destiny]["image"] = peca
                        self.botao[destiny - 9]["image"] = self.Fundo
                        self.botao[selected]["image"] = self.Fundo
                        self.B[destiny] = peca
                        self.B[selected] = self.Fundo
                        self.B[destiny - 9] = self.Fundo
                        self.destiny = -1
                        self.selected = -1
                        self.Possibilidades()
                if x == -28:
                    if (self.B[destiny - 7] == self.B_Verde) & (self.B[destiny - 14] == self.Fundo) & (
                            self.B[destiny - 21] == self.B_Verde):
                        self.botao[destiny]["image"] = peca
                        self.botao[destiny - 7]["image"] = self.Fundo
                        self.botao[destiny - 21]["image"] = self.Fundo
                        self.botao[selected]["image"] = self.Fundo
                        self.B[destiny] = peca
                        self.B[selected] = self.Fundo
                        self.B[destiny - 7] = self.Fundo
                        self.B[destiny - 21] = self.Fundo
                        self.destiny = -1
                        self.selected = -1
                        self.Possibilidades()
                if x ==  -36:
                    if (self.B[destiny - 9] == self.B_Verde) & (self.B[destiny - 18] == self.Fundo) & (
                            self.B[destiny - 27] == self.B_Verde):
                        self.botao[destiny]["image"] = peca
                        self.botao[destiny - 9]["image"] = self.Fundo
                        self.botao[destiny - 27]["image"] = self.Fundo
                        self.botao[selected]["image"] = self.Fundo
                        self.B[destiny] = peca
                        self.B[selected] = self.Fundo
                        self.B[destiny - 9] = self.Fundo
                        self.B[destiny - 27] = self.Fundo
                        self.destiny = -1
                        self.selected = -1
                        self.Possibilidades()
                if x == 32:
                    if (self.B[destiny - 7] == self.B_Verde) & (self.B[destiny + 14] == self.Fundo) & (
                            self.B[destiny - 23] == self.B_Verde):
                        self.botao[destiny]["image"] = peca
                        self.botao[destiny - 7]["image"] = self.Fundo
                        self.botao[destiny - 23]["image"] = self.Fundo
                        self.botao[selected]["image"] = self.Fundo
                        self.B[destiny] = peca
                        self.B[selected] = self.Fundo
                        self.B[destiny - 7] = self.Fundo
                        self.B[destiny - 23] = self.Fundo
                        self.destiny = -1
                        self.selected = -1
                        self.Possibilidades()
                    elif (self.B[destiny - 9] == self.B_Verde) & (self.B[destiny + 18] == self.Fundo) & (
                            self.B[destiny - 25] == self.B_Verde):
                        self.botao[destiny]["image"] = peca
                        self.botao[destiny - 9]["image"] = self.Fundo
                        self.botao[destiny - 25]["image"] = self.Fundo
                        self.botao[selected]["image"] = self.Fundo
                        self.B[destiny] = peca
                        self.B[selected] = self.Fundo
                        self.B[destiny - 9] = self.Fundo
                        self.B[destiny - 25] = self.Fundo
                        self.destiny = -1
                        self.selected = -1
                        self.Possibilidades()


    def C_0(self):
        x = 0
        if (self.B[x] == self.damaRed)|(self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_2(self):

        x = 2
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_4(self):
        x = 4
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_6(self):
        x = 6
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_9(self):
        x = 9
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_11(self):
        x = 11
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_13(self):
        x = 13
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_15(self):
        x = 15
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_16(self):
        x = 16
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_18(self):
        x = 18
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_20(self):
        x = 20
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_22(self):
        x = 22
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_25(self):
        x = 25
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_27(self):
        x = 27
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_29(self):
        x = 29
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_31(self):
        x = 31
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_32(self):
        x = 32
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_34(self):
        x = 34
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_36(self):
        x = 36
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_38(self):
        x = 38
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_41(self):
        x = 41
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_43(self):
        x = 43
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_45(self):
        x = 45
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_47(self):
        x = 47
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_48(self):
        x = 48
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_50(self):
        x = 50
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_52(self):
        x = 52
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_54(self):
        x = 54
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_57(self):
        x = 57
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_59(self):
        x = 59
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_61(self):
        x = 61
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)
    def C_63(self):
        x = 63
        if (self.B[x] == self.damaRed) | (self.B[x] == self.B_Vermelho):
            self.selected = x
        elif self.B[x] == self.Fundo:
            self.destiny = x
        if (self.selected != -1 & self.destiny != -1):
            self.Jogada(self.selected, self.destiny)



    def SetTable(self):

        cont = 0
        SIZE = 70
        X = 0
        Y = 0
        cor = "black"


        ptr = 0

        while ptr < 70:
            self.botao.append(1)
            ptr += 1

        while cont < 64:
            if cor == "white":
                cor = "black"
            else:
                cor = "white"
            if cont % 8 == 0:
                if cor == "white":
                    cor = "black"
                else:
                    cor = "white"

            self.casa.append(Frame(self.janela, bg=cor, width=SIZE, height=SIZE))
            cont += 1




        cont = 0
        while cont < 64:
            if X > 490:
                X = 0
                Y += 70
            self.casa[cont].place(x = X,y = Y)
            cont+=1
            X+=70

    def Mostrar(self):
        self.janela.geometry("600x600+500+500")
        self.SetTable()
        self.SetCasa()
        self.janela.mainloop()


class Main:
    table = Tabuleiro()
    table.Mostrar()





