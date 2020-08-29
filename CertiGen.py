# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 19:13:26 2019

@author: tanma
"""


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from HashGen import *
import pygame
import os

os.system('mkdir certificates')

'''
Please edit the filenames in the function below to change the fonts and the certificate file name
Play around by generating a single certificate and change the fonts accordingly

'''


def generateImages(to_draw):
    details=dataset.iloc[:,:].values
    for detail in details:
        i=0
        img = Image.open("certificate.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("mont.otf", size = 80)
        for rect in to_draw:        
            if(i==2):                
                font = ImageFont.truetype("mont.otf", size = 50)
                detail[i]=f'Certificate ID : {detail[i]}'
            draw.text( (rect.left*4,rect.top*4), detail[i], (0,0,0), font, align='center')
            i+=1
        img.save( f'certificates/{detail[3]}.pdf', "pdf", resolution=100.0)
    



pygame.init()


img = Image.open("certificate.jpg")
image = pygame.image.load(r'certificate.jpg') 
width, height = img.size
image = pygame.transform.scale(image,(width//4,height//4))
screen = pygame.display.set_mode((width//4,height//4)) 

clock = pygame.time.Clock()
  
running=True
draw_start=False
to_draw=[]
pos=None
mouse_pos=None
final_pos=None
# infinite loop 
columns = dataset.columns.tolist()
i = 0;
while running : 
  
    # completely fill the surface object 
    # with white colour 
    pygame.display.set_caption(columns[i]) 
    
    screen.fill((0,0,0)) 
    screen.blit(image, (0, 0)) 
    
  
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            running=False
        
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = mouse_pos
            draw_start = True
        if event.type == pygame.MOUSEBUTTONUP:
            final_pos = mouse_pos
            draw_start = False
            rect = pygame.Rect(pos,(final_pos[0]- pos[0], final_pos[1]-pos[1]))
            rect.normalize()
            to_draw+=[rect]
            i+=1
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


            if event.key == pygame.K_RETURN:
                generateImages(to_draw)
                running=False
                
            
            if event.key == pygame.K_BACKSPACE:
                to_draw.pop()

        
    screen.blit(image,(0,0))

    if draw_start:
        pygame.draw.rect(screen,(255,0,0), pygame.Rect(pos, (mouse_pos[0] - pos[0],mouse_pos[1]- pos[1])))
    for item in to_draw:
        pygame.draw.rect(screen,(0,255,0),item)
        # Draws the surface object to the screen.   
    clock.tick(30)
    pygame.display.update()  

pygame.quit()