import RPi.GPIO as JUICE
from time import sleep
import keyboard

JUICE.setmode(JUICE.BCM)

Motor1A = 23 #IN1
Motor1B = 24 #IN2
Motor1E = 25 #EN1

Motor2A = 26 
Motor2B = 5
Motor2E = 6

JUICE.setup(Motor1A, JUICE.OUT)
JUICE.setup(Motor1B, JUICE.OUT)
JUICE.setup(Motor1E, JUICE.OUT)
JUICE.setup(Motor2A, JUICE.OUT)
JUICE.setup(Motor2B, JUICE.OUT)
JUICE.setup(Motor2E, JUICE.OUT)
print("Setup complete.")

while True:
    
    while keyboard.is_pressed('w'):
        JUICE.output(Motor1A, JUICE.LOW)
        JUICE.output(Motor1B, JUICE.HIGH)
        JUICE.output(Motor1E, JUICE.HIGH)
        JUICE.output(Motor2A, JUICE.LOW)
        JUICE.output(Motor2B, JUICE.HIGH)
        JUICE.output(Motor2E, JUICE.HIGH)
        print("Moving forwards...")
        sleep(0.1)
        
        print("Stopped.")
        JUICE.output(Motor1E, JUICE.LOW)
        JUICE.output(Motor2E, JUICE.LOW)
        
    while keyboard.is_pressed('s'):
        # Going backwards
        JUICE.output(Motor1A, JUICE.HIGH)
        JUICE.output(Motor1B, JUICE.LOW)
        JUICE.output(Motor1E, JUICE.HIGH)
        JUICE.output(Motor2A, JUICE.HIGH)
        JUICE.output(Motor2B, JUICE.LOW)
        JUICE.output(Motor2E, JUICE.HIGH)
        print("Moving backwards...")
        sleep(0.1)
        
        print("Stopped.")
        JUICE.output(Motor1E, JUICE.LOW)
        JUICE.output(Motor2E, JUICE.LOW)
        
    while keyboard.is_pressed('a'):
        JUICE.output(Motor1A, JUICE.LOW)
        JUICE.output(Motor1B, JUICE.HIGH)
        JUICE.output(Motor1E, JUICE.HIGH)
        JUICE.output(Motor2A, JUICE.HIGH)
        JUICE.output(Motor2B, JUICE.LOW)
        JUICE.output(Motor2E, JUICE.HIGH)
        print("Turning left...")
        sleep(0.1)
        
        print("Stopped.")
        JUICE.output(Motor1E, JUICE.LOW)
        JUICE.output(Motor2E, JUICE.LOW)
        
    while keyboard.is_pressed('d'):
        JUICE.output(Motor1A, JUICE.HIGH)
        JUICE.output(Motor1B, JUICE.LOW)
        JUICE.output(Motor1E, JUICE.HIGH)
        JUICE.output(Motor2A, JUICE.LOW)
        JUICE.output(Motor2B, JUICE.HIGH)
        JUICE.output(Motor2E, JUICE.HIGH)
        print("Turning right...")
        sleep(0.1)
        
        print("Stopped.")
        JUICE.output(Motor1E, JUICE.LOW)
        JUICE.output(Motor2E, JUICE.LOW)
        
# Cool lines here!!!!
#
# 
#
# Cool lines are OVER STOP IT