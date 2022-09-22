import PIL
from PIL import Image
import glob
import subprocess

subprocess.call("rm -f pngs/*.png", shell=True)

inserts = glob.glob("inserts/*.png")
cards = glob.glob("compcards/individual/*.png")
inserts.sort(), cards.sort()

cards = cards[0:len(inserts)]

cardsDone = 0
canvasesDone = 0

def filename(num):
    num = str(num)
    for i in range(4-len(num)):
        num = '0' + num

    return num + '.png'

def get_card_image(cardsDone):
    card = Image.open(cards[cardsDone])
    ratio = min((3370/2)/card.size[0], (2125/2)/card.size[1])
    card = card.resize((int(card.size[0]*ratio), int(card.size[1]*ratio)))
    return card

def run():
    global cardsDone, canvasesDone

    while cardsDone < len(inserts):
        cardcanvas = Image.new('RGB', (int(8.5*500), 11*500), (255, 255, 255))
        insertcanvas = Image.new('RGB', (int(8.5*500), 11*500), (0, 0, 0))

        for x in range(2):
            for y in range(5):
                card = Image.open(inserts[cardsDone])
                card = card.resize((3370//2, 2125//2))
                insertcanvas.paste(card, (x*(3390//2), y*(2140//2)))

                card = get_card_image(cardsDone)
                cardcanvas.paste(card, (x*(3390//2), y*(2140//2)))

                cardsDone+=1
        
        cardcanvas.save("pngs/cards-{}.png".format(canvasesDone))
        insertcanvas.save("pngs/inserts-{}.png".format(canvasesDone))
        print("Page {} saved".format(canvasesDone))
        canvasesDone+=1

if __name__ == "__main__":
    run()
