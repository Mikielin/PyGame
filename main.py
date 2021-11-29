import pygame, sys, random, math
from pygame.locals import *

arquivo = open("dados.game", "r")
dados = arquivo.read()
arquivo.close()

nome = input("Informe o nome do jogador: ")
email = input("Informe o e-mail do jogador: ")
dados = dados + nome + "," + email + "\n"

arquivo = open("dados.game", "w")
arquivo.write(dados)
arquivo.close()

pygame.init()

D = pygame.display.set_mode((600,500),0,32)
pygame.display.set_caption('Atire no bloco Azul!')
icone = pygame.image.load("assets/nave.png")
pygame.display.set_icon(icone)

W =(255,255,255)
R=(255,0,0)
B=(0,0,255)
G=(0,255,0)
S=(100,100,100)
BL=(0,0,0)
E=(255,100,100)
C=R

i=0
pos_x=300
pos_y=200
pos_speed=1
shoot_x=305
shoot_y=205
shoot_speed=1
shoot=False
direc="right"
shoot_direc="right"
tar_dead=True
pause=False
isdie=False
tar_range=20
(a,b,c,d,e,f)=(0,0,0,0,0,0)

font = pygame.font.SysFont('Calibri', 50, True, False)
fonty = pygame.font.SysFont('Calibri', 20, True, False)
start = font.render("Começar",True,G)
endr = font.render("Morreu",True,R)
endw = font.render("Morreu",True,W)
esc = fonty.render("Pressione Esc para Pausar e 2 para Despausar",True,S)
restart = fonty.render("Pressione Tab para Recomecar",True,S)
clock = pygame.time.Clock()

D.fill(W)
pygame.draw.rect(D,R,[-1,-1,601,401],4)

while True:
	
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                elif event.type == KEYDOWN:
                        user=pygame.key.get_pressed()
                        if event.key == K_ESCAPE:
                                if pause or isdie:
                                        pygame.quit()
                                        sys.exit()
                                else:
                                        pause=True
                        else:
                                pause=False
                                if event.key == K_RIGHT and not(direc=="left"):
                                        direc="right"
                                elif event.key == K_LEFT and not(direc=="right"):
                                        direc="left"
                                elif event.key == K_UP and not(direc=="down"):
                                        direc="up"
                                elif event.key == K_DOWN and not(direc=="up"):
                                        direc="down"
                                elif event.key == K_SPACE:
                                        if shoot==False:
                                            shoot_speed=2
                                            shoot_direc=direc
                                            shoot=True
                                elif event.key == K_TAB:
                                        pos_x=300
                                        pos_y=200
                                        shoot_x=305
                                        shoot_y=205
                                        shoot_speed=5
                                        shoot=False
                                        direc="right"
                                        shoot_direc="right"
                                        tar_dead=True
                                        pygame.draw.rect(D,W,[0,0,600,500])
                                        continue
                                        
        if pause==False:
                if tar_dead==True:
                        target_x=random.randint(20,540)
                        target_y=random.randint(20,340)
                        tar_dead=False

                if tar_dead==False:
                        pygame.draw.rect(D,B,[target_x,target_y,20,20])
                        if (shoot_x+5<=target_x+20 and shoot_y+5<=target_y+20 and shoot_x+5>=target_x and shoot_y+5>=target_y):
                            pygame.draw.rect(D,W,[target_x,target_y,40,40])
                            shoot_speed=200
                            shoot==False
                            tar_dead=True
                    
                if pos_x<=0 or pos_x>=580 or pos_y<=0 or pos_y>=380 or (pos_x<=target_x+tar_range and pos_y<=target_y+tar_range and pos_x>=target_x-tar_range and pos_y>=target_y-tar_range):
                        isdie=True
                        if i%80<40:
                                pygame.draw.rect(D,E,[0,0,600,400])
                                D.blit(endw, [250, 180])
                                i+=1
							
                        else:
                                pygame.draw.rect(D,W,[0,0,600,410])
                                D.blit(endr, [250, 180])
                                i+=1
                        
                else:
                        pygame.draw.rect(D,W,[shoot_x+5,shoot_y+5,10,10])
                        pygame.draw.rect(D,W,[pos_x,pos_y,20,20])
                        pygame.draw.polygon(D,W,[(pos_x+a,pos_y+b),(pos_x+c,pos_y+d),(pos_x+e,pos_y+f)])

                        if direc=="right":
                                pos_x+=pos_speed
                                (a,b,c,d,e,f)=(20,0,30,10,20,20)
                        elif direc=="left":
                                pos_x-=pos_speed
                                (a,b,c,d,e,f)=(-10,10,0,0,0,20)
                        elif direc=="up":
                                pos_y-=pos_speed
                                (a,b,c,d,e,f)=(0,0,10,-10,20,0)
                        elif direc=="down":
                                pos_y+=pos_speed
                                (a,b,c,d,e,f)=(0,20,10,30,20,20)

                        if shoot==True:
                            C=B
                            if shoot_direc=="right":
                                    shoot_x+=shoot_speed
                                    
                            elif shoot_direc=="left":
                                    shoot_x-=shoot_speed
                                    
                            elif shoot_direc=="up":
                                    shoot_y-=shoot_speed
                                    
                            elif shoot_direc=="down":
                                    shoot_y+=shoot_speed
                                    
                            if shoot_x<=0 or shoot_x>=590 or shoot_y<=0 or shoot_y>=390:
                                    shoot=False
                        else:
                            C=R
                            shoot_x=pos_x
                            shoot_y=pos_y   


                        pygame.draw.rect(D,R,[shoot_x+5,shoot_y+5,10,10])
                        pygame.draw.rect(D,G,[pos_x,pos_y,20,20])
                        pygame.draw.rect(D,C,[pos_x+5,pos_y+5,10,10])
                        pygame.draw.polygon(D,G,[(pos_x+a,pos_y+b),(pos_x+c,pos_y+d),(pos_x+e,pos_y+f)])
                        pygame.draw.rect(D,R,[-1,0,601,401],4)
                        D.blit(esc, [200, 420])
                        D.blit(restart, [200, 460])
                
                        
        pygame.display.update()
        clock.tick(150)