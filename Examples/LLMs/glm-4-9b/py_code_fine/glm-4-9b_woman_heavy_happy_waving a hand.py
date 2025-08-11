
import numpy as np
import pygame
import sys
from pygame.locals import *

class PointLightAnimation:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 600
        self.FPS = 60
        self.point_lights = []
        self.bg_color = (0, 0, 0)
        self.light_color = (255, 255, 255)
        self.light_radius = 5
        self.init_pygame()
        self.create_point_lights()
        self.wave()

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Biological Motion Stimulus')
        self.clock = pygame.time.Clock()

    def create_point_lights(self):
        num_lights = 15
        center_x, center_y = self.WIDTH // 2, self.HEIGHT // 2
        radius = 150
        
        for i in range(num_lights):
            angle = 2 * np.pi * i / num_lights
            x = center_x + radius * np.cos(angle)
            y = center_y + radius * np.sin(angle)
            self.point_lights.append([x, y])

    def wave(self):
        wave_length = 2 * np.pi
        wave_speed = 0.05
        time_offset = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.screen.fill(self.bg_color)
            
            current_time = pygame.time.get_ticks() / 1000.0 + time_offset
            for light in self.point_lights:
                center_x, center_y = self.WIDTH // 2, self.HEIGHT // 2
                dx = light[0] - center_x
                dy = light[1] - center_y
                angle = np.arctan2(dy, dx)
                wave = np.sin(current_time * wave_speed * wave_length + angle)
                x = center_x + dx + wave * 50
                y = center_y + dy
                pygame.draw.circle(self.screen, self.light_color, (int(x), int(y)), self.light_radius)
            
            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    animation = PointLightAnimation()
