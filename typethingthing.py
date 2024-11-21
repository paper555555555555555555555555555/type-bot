import keyboard
import time

# Define the phrase to type
phrase = "cake state high most it head we mean high much"
def type_phrase():
    for char in phrase:
        keyboard.write(char)
        time.sleep(0.027)  # Adding a small delay to mimic typing speed

# Define the key combination to start typing


# Wait for the specific key combination
keyboard.wait("ctrl+shift+?")

# Start typing the phrase
type_phrase()

