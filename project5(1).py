import tinybit
from microbit import display, Image, sleep

# Display forward direction indicator
display.show(Image.ARROW_S)

# Initiate forward movement at medium speed
tinybit.car_run(150)

# Maintain movement for 2 seconds
sleep(2000)

# Stop the robot after movement cycle
tinybit.car_stop()