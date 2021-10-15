#LINKING OF PAGES (from world selection onwards)
#for pages that need trasnfer of parameters/data

import pygame, sys
from pygame.locals import *

#subject = worldselect()
#topic =world.levelselect(subject)
#level = levelselect.levelselect(topic)
#score = minigame.score(topic, level)
#results.storescore(subject, topic, level,score)

import levelselect
level = levelselect.levelselect('algebra')
import Game
score = Game.Game('algebra',level)
import results
results.results('maths','algebra',level,score)

