import PIL
from PIL import Image
import glob
import subprocess

TOP_EDGE_PADDING = 60
SIDE_EDGE_PADDING = 400
PADDING_BETWEEN_CARDS = 10

subprocess.call("rm -f pngs/*.png", shell=True)

inserts = glob.glob("inserts/*.png")
cards = glob.glob("compcards/individual/*.png")
inserts.sort(), cards.sort()

cardsDone = 0
canvasesDone = 0


def get_card_image(cardsDone):
    card = Image.open(cards[cardsDone])
    ratio = min((3370/2)/card.size[0], (2125/2)/card.size[1])
    card = card.resize((int(card.size[0]*ratio), int(card.size[1]*ratio)))
    return card

def run():
    global cardsDone, canvasesDone

    while cardsDone < len(inserts):
        cardcanvas = Image.new('RGB', (int(8.5*500), 11*500), (255, 255, 255))
        insertcanvas = Image.new('RGB', (int(8.5*500), 11*500), (255, 255, 255))

        for x in range(2):
            for y in range(5):
                card = Image.open(inserts[cardsDone])
                card = card.resize((3370//2, 2125//2))
                insertcanvas.paste(card, (x*(3370//2 + PADDING_BETWEEN_CARDS) + SIDE_EDGE_PADDING, y*(2125//2 + PADDING_BETWEEN_CARDS) + TOP_EDGE_PADDING))

                card = get_card_image(cardsDone)
                cardcanvas.paste(card, ((1-x)*(3370//2 + PADDING_BETWEEN_CARDS) + SIDE_EDGE_PADDING, y*(2125//2 + PADDING_BETWEEN_CARDS) + TOP_EDGE_PADDING))

                cardsDone+=1
        
        cardcanvas.save("pngs/cards-{}.png".format(canvasesDone))
        insertcanvas.save("pngs/inserts-{}.png".format(canvasesDone))
        print("Page {} saved".format(canvasesDone))
        canvasesDone+=1

if __name__ == "__main__":
    run()
