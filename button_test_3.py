# Children's activity board script v1.1
# July 25, 2020
# By Justin Manzo
# Reads buttons and switches only - two modes of sounds for switch up or down

import time
import pygame.mixer
from pygame.mixer import Sound
from pygame.mixer import music
from gpiozero import Button

#https://gpiozero.readthedocs.io/en/stable/recipes.html#gpio-music-box

pygame.mixer.init()

button ={}
button[0] = Button(5, pull_up=True, bounce_time=0.01, hold_time=.5)
button[1] = Button(6,pull_up=True, bounce_time=0.01, hold_time=.5)
button[2] = Button(13,pull_up=True, bounce_time=0.01, hold_time=.5)
button[3] = Button(19,pull_up=True, bounce_time=0.01, hold_time=.5)
button[4] = Button(26,pull_up=True, bounce_time=0.01, hold_time=.5)
button[5] = Button(21,pull_up=True, bounce_time=0.01, hold_time=.5)
button[6] = Button(20,pull_up=True, bounce_time=0.01, hold_time=.5)
button[7] = Button(16,pull_up=True, bounce_time=0.01, hold_time=.5)
buttonlist = ["Blue", "Red", "Yellow", "Green", "White", "Switch", "Unused1", "Unused2"]

buttonsound={}

buttonsound[0,0]='rooster.mp3'
buttonsound[1,0]='carstartgarage.mp3'
buttonsound[2,0]='phonedial.mp3'
buttonsound[3,0]='carpeelout.mp3'
buttonsound[4,0]='carstart.mp3'

buttonsound[0,1]='spacetakeoff.mp3'
buttonsound[1,1]='spacestartup.mp3'
buttonsound[2,1]='spacefailure.mp3'
buttonsound[3,1]='spacetakeoff.mp3'
buttonsound[4,1]='emergency003.mp3'


def main():
    while True:
        for x in range(0,5):
            if (button[x].value==1):
                print(f"{buttonlist[x]} button pressed. Held: {button[x].is_held}")
                music.load(buttonsound[x,button[5].value])
                music.play()
                #while music.get_busy()==True:
                 #  continue
                while button[x].value==1:
                    continue
        time.sleep(.05)

if __name__ == "__main__":
    main()