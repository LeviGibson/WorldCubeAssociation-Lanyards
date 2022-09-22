import PIL
from PIL import Image, ImageDraw, ImageFont
import random
import subprocess
from os.path import exists
import argparse

subprocess.call("rm -f inserts/*.png", shell=True)
LOGO_SIZE = 256
SUBTEXT = True

#taken from Stack Overflow
def sort_names(tup):
 
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    tup.sort(key = lambda x: x[0])
    return tup

def read_names_from_csv():
    infile = open("names.csv")
    #read the header
    infile.readline()
    
    names = []
    for line in infile:
        line = line.split(',')
        names.append((line[1], line[0], line[5]))

    names.sort()

    infile.close()
    return names

names = read_names_from_csv()

def color_ramp():
    return (0, 0, random.randint(0, 255))

def make_background(COMPETITION_NAME):
    COMPETITION_NAME_FONT = ImageFont.truetype('RubikMonoOne-Regular.ttf', size=(1200)//len(COMPETITION_NAME))

    background = Image.open("background_competitor.png")
    I1 = ImageDraw.Draw(background)
    I1.text((background.size[0]/2, background.size[1]/6), COMPETITION_NAME, fill=(255, 255, 255), font=COMPETITION_NAME_FONT, anchor='mm')

    if exists("logo1.png"):
        logo = Image.open("logo1.png")
        logo = logo.resize((LOGO_SIZE, LOGO_SIZE))
        background.paste(logo, (background.size[0]//10 - logo.size[0]//2, background.size[1]//6 - logo.size[0]//2), logo)

    if exists("logo2.png"):
        logo = Image.open("logo2.png")
        logo = logo.resize((LOGO_SIZE, LOGO_SIZE))
        background.paste(logo, (background.size[0]-(background.size[0]//10) - logo.size[0]//2, background.size[1]//6 - logo.size[0]//2), logo)

    return background

def get_subetext(competitor):
    if SUBTEXT:
        if competitor[1] == "CMP": return "Competitor"
        if competitor[1] == "STF": return "Staff"
        if competitor[1] == "DEL": return "Delegate"
        if competitor[1] == "ORG": return "Organizer"
        if competitor[2] == 'm': return "he/him"
        if competitor[2] == 'f': return "she/her"
        if competitor[2] == '0': return "they/them"
    return ""

SUBTEXT_FONT = ImageFont.truetype('RubikMonoOne-Regular.ttf', size=(80))

def run(COMPETITION_NAME):
    background = make_background(COMPETITION_NAME)

    for i, competitor in enumerate(names):
        image = background.copy()
        font = ImageFont.truetype('RubikMonoOne-Regular.ttf', size=(1800 // len(competitor[0])))

        I1 = ImageDraw.Draw(image)
        I1.text((image.size[0]//2, image.size[1]//2), competitor[0], fill=(255, 255, 255), font=font, anchor='mm')
        I1.text((image.size[0]//2, image.size[1]-(image.size[1]//6)), get_subetext(competitor), fill=(255, 255, 255), font=SUBTEXT_FONT, anchor='mm')

        image.save("inserts/{}.png".format("{0:0=4d}".format(i)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate double-sided lanyard inserts for WCA competitions')
    parser.add_argument('-name', help="Name of the competition.", default="Genaric Competition 2054")
    parser.add_argument('-logosize', type=int, help="Size in pixels of the logos to the left and right of the Competition Name. Default 256")
    parser.add_argument('-nosubtext', help="Don't add subtext under Competitor Name (Pronouns / Roles)")
    parser.add_argument('-subtextsize', type=int, help="Size of subtext (Default 8-)")
    args = parser.parse_args()

    if args.logosize:
        LOGO_SIZE = int(args.logosize)
    if args.nosubtext:
        SUBTEXT = False
    if args.subtextsize:
        SUBTEXT_FONT = ImageFont.truetype('RubikMonoOne-Regular.ttf', size=(args.subtextsize))
        
    run(args.name)
