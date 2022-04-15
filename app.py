import pygame
import numpy as np
from math import sin, cos
from matrices import projection_matrix


def read_points_from_file(filename):
    with open(filename, "r") as file:
        matrix = [[[int(num)] for num in line.split(',')] for line in file]

        return matrix


def connect(p1, p2):
    pygame.draw.line(window, (255, 255, 255), (p1[0], p1[1]), (p2[0], p2[1]))


WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
OFFSET_HEIGHT = WINDOW_HEIGHT / 2
OFFSET_WIDTH = WINDOW_WIDTH / 2
SCALE = 100
ACCELERATION = 0.01

cube_matrix = read_points_from_file("cube_points.txt")

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

x_angle = y_angle = z_angle = 0

while True:
    clock.tick(60)
    window.fill((0, 0, 0))

    x_rotation_matrix = [[1, 0, 0],
                         [0, cos(x_angle), -sin(x_angle)],
                         [0, sin(x_angle), cos(x_angle)]]

    y_rotation_matrix = [[cos(y_angle), 0, sin(y_angle)],
                         [0, 1, 0],
                         [-sin(y_angle), 0, cos(y_angle)]]

    z_rotation_matrix = [[cos(z_angle), -sin(z_angle), 0],
                         [sin(z_angle), cos(z_angle), 0],
                         [0, 0, 1]]

    points = []
    for point in cube_matrix:
        x_rotation = np.dot(x_rotation_matrix, point)
        y_rotation = np.dot(y_rotation_matrix, x_rotation)
        z_rotation = np.dot(z_rotation_matrix, y_rotation)

        points_flat = np.dot(projection_matrix, z_rotation)

        x = (points_flat[0][0] * SCALE) + OFFSET_WIDTH
        y = (points_flat[1][0] * SCALE) + OFFSET_HEIGHT
        points.append((x, y))
        pygame.draw.circle(window, (255, 0, 0), (x, y), 5)

    connect(points[0], points[1])
    connect(points[0], points[3])
    connect(points[0], points[4])
    connect(points[1], points[2])
    connect(points[1], points[5])
    connect(points[2], points[6])
    connect(points[2], points[3])
    connect(points[3], points[7])
    connect(points[4], points[5])
    connect(points[4], points[7])
    connect(points[6], points[5])
    connect(points[6], points[7])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            y_angle -= ACCELERATION

        if keys[pygame.K_d]:
            y_angle += ACCELERATION

        if keys[pygame.K_w]:
            x_angle -= ACCELERATION

        if keys[pygame.K_s]:
            x_angle += ACCELERATION

        if keys[pygame.K_z]:
            SCALE += 100

        if keys[pygame.K_x]:
            SCALE -= 100



    pygame.display.update()
