from microbit import display, Image, sleep
import tinybit

# Display startup confirmation
display.show(Image.HAPPY)
sleep(500)

# Define speed profiles: (left_speed, right_speed, duration_ms)
SPEED_PROFILES = [
    (0, 0, 1000),      # Stop
    (50, 50, 1000),     # Very slow
    (100, 100, 1000),   # Slow
    (150, 150, 1000),   # Medium
    (200, 200, 1000),   # Fast
    (255, 255, 1000)    # Full speed
]

# Main speed cycle loop
while True:
    for left_speed, right_speed, duration in SPEED_PROFILES:
        tinybit.car_run(left_speed, right_speed)
        sleep(duration)s