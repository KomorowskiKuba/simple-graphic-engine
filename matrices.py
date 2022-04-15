from math import sin, cos

x_angle = 0
y_angle = 0
z_angle = 0

projection_matrix = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]

x_rotation_matrix = [[1, 0, 0],
                     [0, cos(x_angle), -sin(x_angle)],
                     [0, sin(x_angle), cos(x_angle)]]

y_rotation_matrix = [[cos(y_angle), 0, sin(y_angle)],
                     [0, 1, 0],
                     [-sin(y_angle), 0, cos(y_angle)]]

z_rotation_matrix = [[cos(z_angle), -sin(z_angle), 0],
                     [sin(z_angle), cos(z_angle), 0],
                     [0, 0, 1]]
