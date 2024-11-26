import keyboard
import time
# to change the phrase change type varible
# the faster the speed the less accuracy
type = "cake state high most it head we mean high much"
def type_phrase():
    for char in type:
        keyboard.write(char)
        time.sleep(0.027)  
# change keyboard .wait to a shortcut you want to use when you start the bot
keyboard.wait("ctrl+shift+?")

type_phrase()


