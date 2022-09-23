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

