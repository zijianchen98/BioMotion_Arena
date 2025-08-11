
from PIL import Image, ImageDraw
import numpy as np

def point_light_animation():
    height, width = 600, 600
    image = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(image)

    hand_points = [(210, 150), (200, 100), (205, 70), (220, 50), (230, 30), (235, 80), (250, 120), (245, 150)]
    hand_points_next = [(310, 150), (320, 100), (315, 70), (300, 50), (290, 30), (285, 80), (270, 120), (275, 150)]
    
    for _ in range(50):  # 50 to show 2 frames per second for a 10 second animation
        image_draw = ImageDraw.Draw(image)
        for light in hand_points:
            draw_circle(image_draw, light)
        for light in hand_points_next:
            draw_circle(image_draw, light)
        image.save('point_light_animation.gif', save_all=True, append_images=[image], duration=40)
        hand_points = hand_points_next
        hand_points_next = [(x+1, y) if y < 250 else (x-1, y-20) for x, y in hand_points]
    return None

def draw_circle(draw, center, radius=10, fill=(255, 255, 255, 255)):
    draw.ellipse((center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius), fill=fill)

point_light_animation()
