from Arduino import Arduino
import time
import giphy
import json

board = Arduino('9600', port='COM4') #plugged in via USB, serial com at rate 9600

CLEAN = "flowers"
SMELLY = "skunks"

def write(url, smelliness):
    with open('state.html', 'w') as f:
        data = json.dumps({'url':url, 'smelliness':smelliness})
        f.write(data)

last_state = new_state = None
url = ''
while True:
    time.sleep(.01)
    reading = board.analogRead(0)
    reading = float(reading)*5/1023
    print reading
    if reading > .875:
        new_state = SMELLY
    elif reading < .87:
        new_state = CLEAN
    if new_state != last_state:
        print("New state: %s" % new_state)
        url = giphy.search(new_state)
    write(url, reading)
    last_state = new_state





