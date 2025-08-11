
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define point-light positions and connections
# Initial positions of the point-lights representing a stick figure
initial_positions = {
    'head': (0, 6),
    'shoulderL': (-1, 5), 'shoulderR': (1, 5),
    'elbowL': (-1.5, 4), 'elbowR': (1.5, 4),
    'handL': (-2, 3.5), 'handR': (2, 3.5),
    'hipL': (-0.5, 2), 'hipR': (0.5, 2),
    'kneeL': (-0.5, 1), 'kneeR': (0.5, 1),
    'footL': (-0.5, 0), 'footR': (0.5, 0)
}

connections = [
    ('head', 'shoulderL'), ('head', 'shoulderR'),
    ('shoulderL', 'elbowL'), ('shoulderR', 'elbowR'),
    ('elbowL', 'handL'), ('elbowR', 'handR'),
    ('shoulderL', 'hipL'), ('shoulderR', 'hipR'),
    ('hipL', 'kneeL'), ('hipR', 'kneeR'),
    ('kneeL', 'footL'), ('kneeR', 'footR'),
    ('hipL', 'hipR')
]

# Function to create the waving motion
def update_positions(frame):
    # Define hand waving motion based on sine wave
    hand_wave_amplitude = 0.5  # Height of the wave
    hand_wave_frequency = 0.1  # Speed of the wave

    handL_y_offset = hand_wave_amplitude * np.sin(hand_wave_frequency * frame)
    # Only move left hand in sine wave motion
    positions['handL'] = (-2, 3.5 + handL_y_offset)

    # Update other positions for smooth motion if needed
    # (fixed here for the example)

# Initialize positions dictionary for animation
positions = initial_positions.copy()

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)  # Set limits for better view
fig.loop polly event frame

