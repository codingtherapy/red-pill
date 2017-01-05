# some thoughts on "moving sofa problem"
# https://www.math.ucdavis.edu/~romik/movingsofa/
#
# The main idea is to apply genetic programming.
# First I generate initial closed polygon contained within "corridor".
# The figure is small enough to be rotated.
# Then I succesively modify segments of polygon such that figure is getting bigger and bigger and still can be moved around.

import time
import sys
import random
import pygame

import tsp

WHITE = (255, 255, 255)
GREY1 = (220, 220, 220)
GREY2 = (192, 192, 192)
GREY3 = (128, 128, 128)
GREY4 = (30, 30, 30)

N = [[-1, -1], [-1,0], [-1, 1], [0, -1], [0,1], [1, -1], [1, 0], [1, 1]]

def move(polygon, x, y):
    return [(p[0]+x, p[1]+y) for p in polygon]

def rotate(polygon, x0, y0, alpha):
    return polygon

def demo_animation():
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

def draw_trajectory():
    '''Generate random trajectory between two points and draw it'''
    screen = pygame.display.set_mode((300,300), 0, 32)
    p = [20, 20]
    q = [280, 280]
    dots = [[random.randint(20,280), random.randint(20,280)] for _ in range(500)]

    lpoints = []
    rpoints = []
    left = p
    right = q
    for _ in range(250):
        dots.sort(key=lambda d: -((d[0]-left[0])**2+(d[1]-left[1])**2))
        d = dots.pop()
        lpoints.append(d)
        left = d
        dots.sort(key=lambda d: -(abs(d[0]-right[0])+abs(d[1]-right[1])))
        d = dots.pop()
        rpoints.insert(0, d)
        right = d
    points = [p] + lpoints + rpoints + [q]
    color = (255, 255, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.lock()
        pygame.draw.lines(screen, color, False, points)
        screen.unlock()
        pygame.display.update()

def draw_trajectory_with_tsp():
    '''Generate random trajectory between two points and draw it'''
    screen = pygame.display.set_mode((300,300), 0, 32)
    p = [20, 20]
    q = [280, 280]
    dots = [[random.randint(20,280), random.randint(20,280)] for _ in range(500)]

    n, D = tsp.mk_matrix(dots, tsp.distL2) # create the distance matrix
    tour = tsp.randtour(n)
    z = tsp.length(tour, D)
    z = tsp.localsearch(tour, z, D)
    # tour zawiera indeksy punktow, przez ktore prowadzi trasa

    points = [p] + [dots[i] for i in tour] + [q]
    color = (255, 255, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.lock()
        pygame.draw.lines(screen, color, False, points)
        screen.unlock()
        pygame.display.update()


def tsp_demo():
    coord = [(4,0),(5,6),(8,3),(4,4),(4,1),(4,10),(4,7),(6,8),(8,1)]
    n, D = tsp.mk_matrix(coord, tsp.distL2) # create the distance matrix
    instance = "demo"
    tour = tsp.randtour(n)
    z = tsp.length(tour, D)
    print "random:", tour, z, '  -->  ',
    z = tsp.localsearch(tour, z, D)
    print tour, z

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
        dx, dy = random.choice(N)
        sofa_ = move(sofa, dx, dy)
        if in_corridor(sofa_):
            sofa = sofa_
            screen.fill(GREY1)
            pygame.draw.polygon(screen, GREY2, corridor)
            pygame.draw.polygon(screen, WHITE, sofa)
            screen.unlock()
            pygame.display.update()
        pygame.time.wait(100)



if __name__ == '__main__':
    #show_sofa()
    draw_trajectory_with_tsp()
