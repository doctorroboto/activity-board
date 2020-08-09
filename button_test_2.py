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
button[0] = Button(5, pull_up=True, bounce_time=0.05, hold_time=.05)
button[1] = Button(6,pull_up=True)
button[2] = Button(13,pull_up=True)
button[3] = Button(19,pull_up=True)
button[4] = Button(26,pull_up=True)
button[5] = Button(21,pull_up=True)
button[6] = Button(20,pull_up=True)
button[7] = Button(16,pull_up=True)
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


while True:
    #if cap[1].value
#    for x in range(0,1):
#        is_touched[x] = cap[x+1].value
 #       if (is_touched[x] != was_touched[x]):
  #          if is_touched[x]:
   #             print("Something pressed!")
    #        else:
     #           print("Something released!")
      #  was_touched[x]=is_touched[x]
       # time.sleep(0.05)
    for x in range(0,5):   
        if (button[x].value==1):
            print("%s button pressed",buttonlist[x])
            music.load(buttonsound[x,button[5].value])
            music.play()
            #while music.get_busy()==True:
             #   continue
    time.sleep(.1)