# Children's activity board script v1.2
# August 6, 2020
# By Justin Manzo
# Reads buttons and switches only - two modes of sounds for switch up or down
# Uses event handlers for each button press

import time
import pygame.mixer
from pygame.mixer import Sound
from pygame.mixer import music
from gpiozero import Button

#https://gpiozero.readthedocs.io/en/stable/recipes.html#gpio-music-box

pygame.mixer.init()

button={}
button[0] = Button(5, bounce_time=0.05)
button[1] = Button(6, bounce_time=0.05)
button[2] = Button(13, bounce_time=0.05)
button[3] = Button(19, bounce_time=0.05)
button[4] = Button(26, bounce_time=0.05)
button[5] = Button(21, bounce_time=0.05, hold_time=.5)
button[6] = Button(20, bounce_time=0.05, hold_time=.5)
button[7] = Button(16, bounce_time=0.05, hold_time=.5)
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


def but_pushA():
    a=button[5].is_pressed
    music.load(buttonsound[0,a])
    music.play()
    
def but_pushB():
    a=button[5].is_pressed
    music.load(buttonsound[1,a])
    music.play()
    
def but_pushC():
    a=button[5].is_pressed
    music.load(buttonsound[2,a])
    music.play()

def but_pushD():
    a=button[5].is_pressed
    music.load(buttonsound[3,a])
    music.play()

def but_pushE():
    a=button[5].is_pressed
    music.load(buttonsound[4,a])
    music.play()

button[0].when_pressed=but_pushA
button[1].when_pressed=but_pushB
button[2].when_pressed=but_pushC
button[3].when_pressed=but_pushD
button[4].when_pressed=but_pushE



def main():
    while True:
        pass

if __name__ == "__main__":
    main()