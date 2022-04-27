import numpy as np
import pygame

from math import sin, cos


class CameraController:
    def __init__(self, camera, velocity=3, sensitivity=0.01):
        self.camera = camera
        self.velocity = velocity
        self.sensitivity = sensitivity

        # pygame.mouse.set_visible(False)
        # pygame.event.set_grab(True)

    def rotate(self):
        keys = pygame.key.get_pressed()

        a = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        b = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        c = keys[pygame.K_o] - keys[pygame.K_p]

        self.camera.x_rotation -= self.sensitivity * a
        self.camera.y_rotation += self.sensitivity * b
        self.camera.z_rotation += self.sensitivity * c

    def move(self):
        y = self.camera.y_rotation

        matrix = np.matrix([
            [cos(y), 0, sin(y), 0],
            [0, 1, 0, 0],
            [-sin(y), 0, cos(y), 0],
            [0, 0, 0, 1]
        ])

        keys = pygame.key.get_pressed()

        a = keys[pygame.K_d] - keys[pygame.K_a]
        b = keys[pygame.K_w] - keys[pygame.K_s]
        c = keys[pygame.K_x] - keys[pygame.K_z]

        self.camera.position += 0.05 * np.matmul(matrix, np.matrix([a, c, b, 0]).T)

    def update(self):
        self.rotate()
        self.move()
