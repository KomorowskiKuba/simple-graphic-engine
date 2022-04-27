from scene_object import SceneObject


class Cube(SceneObject):
    def __init__(self, camera, position, rotation, scale, corners, edges):
        super().__init__(
            camera,
            position,
            rotation,
            scale,
            corners,
            edges
        )
