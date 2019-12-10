''' This is the beginning of the scenario in which the picars demonstrate the
human race first entering the equation and how they interact with the oceans.
The picars will go along and fish in the oceans as "humans".

For this scene set a paper with a spear on it to show the picar
as a human that is spear fishing.
'''
STARTING_SPEED = 50

import comm
import Pyro4
import traceback
import picar
from picar.obstacle_sensor import *
from picar.front_wheels import *
from picar.back_wheels import *
import time

steering = Front_Wheels()  # create a Front_Wheels object for steering the car
motors = Back_Wheels()    # create a Back_Wheels object to move the car
objSensor = Obstacle_Sensor()  # create an Object_Sensor() object to detect distance to objects

picar.setup()
steering.ready()
motors.speed = STARTING_SPEED
motors.ready()

#class HuntingDance:

@Pyro4.expose
def fisherman():
    ''' This is as if a human is looking around in the water
    for the fish, waiting for an opportunity.
    '''
    motors.stop()
    for i in range(2):
        steering.turn(140)
        time.sleep(2)
        steering.turn(40)
        time.sleep(2)
    
    steering.turn_straight()
    
    motors.speed = 90
    motors.forward()
    time.sleep(1)
    motors.stop()
    motors.speed = 50
    #Sound to be implemented

@Pyro4.expose
def caughtFish():
    ''' This is the fish squirming as it gets caught before dying.
    '''
    motors.stop()
    motors.speed= 15
    motors.forward()
    for i in range(3):
        steering.turn_left()
        time.sleep(1)
        steering.turn_right()
        time.sleep(1)
    steering.turn(140)
    steering.turn(110)
    time.sleep(1)
    motors.stop()
    motors.speed= 50
    steering.turn_straight()

@Pyro4.expose
def failedCatch():
    ''' This is the audio played when the human
    fails to catch the fish he has spotted.
    '''
    motors.stop()
    #Wiggle
    for i in range(2):
        steering.turn_left()
        time.sleep(0.5)
        steering.turn_right()
        time.sleep(0.5)
    steering.turn_straight()
    motors.speed = 90
    motors.backward()
    time.sleep(3)
    motors.stop()
    motors.speed= 50

'''if __name__ == "__main__":
    comm.startServer("10.33.22.155","PicarHunter",{"HuntingDance",HuntingDance})
'''
