import subprocess
import PIL
from PIL import Image, ImageChops
from os.path import exists
import glob
import numpy as np

subprocess.call("rm -f compcards/*.png", shell=True)
subprocess.call("rm -f compcards/individual/*.png", shell=True)
subprocess.call("cd compcards && pdftoppm cards.pdf page -png && cd ..", shell=True)
    

filenames = glob.glob("compcards/*.png")
filenames.sort()

crop = None

def crop_to_edges(img):
    global crop
    if crop is None:
        pixels = np.asarray(img)
        crop = [20, 25, pixels.shape[1]-20, 0]
        for i in range(pixels.shape[0]):
            i = pixels.shape[0] - 1 - i
            if np.min(pixels[i]) < 100:
                crop[3] = i
                break
        crop[0] -= 5
        crop[1] -= 5
        crop[2] += 5
        crop[3] += 5
    
    img = img.crop(tuple(crop))

    return img

#taken from StackOverflow :)
def trim_card(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    return im.crop(bbox)

def run():
    for pageid, pagename in enumerate(filenames):
        page = Image.open(pagename)
        page = crop_to_edges(page)
        width, height = page.size
        for y in range(4):
            for x in range(3):
                card = page.crop(((width/3)*x, (height/4)*y, (width/3)*(x+1), (height/4)*(y+1)))
                card = trim_card(card)
                card.save("compcards/individual/{}.png".format("{0:0=4d}".format(x + y*3 + (3*4*pageid))))

if __name__ == "__main__":
    run()
