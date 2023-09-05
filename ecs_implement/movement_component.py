from ecs import Component

class MovementComponent(Component):
    def __init__(self, step):
        self.step = step