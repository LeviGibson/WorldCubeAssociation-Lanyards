import subprocess
import PIL
from PIL import Image, ImageChops
from os.path import exists
import glob
import numpy as np

from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

COMPCARD_SCALE_FACTOR = .85

if not exists("compcards/cards.pdf"):
    raise Exception("compcards/cards.pdf Not Found. Please download groupifier competitor card PDF to compcards/cards.pdf")

subprocess.call("rm -f compcards/*.png", shell=True)
subprocess.call("rm -f compcards/individual/*.png", shell=True)

images = convert_from_path('compcards/cards.pdf')

filenames = []

for i, image in enumerate(images):
    fname = "compcards/page-" + str(i) + ".png"
    filenames.append(fname)
    image.save(fname, "PNG")


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

def add_padding(im):
    bg = Image.open("background_competitor.png")
    bgsize = bg.size
    bg = Image.new('RGB', bgsize, (255, 255, 255))
    ratio = min((bgsize[0])/im.size[0], (bgsize[1])/im.size[1])
    im = im.resize((int(im.size[0]*ratio*COMPCARD_SCALE_FACTOR), int(im.size[1]*ratio*COMPCARD_SCALE_FACTOR)))

    loc = ((bg.size[0] - im.size[0])//2, (bg.size[1] - im.size[1])//2)
    bg.paste(im, loc)
    return bg

def run():
    for pageid, pagename in enumerate(filenames):
        page = Image.open(pagename)
        page = crop_to_edges(page)
        width, height = page.size
        for y in range(4):
            for x in range(3):
                card = page.crop(((width/3)*x, (height/4)*y, (width/3)*(x+1), (height/4)*(y+1)))
                card = trim_card(card)
                card = add_padding(card)

                #Don't save card if it's blank.
                if np.min(np.asarray(card)) < 200:
                    card.save("compcards/individual/{}.png".format("{0:0=4d}".format(x + y*3 + (3*4*pageid))))

if __name__ == "__main__":
    run()
