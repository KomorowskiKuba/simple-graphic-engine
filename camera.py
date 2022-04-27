import numpy as np

from math import sin, cos, tan, pi


def make_x_rotation_matrix(angle, point):
    matrix = np.matrix([
        [1, 0, 0, 0],
        [0, cos(angle), sin(angle), 0],
        [0, -sin(angle), cos(angle), 0],
        [0, 0, 0, 1]
    ])

    return np.matmul(matrix, point)


def make_y_rotation_matrix(angle, point):
    matrix = np.matrix([
        [cos(angle), 0, sin(angle), 0],
        [0, 1, 0, 0],
        [-sin(angle), 0, cos(angle), 0],
        [0, 0, 0, 1]
    ])

    return np.matmul(matrix, point)


def make_z_rotation_matrix(angle, point):
    matrix = np.matrix([
        [cos(angle), -sin(angle), 0, 0],
        [sin(angle), cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    return np.matmul(matrix, point)


def make_translation_matrix(vector, point, constant=1):
    matrix = np.matrix([
        [1, 0, 0, constant * vector[0]],
        [0, 1, 0, constant * vector[1]],
        [0, 0, 1, constant * vector[2]],
        [0, 0, 0, 1]
    ])

    return np.matmul(matrix, point)


class Camera:
    def __init__(self, position, rotation, fov, offset, zoom=1):
        self.position = np.matrix(list(position) + [0], dtype=float).T
        self.x_rotation, self.y_rotation, self.z_rotation = rotation
        self.fov = fov
        self.offset = offset
        self.ow, self.oh = self.offset
        self.a = self.ow / tan(self.fov * pi / 360)
        self.zoom = zoom

    def relative(self, point):
        matrix = make_translation_matrix(self.position.T.tolist()[0], point, self.zoom)
        matrix = make_z_rotation_matrix(-self.z_rotation, matrix)
        matrix = make_y_rotation_matrix(-self.y_rotation, matrix)
        matrix = make_x_rotation_matrix(-self.x_rotation, matrix)

        return matrix

    def perspective(self, relative_point):
        matrix = np.matrix([
            [self.a, 0, self.ow, 0],
            [0, -self.a, self.oh, 0],
            [0, 0, 1, 0]
        ])

        result = np.matmul(matrix, relative_point)

        return np.squeeze(np.asarray(result / result[-1])).tolist()[:-1]

    def render(self, relative):
        return self.perspective(relative)

    def render_line(self, relative_1, relative_2):
        u = self.perspective(relative_1)
        v = self.perspective(relative_2)

        return u, v
