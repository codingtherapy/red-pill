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

WHITE = (255, 255, 255)
GREY1 = (220, 220, 220)
GREY2 = (192, 192, 192)
GREY3 = (128, 128, 128)
GREY4 = (30, 30, 30)


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

def corridor(p):
    return (p[0]>=0 and p[0] <= 201 and p[1]>=99 and p[1]<=201) or (p[0]>=199 and p[0]<=301 and p[1]>=99 and p[1]<=401)

def in_corridor(polygon):
    return all([corridor(p) for p in polygon])

def show_sofa():
    screen = pygame.display.set_mode((400, 400), 0, 32)
    screen.fill(GREY1)

    corridor = [[0, 100], [300, 100], [300, 400], [200, 400], [200, 200], [0, 200]]
    sofa = [[120, 100], [220, 120], [260, 140], [280, 190], [270, 260], [240, 290], [230, 220], [220, 180], [150, 180], [90, 180]]
    pygame.draw.polygon(screen, GREY2, corridor)
    pygame.draw.polygon(screen, WHITE, sofa)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.lock()
        sofa = move(sofa, 1, 1)
        screen.fill(GREY1)
        pygame.draw.polygon(screen, GREY2, corridor)
        pygame.draw.polygon(screen, WHITE, sofa)
        screen.unlock()
        pygame.time.wait(100)
        pygame.display.update()

if __name__ == '__main__':
    show_sofa()
