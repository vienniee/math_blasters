#import libraries
import pygame


#start pygame
pygame.init()

#create display window
SCREEN_HEIGHT = 600    
SCREEN_WIDTH = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Background
background = pygame.image.load('image\level_select.png').convert()

#logo - icon made by Freepik from www.flaticon.com
pygame.display.set_caption("MathBlasters!")
icon = pygame.image.load('Image\mathblasters.png')
pygame.display.set_icon(icon)

#score text
passScore = 6
quizScore = 8
font = pygame.font.Font('freesansbold.ttf', 42)
resultFont = pygame.font.Font('freesansbold.ttf', 58)
scoreTextX = 390
scoreTextY = 275
resultTextX = 340
resultTextY = 200


def showResults(x, y, passQuiz):
    scoreText = font.render("SCORE : "+ str(quizScore), True, (0, 0, 0))
    screen.blit(scoreText, (x, y))
    if passQuiz:
        resultText = resultFont.render("YOU WIN!", True, (0, 0, 0))
        screen.blit(resultText, (resultTextX, resultTextY))
    elif not passQuiz:
        resultText = resultFont.render("YOU LOSE!", True, (0, 0, 0))
        screen.blit(resultText, (resultTextX-10, resultTextY))

#TODO: continue button






#game runner
running = True
while running:
    screen.fill((202, 228, 241))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    if (quizScore>=passScore):
        showResults(scoreTextX,scoreTextY,True)
    else:
        showResults(scoreTextX,scoreTextY,False)
    
    pygame.display.update()