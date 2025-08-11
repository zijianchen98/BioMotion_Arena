
import pygame
import math
import random

class PointLight:
    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return f"PointLight({self.position})"

class SadWomanAnimation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.running = True
        self.light_positions = self.init_lights()
        self.last_time = None

    def init_lights(self):
        lights = [
            PointLight((150, 50)),
            PointLight((250, 50)),
            PointLight((150, 150)),
            PointLight((250, 150)),
            PointLight((350, 150)),
            PointLight((150, 250)),
            PointLight((350, 250)),
            PointLight((450, 250)),
            PointLight((150, 350)),
            PointLight((350, 350)),
            PointLight((450, 350)),
            PointLight((150, 450)),
            PointLight((250, 450)),
            PointLight((450, 450)),
            PointLight((350, 500))
        ]
        return lights

    def update_lights(self, dt):
        for light in self.light_positions:
            light.position = (
                (light.position[0] + -5 if random.random() > 0.5 else light.position[0] + 5),
                (light.position[1] + 10 if random.random() > 0.5 else light.position[1] + 15)
            )

    def run(self):
        clock = pygame.time.Clock()
        self.last_time = pygame.time.get_ticks()
        while self.running:
            self.update_lights(clock.tick() / 1000)
            
            self.screen.fill((0, 0, 0))
            for light in self.light_positions:
                pygame.draw.circle(self.screen, (255, 255, 255), light.position, 5)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()

if __name__ == "__main__":
    animation = SadWomanAnimation()
    animation.run()
