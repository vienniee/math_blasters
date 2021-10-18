
#LINKING OF PAGES (from world selection onwards)
#for pages that need trasnfer of parameters/data
import pygame, sys
from pygame.locals import *
import subject_chapter_selection
import levelselect
import Game
import results


#import subject_chapter_selection
#subject = worldselect()
#topic =world.levelselect(subject)
#level = levelselect.levelselect(topic)
#score = minigame.score(topic, level)
#results.storescore(subject, topic, level,score)


minigame = subject_chapter_selection.subject_Chapter_selection("male")
level = levelselect.levelselect() #'algebra'
score = Game.Game(minigame,level) #'algebra'
results.results(minigame,level,score)


        