
# pseudo-code only, real implementation would be very complex and beyond here 

import pygame

# Define a function for the points' movements
def point_movement():
    ...

# Define a function to arrange lights in a running person
def arrange_lights_in_person():
    ...

# Create the pygame screen
screen = pygame.display.set_mode((width, height))

while True:
    events = pygame.event.get()
    for event in events:
        if event == QUIT:
            ...  # End the loop to close the window

    # Call the function to move the points
    point_movement()

    # Call the function to arrange lights in a person
    arrange_lights_in_person()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
