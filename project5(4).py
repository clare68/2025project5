from microbit import sleep, display, Image, button_a, button_b
import tinybit

# Define custom letter images for LED display
LETTER_IMAGES = {
    "L": Image("90000:90000:90000:90000:99999"),
    "O": Image("09990:90009:90009:90009:09990"),
    "D": Image("99000:90900:90090:90009:99999"),
    "Z": Image("99999:00090:00900:09000:99999")
}

# Define movement sequences for each letter (action, speed, duration_ms)
LETTER_MOVEMENTS = {
    "L": [
        ("run", 80, 1000),
        ("spinleft", 180, 400),
        ("run", 80, 1000),
        ("stop", 0, 0)
    ],
    "O": [
        ("run", 80, 1000),
        ("spinleft", 180, 400),
        ("run", 80, 1000),
        ("spinleft", 180, 400),
        ("run", 80, 1000),
        ("spinleft", 180, 400),
        ("run", 80, 1000),
        ("spinleft", 180, 400),
        ("stop", 0, 0)
    ],
    "D": [
        ("run", 80, 1000),
        ("spinleft", 180, 500),
        ("run", 80, 1500),
        ("spinleft", 80, 1000),
        ("run", 80, 1200),
        ("stop", 0, 0)
    ],
    "Z": [
        ("run", 80, 1000),
        ("spinright", 120, 500),
        ("run", 80, 1300),
        ("spinleft", 65, 600),
        ("run", 60, 1300),
        ("stop", 0, 0)
    ]
}

# Initialization
display.show(Image.HAPPY)
sleep(1000)
current_letter_index = 0
letter_keys = list(LETTER_IMAGES.keys())
current_letter = letter_keys[current_letter_index]
display.show(LETTER_IMAGES[current_letter])

def execute_path(letter):
    """Execute the movement sequence for the selected letter"""
    display.show(LETTER_IMAGES[letter])
    sleep(1000)
    
    for action, speed, duration in LETTER_MOVEMENTS[letter]:
        if action == "run":
            tinybit.car_run(speed)
        elif action == "spinleft":
            tinybit.car_spinleft(speed)
        elif action == "spinright":
            tinybit.car_spinright(speed)
        elif action == "stop":
            tinybit.car_stop()
        
        if duration > 0:
            sleep(duration)

# Main interaction loop
while True:
    # Button A cycles through letter options
    if button_a.was_pressed():
        current_letter_index = (current_letter_index + 1) % len(letter_keys)
        current_letter = letter_keys[current_letter_index]
        display.show(LETTER_IMAGES[current_letter])
        sleep(500)
    
    # Button B executes the selected path
    if button_b.was_pressed():
        execute_path(current_letter)
        # Reset display after path completion
        sleep(1000)
        display.show(LETTER_IMAGES[current_letter])