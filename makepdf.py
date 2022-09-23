import PIL
from PIL import Image
import glob
import subprocess

PADDING_BETWEEN_CARDS = 20
PAGEWIDTH = int(8.5*500)
PAGEHEIGHT = int(11*500)

CARDWIDTH = 3370//2
CARDHEIGHT = 2125//2

def get_side_padding():
    fullsize = (CARDWIDTH*2) + (PADDING_BETWEEN_CARDS*1)
    padding = (PAGEWIDTH - fullsize)//2

    return padding

def get_top_padding():
    fullsize = CARDHEIGHT*5 + (PADDING_BETWEEN_CARDS*4)
    padding = (PAGEHEIGHT - fullsize)//2

    return padding

TOP_EDGE_PADDING = get_top_padding()
SIDE_EDGE_PADDING = get_side_padding()

subprocess.call("rm -f pngs/*.png", shell=True)

inserts = glob.glob("inserts/*.png")
cards = glob.glob("compcards/individual/*.png")
inserts.sort(), cards.sort()

cardsDone = 0
canvasesDone = 0


def run():
    global cardsDone, canvasesDone

    while cardsDone < len(inserts):
        cardcanvas = Image.new('RGB', (PAGEWIDTH, PAGEHEIGHT), (255, 255, 255))
        insertcanvas = Image.new('RGB', (PAGEWIDTH, PAGEHEIGHT), (255, 255, 255))

        for x in range(2):
            for y in range(5):
                card = Image.open(inserts[cardsDone])
                card = card.resize((CARDWIDTH, CARDHEIGHT))
                insertcanvas.paste(card, (x*(3370//2 + PADDING_BETWEEN_CARDS) + SIDE_EDGE_PADDING, y*(2125//2 + PADDING_BETWEEN_CARDS) + TOP_EDGE_PADDING))

                card = Image.open(cards[cardsDone])
                card = card.resize((CARDWIDTH, CARDHEIGHT))
                cardcanvas.paste(card, ((1-x)*(3370//2 + PADDING_BETWEEN_CARDS) + SIDE_EDGE_PADDING, y*(2125//2 + PADDING_BETWEEN_CARDS) + TOP_EDGE_PADDING))

                cardsDone+=1
        
        cardcanvas.save("pngs/cards-{}.png".format(canvasesDone))
        insertcanvas.save("pngs/inserts-{}.png".format(canvasesDone))
        print("Page {} saved".format(canvasesDone))
        canvasesDone+=1

if __name__ == "__main__":
    run()
