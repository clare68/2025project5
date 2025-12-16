from microbit import display, Image, sleep
import tinybit

# Define movement sequence: (function, speed, indicator, duration)
MOVEMENT_SEQUENCE = [
    (tinybit.car_run, 150, Image.ARROW_S, 1000),    # Forward
    (tinybit.car_back, 150, Image.ARROW_N, 1000),    # Backward
    (tinybit.car_left, 150, Image.ARROW_E, 1000),    # Left turn
    (tinybit.car_right, 150, Image.ARROW_W, 1000),   # Right turn
    (tinybit.car_spinleft, 150, Image.ARROW_E, 1000),# Spin left
    (tinybit.car_spinright, 150, Image.ARROW_W, 1000)# Spin right
]

# Main execution loop
while True:
    for move_func, speed, indicator, duration in MOVEMENT_SEQUENCE:
        # Execute movement
        move_func(speed)
        # Display direction indicator
        display.show(indicator)
        # Maintain movement for specified duration
        sleep(duration)
    
    # Reset between cycles
    display.clear()
    tinybit.car_stop()
    sleep(1000)