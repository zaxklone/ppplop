#! /usr/bin/python

#Image placeholder generator
#MIT LICENSE

from PIL import Image
from random import randint


def create_image(dimx = 520, dimy =520, x=20 ,y=20, bg = 'rgb(155,0,0)' ):
   
    image = Image.new('RGB',(dimx,dimy), bg )
    
    for stepx in range(0,dimx,x):
        for stepy in range(0,dimy,y):
            str_rgb = "rgb({0},{1},{2})".format(randint(0,255), randint(0,255), randint(0,255))
            image.paste(Image.new('RGB', (x,y), str_rgb), (stepx,stepy))  
    return image

def main():
    im = create_image()
    im.save('ppplop.png', optimize=True)

if __name__ == '__main__':
    main()
