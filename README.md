# Installing Dependencies
### if using python3:
`pip3 install pillow pdf2image`
### if using python2:
`pip install pillow pdf2image`

# Setting up the script

The first thing  you need to do is download your competitor card PDF, and move it to the folder labeled `compcards` with the filename `cards.pdf`.
This pdf can be downloaded from groupifier. This must be an 8.5x11 pdf. support for A4 will hopefully come soon :).


Next you can go to the registration tab of your competition and download a CSV file containing the names of all your registered competitors. Select all and click `Export To CSV`.
Move this to this folder and rename it to `names.csv`

![Alt text](images/Screenshot from 2022-09-23 09-59-43.png?raw=true "Title")
Now the these files should exist:

`names.csv`

`compcards/cards.pdf`

# Running the script

Run the main.py file with `python3 ./main.py -name "Cubing in Boston 2022"`.  
After the script is finished running, there should be many PNG files in the `pngs` folder. 

Print them out double sided, cut them, and you have some ready-to-use lanyard inserts! Enjoy!

# Customising the Lanyards

By default, the lanyards look like this
![Alt text](images/Standard Card.png?raw=true "Title")

The pronouns are taken from the competitor's gender, and genders other than male/female are marked as they/them.

You can also make the program display the person's role (Competitor, Staff, Organizer, Delegate) instead of their pronouns by editing the `names.csv` file like so:
![Alt text](images/roles.png?raw=true "Title")

You can also remove the subtext entirely by running main.py with the `-nosubtext` flag.

You can also replace `logo1.png` and `logo2.png` with whatever logos you want, or you can delete them entirely. 
This program uses TheCubicle logo and the WCA logo as a defualt.
You can also change the size of the logos with the -logosize flag like this:

`python3 ./main.py -name "Cubing In Boston 2022" -logosize 200`
