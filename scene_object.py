import numpy as np
import pygame

from camera import make_x_rotation_matrix, make_y_rotation_matrix, make_z_rotation_matrix, make_translation_matrix
from settings import PINK, LIGHT_BLUE


def do_scale(factor, point):
    matrix = np.matrix([
        [factor[0], 0, 0, 0],
        [0, factor[1], 0, 0],
        [0, 0, factor[2], 0],
        [0, 0, 0, 1]
    ])

    return np.matmul(matrix, point)


class SceneObject:
    def __init__(self, camera, position, rotation, scale, corners, edges):
        self.camera = camera
        self.position = position
        self.rotation = rotation
        self.x_rotation, self.y_rotation, self.z_rotation = rotation
        self.scale = scale
        self.raw_corners = [np.matrix([x, y, z, 1]).T for x, z, y in corners]
        self.corners = self.get_corners()
        self.edges = edges

    def get_corners(self):
        output = []
        for corner in self.raw_corners:
            matrix = make_z_rotation_matrix(
                self.z_rotation,
                do_scale(self.scale, corner)
            )

            matrix = make_y_rotation_matrix(self.y_rotation, matrix)
            matrix = make_x_rotation_matrix(self.x_rotation, matrix)
            matrix = make_translation_matrix(self.position, matrix)

            output.append(matrix)

        return output

    def draw(self, window):
        relative_corners = [self.camera.relative(corner) for corner in self.corners]

        for corner in relative_corners:
            c = self.camera.render(corner)
            if c:
                pygame.draw.circle(window, PINK, c, 5)

        for edge in self.edges:
            line = self.camera.render_line(relative_corners[edge[0]], relative_corners[edge[1]])
            if line:
                pygame.draw.line(window, LIGHT_BLUE, line[0], line[1], 2)
