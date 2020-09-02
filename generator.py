import sys
import pygame as pg
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from HashGen import *
import os

pg.init()
FONT = pg.font.Font('mont.otf', 20)
columns = dataset.columns.tolist()

class Text(pg.sprite.Sprite):

    def __init__(self, text, pos, color, *groups):
        super().__init__(*groups)
        self.image = FONT.render(text, True, color)
        self.rect = self.image.get_rect(center=pos)


def generateImages(to_draw):
    details=dataset.iloc[:,:].values
    for detail in details:
        i=0
        img = Image.open("certificate.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("mont.otf", size = 80)
        for text in to_draw:        
            if(columns[i]=='Hash'):                
                font = ImageFont.truetype("mont.otf", size = 50)
                detail[i]=f'Certificate ID : {detail[i]}'
            draw.text( (text.rect.left*4,text.rect.top*4), detail[i], (0,0,0), font, align='center')
            i+=1
        img.save( f'certificates/{detail[3]}.pdf', "pdf", resolution=100.0)
    


img = Image.open("certificate.jpg")
image = pg.image.load(r'certificate.jpg') 
width, height = img.size
dim = (width//4,height//4)
image = pg.transform.scale(image, dim)
screen = pg.display.set_mode(dim) 

clock = pg.time.Clock()
text_group = []
i = 0
for column in columns[0:len(columns)-1]:
    text_group.append(Text(column, (100, 100+i), pg.Color('black')))
    i+=100;

all_sprites = pg.sprite.Group(text_group)
selected = None
done = False

while not done:
    
     
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            for sprite in all_sprites:
                if sprite.rect.collidepoint(event.pos):
                    selected = sprite
                    break
        elif event.type == pg.MOUSEBUTTONUP:
            selected = None
        elif event.type == pg.MOUSEMOTION:
            if selected:
                selected.rect.center = event.pos
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                done = True


            if event.key == pg.K_RETURN:
                generateImages(all_sprites)
                done=True

    all_sprites.update()
    screen.fill((0,0,0)) 
    screen.blit(image, (0, 0))
    all_sprites.draw(screen)

    pg.display.flip()
    clock.tick(30)


pg.quit()