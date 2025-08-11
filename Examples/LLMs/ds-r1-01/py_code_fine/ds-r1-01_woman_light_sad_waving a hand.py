
import pygame
import math

def calculate_elbow(shoulder, hand, upper_arm_length, forearm_length):
    sx, sy = shoulder
    hx, hy = hand

    dx = hx - sx
    dy = hy - sy
    d = math.hypot(dx, dy)

    if d == 0:
        return (sx, sy + upper_arm_length)

    if d > upper_arm_length + forearm_length or d < abs(upper_arm_length - forearm_length):
        return ((sx + hx)/2, (sy + hy)/2)

    a = (a**2 + c**2 - b**2) / (2 * a * c) if d > upper_arm_length + forearm_length or d < abs(upper_arm_length - forearm_length):
        mid_x = (sx + hx) / 2
        mid_y = (sy + hy) / 2
        return (mid_x, mid_y)

    a = upper_arm_length
    b = forearm_length
    c = d

    cos_theta = (a**2 + c**2 - b**2) / (2 * a * c)
    theta = math.acos(cos_theta)

    dir_x = dx / d
    dir_y = dy / d

    elbow_rel_x1 = a * (dir_x * math.cos(theta) - dir_y * math.sin(theta))
    elbow_rel_y1 = a * (dir_x * math.sin(theta) + dir_y * math.cos(theta))

    elbow_rel_x2 = a * (dir_x * math.cos(-theta) - dir_y * math.sin(-theta))
    elbow_rel_y2 = a * (dir_x * math.sin(-theta) + dir_y * math.cos(-theta))

    elbow1 = (sx + elbow_rel_x1, sy + elbow_rel_y1)
    elbow2 = (sx + elbow_rel_x2, sy + elbow_rel_y2)

    return elbow1 if elbow1[1] < elbow2[1] else elbow2

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Biological Motion - Sad Woman Waving")

black = (0, 0, 0)
white = (255, 255, 255)
torso_x, torso_y = screen_width // 2, screen_height // 2

upper_arm_length = 50
forearm_length = 50

points = [
    {'pos': (torso_x, torso_y - 100), 'move': False},
    {'pos': (torso_x, torso_y - 50), 'move': False},
    {'pos': (torso_x + 50, torso_y - 50), 'move': False},
    {'pos': (torso_x + 50, torso_y), 'move': True},
    {'pos': (torso_x + 50, torso_y + 50), 'move': True},
    {'pos': (torso_x - 50, torso_y - 50), 'move': False},
    {'pos': (torso_x - 50, torso_y), 'move': False},
    {'pos': (torso_x - 50, torso_y + 50), 'move': False},
    {'pos': (torso_x, torso_y), 'move': False},
    {'pos': (torso_x + 30, torso_y + 50), 'move': False},
    {'pos': (torso_x + 30, torso_y + 100), 'move': False},
    {'pos': (torso_x + 30, torso_y + 150), 'move': False},
    {'pos': (torso_x - 30, torso_y + 50), 'move': False},
    {'pos': (torso_x - 30, torso_y + 100), 'move': False},
    {'pos': (torso_x - 30, torso_y + 150), 'move': False},
]

clock = pygame.time.Clock()
time = 0.0
amplitude = 30
speed = 2.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time += 0.05 * speed
    right_shoulder = points[2]['pos']
    hand_x = right_shoulder[0] + amplitude * math.sin(time)
    hand_y = right_shoulder[1] + 30 * math.sin(time * 2) + 30

    elbow_pos = calculate_elbow(right_shoulder, (hand_x, hand_y), upper_arm_length, forearm_length)
    points[3]['pos'] = elbow_pos
    points[4]['pos'] = (hand_x, hand_y)

    screen.fill(black)
    for point in points:
        pygame.draw.circle(screen, white, (int(point['pos'][0]), int(point['pos'][1])), 5)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
