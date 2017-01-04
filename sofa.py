# some thoughts on "moving sofa problem"
# https://www.math.ucdavis.edu/~romik/movingsofa/
#
# The main idea is to apply genetic programming.
# First I generate initial closed polygon contained within "corridor".
# The figure is small enough to be rotated.
# Then I succesively modify segments of polygon such that figure is getting bigger and bigger and still can be moved around.

import time
import tkinter
import sys
import pygame

def move(polygon, x, y):
    return [(p[0]+x, p[1]+y) for p in polygon]

def rotate(polygon, x0, y0, alpha):
    return polygon

def demo_animation_tkinter():
    animation = tkinter.Tk()
    canvas = tkinter.Canvas(animation, width=800, height=600)
    canvas.pack()
    canvas.create_polygon(10, 10, 10, 10, 60, 50, 35, 35)
    for x in range(0, 140):
        canvas.move(1, 5, 0)
        animation.update()
        time.sleep(0.05)

def demo_animation_pygame():
    screen = pygame.display.set_mode((640,320), 0, 32)
    polygon = [[10, 10], [10, 10], [60, 50], [35, 35]]
    color = (255, 255, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.lock()
        pygame.draw.polygon(screen, color, polygon)
        screen.unlock()
        pygame.display.update()
