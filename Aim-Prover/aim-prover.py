import pygame
from sys import exit
import time
import numpy 

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("aim-prover")
cl=pygame.time.Clock()
textfont = pygame.font.Font(None,50)

# music
sound_file = 'hit.wav'
hit_sound=pygame.mixer.Sound(sound_file)

target=pygame.Surface((15,15))
target.fill('pink')
bg=pygame.image.load("bg.jpg")
welcome= textfont.render("Aim~Prover",True,'khaki2')


score = 0


# mouse click 
def targetPix(l,w):
    l_o_tups=[]
    for i in range(l,l+15):
        for j in range(w,w+15,1):
            l_o_tups.append((i,j))
    # print(l_o_tups)         
    return l_o_tups        




while True :
    # game bg 
    screen.blit(bg,(0,0))
    # gamme title
    screen.blit(welcome,(310,25))
    # score display
    scoretxt=textfont.render(str(score),True,'lightcoral')
    screen.blit(scoretxt,(398,55))
    
    # AIM TARGET
    ts_lc = numpy.random.random_integers(0,760)
    ts_hc = numpy.random.random_integers(80,460)
    screen.blit(target,(ts_lc,ts_hc))
    
    pygame.display.update()  

     
    # modify tick n sleep values for easy or difficulty level. 
    cl.tick(2)
    time.sleep(0.8)




     
    for e in pygame.event.get():
        print(e)
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
                
               if pygame.mouse.get_pressed():
                    if e.button == 1:
                        possibles = targetPix(ts_lc,ts_hc)
                        pos = pygame.mouse.get_pos()
                        print(pos)
                        if pos in possibles:
                            hit_sound.play()
                            score += 1
                              
                    print(score)

            
