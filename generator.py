import sys
import pygame as pg
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from HashGen import *
import os
import zipfile



pg.init()
FONT = pg.font.Font('mont.otf', 20)
FONT1 = pg.font.Font('mont.otf', 12)
columns = dataset.columns.tolist()[:-1]


class Text(pg.sprite.Sprite):

    def __init__(self, text, pos, color, font, *groups):
        super().__init__(*groups)
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect(center=pos)


def generateImages(to_draw):
    
    if not os.path.exists(f'certificates/{event_name}/{year}'):
        os.makedirs(f'certificates/{event_name}/{year}')
    details=dataset.iloc[:,:].values
    j=0
    for detail in details:
        i=0
        img = Image.open("certificate.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("mont.otf", size = 80)
        for text in to_draw:        
            if(columns[i]=='Certificate ID' or columns[i]=='Date'):                
                font = ImageFont.truetype("mont.otf", size = 50)
                detail[i]=f'{columns[i]} : {detail[i]}'
            draw.text( (text.rect.left*4,text.rect.top*4), detail[i], (0,0,0), font, align='center')
            i+=1
        img.save(f'certificates/{event_name}/{year}/{dataset["Filename"][j]}', "pdf", resolution=100.0)
        
        dataset.to_csv(f'certificates/{event_name}/{year}/{event_name}_{year}.csv',index=False)
        j+=1
     
    zip()


def zip():

    zipf = zipfile.ZipFile(f'{event_name}_{year}.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(f'certificates/{event_name}/{year}/', zipf)
    zipf.close()

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            if '.zip' in file or '.csv' in file:
                continue
            ziph.write(os.path.join(root, file), file)

    
        


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
    if column == 'Certificate ID' or column == 'Date':
        text_group.append(Text(column, (100, 100+i), pg.Color('black'), FONT1))
    else:
        text_group.append(Text(column, (100, 100+i), pg.Color('black'), FONT))
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

print("Certificates generated successfully!")