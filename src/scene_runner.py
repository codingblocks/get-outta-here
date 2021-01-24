import pygame
import time

class SceneRunner(object):
    def __init__(self, surface, states, start_state):
        self.scene = None
        self.done = False
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states
        self.change_scene(start_state)
        for s in states:
            states[s].register_runner(self)
        self.last_time = 0
        self.toggle = False
        self.switch_scene_time_s = 0

    def event_loop(self):
        for event in pygame.event.get():
            self.scene.get_event(event)

    def change_scene(self, scene_name: str, state: dict = {}):
        self.scene_name = scene_name
        if self.scene is not None:
            self.scene.before_exit()
        self.switch_scene_time_s = time.time()
        self.scene = self.states[self.scene_name]
        self.scene.update_state(state)

    def update(self, dt):
        if time.time() > self.switch_scene_time_s + 1:
            if self.scene.quit:
                self.done = True

            self.scene.update(dt)

    def render(self):
        self.scene.render(self.surface)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.render()
            pygame.display.update()
