# This file was created by Jude Hammers

# Works Cited
# https://www.youtube.com/@CodingWithRuss/videos
# https://www.pygame.org
# https://chat.openai.com/

import pygame
import sys
import webbrowser

# Initialize Pygame
pygame.init()

# Set up the game screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
# These coordinates set the limit of the game screen.
# The height is more than the width to replicate a bowling alley lane
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bowl-O-Rama")
# These functions connect the coordinates with the actual game screen,
# and give the bowling game the name of "bowl-o-rama", which is seen at the top of the game

# Load and scale the background image
background_image = pygame.image.load("woodfloor.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# this sets the frame rate clock for the game. i set the fps to 60 down below. without this function, you cannot set the fps.
# by having fps set at 60 it creates a smooth running game, espcially for the bowling ball so it rolls instead of moving one block at a time
clock = pygame.time.Clock()

# this sets the starting osition and speed of the player (bowling ball). if the user does not interact with the space bar, the player will not move.
player = [200, 700, 35]
player_velocity = [0, 0]

# this is a mob class for the pins in the game. they load into the game using a file image and are drawn using the screen blit function
class Mob:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
# draws in pins
    def draw(self):
        screen.blit(self.image, self.rect.topleft)

# this defines the mob as the mob class and gives it the coordinate restrictions so it has a size fitting for the game
mob = Mob(100, 50, "pins2.png")

# this allows the strike text to display. it is similar to the turle text from RPS but with pygame instead.
font = pygame.font.Font(None, 70)

# this makes sure that the YT link is only opened once, since after the ball initially collides it continues to collide opening tons of links. 
# with this function it prevents the link from being opened multiple times even if the collision continues
link_opened = False
strike_time = 0
# this makes sure the strike! is displayed as soon as a collision occurs and before the link opens

# main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # the space bar is used to push the ball forward,
            # and each space bar click increases the ball speed
            player_velocity[1] -= 2 

    # this allows the ball (player) to move forward
    # by updating the player's position to it correlates with the speed
    player[0] += player_velocity[0]
    player[1] += player_velocity[1]

    # this draws the woodfloor background
    screen.blit(background_image, (0, 0))
    
    # this draws the player circle in (255 = blue)
    pygame.draw.circle(screen, (0, 0, 255), (int(player[0]), int(player[1])), player[2])
    
    # this draws the mob into the game
    mob.draw()

    # this displays "Strike!" text after the collision
    if mob.rect.colliderect(pygame.Rect(player[0] - player[2], player[1] - player[2], player[2] * 2, player[2] * 2)):
        # Display "Strike!" text
        text_surface = font.render("Strike!", True, (0, 0, 255))
        screen.blit(text_surface, (125, 400))
        if not link_opened:
            # Record the time when "Strike!" is displayed
            strike_time = pygame.time.get_ticks()
            link_opened = True

    # this opens the link after a delay of three seconds so that it doesnt overlap the strike message
    current_time = pygame.time.get_ticks()
    if link_opened and current_time - strike_time >= 3000:
        webbrowser.open("https://www.youtube.com/watch?v=xrdYpzsgp4o")
        link_opened = False
    # updates the display and set the frame rate so that the game runs smoothly and the ball doesnt have a movement history behind it
    pygame.display.flip()
    clock.tick(60)

# quit pygame and exit code
pygame.quit()
sys.exit()