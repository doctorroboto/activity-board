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

buttonsound = [ ['rooster.mp3','quack.mp3','pig-oink.mp3','Smallherdcattle.mp3'],
                ['carstartgarage.mp3','carpeelout.mp3','carstart.mp3','Sad_Trombone.mp3'],
                ['phonedial.mp3','emergency003.mp3','Air_Wrench.mp3','steam-train-whistle.mp3'],
                ['spacetakeoff.mp3','spacestartup.mp3','spacefailure.mp3','Airlock-Door-Open-B2.mp3'] ]


buttoncat=['farmsounds.mp3','carsounds.mp3','machinesounds.mp3']

cycle=0

def but_pushA():
    global cycle
    if button[5].is_pressed:
        a=3
    else:
        a=cycle
    print(a)
    music.load(buttonsound[a][0])
    music.play()
    
def but_pushB():
    global cycle
    if button[5].is_pressed:
        a=3
    else:
        a=cycle
    music.load(buttonsound[a][1])
    music.play()
    
def but_pushC():
    global cycle
    if button[5].is_pressed:
        a=3
    else:
        a=cycle
    music.load(buttonsound[a][2])
    music.play()

def but_pushD():
    global cycle
    if button[5].is_pressed:
        a=3
    else:
        a=cycle
    music.load(buttonsound[a][3])
    music.play()

def but_pushE():
    #a=button[5].is_pressed
    #music.load(buttonsound[4,a])
    #music.play()
    global cycle
    cycle+=1
    if cycle==3:
        cycle=0
    print(buttoncat[cycle])

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
