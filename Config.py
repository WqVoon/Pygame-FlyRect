import time,random,pygame
from pygame import *
from random import randint
from sys import exit
pygame.init()
pygame.mixer.init()
fps = pygame.time.Clock()

#-------------------------Windows-----------------------------
surface = display.set_mode((600,400))
display.set_caption('Fly Rect')


#--------------------------Init-------------------------------
Bgm_Exist=1
times = 0
a = 15
b = 0
c = 15
po = [100,200]
move = 2

#---------------------------BGM-------------------------------
main_music = pygame.mixer.music
try:
    main_music.load('BGM/1.mp3')
except:
    Bgm_Exist=0
end_music = pygame.mixer.Sound('BGM/2.ogg')
get_music = pygame.mixer.Sound('BGM/get.wav')
hit_music = pygame.mixer.Sound('BGM/3.wav')
bo1_music = pygame.mixer.Sound('BGM/bit1.wav')
bo2_music = pygame.mixer.Sound('BGM/bit2.wav')

#UI Control
cho = 3

#----------------------------UI------------------------------
times=0
star_y = 200
title = font.Font(None,40).render('Fly Rect',True,Color(255,255,255))
title_x,title_y = title.get_size()
text = font.Font(None,32).render('Game Over',True,Color(255,255,255))
text_x,text_y = text.get_size()
tip = font.Font(None,25).render('--Press space to enter--',True,Color(255,255,255))
tip_x = tip.get_width()

#--------------------------Status---------------------------------
go = 0
li = 3
noene = 0

#--------------------------Object---------------------------------
class he:
    def restar(self):
        y = randint(150,200)
        self.po = [600,y]
        self.ty = randint(0,1)
        self.re = False
        if self.ty == 0:
            self.co = Color(255,0,0)
        elif self.ty == 1:
            self.co = Color(255,255,0)
    def __init__(self):
        self.restar()
    def move(self):
        if self.re:
            if self.po[0] > 0:
                self.po[0] -= 1
            elif self.po[0] <= 0:
                self.re = False
                self.restar()

class wall:
    def restar(self):
        y = randint(150,250 )
        self.po_start1 = [610,400]
        self.po_end1 = [610,y]
        self.po_start2 = [610,0]
        self.po_end2 = [610,y-100]
    def __init__(self):
        self.restar()
        self.re = False
    def move(self):
        if self.re:
            self.po_start1[0] -= 10
            self.po_start2[0] -= 10
            self.po_end1[0] -= 10
            self.po_end2[0] -= 10

Help = he()
Wall = [wall(),wall(),wall(),wall()]

