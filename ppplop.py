#! /usr/bin/python

#Image placeholder generator
#MIT LICENSE
import argparse 
from PIL import Image
from random import randint




def create_image(dimx = 520, dimy =520, x=20 ,y=20,name= 'ppplop.png', bg = 'rgb(155,0,0)' ):
    image = Image.new('RGB',(dimx,dimy), bg )
    for stepx in range(0,dimx,x):
        for stepy in range(0,dimy,y):
            str_rgb = "rgb({0},{1},{2})".format(randint(0,255), randint(0,255), randint(0,255))
            image.paste(Image.new('RGB', (x,y), str_rgb), (stepx,stepy))  
    try:
        image.save(name, optimize=True)
        return True
    except:
        return False


def main():
    parser = argparse.ArgumentParser(
                       description="Create Colorful Image Placeholders")
    parser.add_argument("-n", "--name", 
                       help='''Name given to image file that is created stored as 
                               a png e.g `ppplop -n COW` will save a COW.png in 
                               working directory ''')
    
    args = parser.parse_args()
    

    if args.name:
        im_name = args.name
        #setting up a translation table so that filename do not contain certain characters
        trans_tuple = (None,'''!@$%^&*{}:;"'\/.,''')
        im_name = im_name.translate(trans_tuple[0], trans_tuple[1])
        
        im_name = '{0}.png'.format(im_name)  
        
        im = create_image( name=im_name)
        print 'Success'
if __name__ == '__main__':
    main()
