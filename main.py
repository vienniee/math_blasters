#LINKING OF PAGES (from world selection onwards)
#for pages that need trasnfer of parameters/data
import pygame, sys
from pygame.locals import *
import levelselect
import Game
import results
import subject_chapter_selection
#subject = worldselect()
#topic =world.levelselect(subject)
#level = levelselect.levelselect(topic)
#score = minigame.score(topic, level)
#results.storescore(subject, topic, level,score)

subject_chapter_selection.subject_Chapter_selection()
level = levelselect.levelselect('algebra')
score = Game.Game('algebra',level)
results.results('maths','algebra',level,score)

