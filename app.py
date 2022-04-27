import sys
import pygame

from camera import Camera
from camera_controller import CameraController
from cube import Cube
from settings import (WINDOW_WIDTH,
                      WINDOW_HEIGHT,
                      OFFSET_WIDTH,
                      OFFSET_HEIGHT,
                      FPS,
                      FOV,
                      BLACK)
from utils import read_points_from_file, read_connections_from_file

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

camera = Camera(position=(0, 0, -4),
                rotation=(0, 0, 0),
                fov=FOV,
                offset=(OFFSET_WIDTH, OFFSET_HEIGHT))

controller = CameraController(camera)

scene_objects = [
    Cube(camera,
         position=(0, 0, 0),
         rotation=(0, 0, 0),
         scale=(1, 1, 1),
         corners=read_points_from_file('data/cube_points_1.txt'),
         edges=read_connections_from_file('data/cube_connections.txt')),
    Cube(camera,
         position=(0, 0, 0),
         rotation=(0, 0, 0),
         scale=(1, 1, 1),
         corners=read_points_from_file('data/cube_points_2.txt'),
         edges=read_connections_from_file('data/cube_connections.txt')),
    Cube(camera,
         position=(0, 0, 0),
         rotation=(0, 0, 0),
         scale=(1, 1, 1),
         corners=read_points_from_file('data/cube_points_3.txt'),
         edges=read_connections_from_file('data/cube_connections.txt')),
    Cube(camera,
         position=(0, 0, 0),
         rotation=(0, 0, 0),
         scale=(1, 1, 1),
         corners=read_points_from_file('data/cube_points_4.txt'),
         edges=read_connections_from_file('data/cube_connections.txt')),
]

while True:
    window.fill(BLACK)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                camera.zoom += 0.5

            if event.key == pygame.K_r:
                camera.zoom -= 0.5

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    for scene_object in scene_objects:
        scene_object.draw(window)

    pygame.display.update()
    controller.update()
