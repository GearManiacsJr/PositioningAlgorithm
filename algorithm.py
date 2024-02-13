import math
import time
from main import gyro, robot

x = 20
y = 20

def reset():
    global x, y
    x = 20
    y = 20
    gyro.reset_angle(0)
    pass

def rad2deg(rad):
    return rad * 180 / math.pi

def rot(deg):
    if gyro.angle() < deg:
        while gyro.angle() < deg:
            robot.drive(0, 45)
            #print(str(deg) + " " + str(gyro.angle()))
        robot.stop()
    elif gyro.angle() > deg:
        while gyro.angle() > deg:
            robot.drive(0, -45)
            #print(str(deg) + " " + str(gyro.angle()))
        robot.stop()
    pass


def MoveForwardBlue(x1, y1, rotation1):
    global x, y
    alpha = rad2deg(math.atan((y1 - y) / (x1 - x)))
    if (x1 > x and y1 > y) or (x1 > x and y > y1): 
        rot(alpha)
    elif (x > x1 and y > y1):
        rot(alpha - 180)
    elif(y1 > y and x > x1):
        rot(alpha + 180)
    d = math.sqrt((x1 - x) * (x1 - x) + (y1 -y) * (y1 - y)) * 10
    robot.straight(d)
    rot(rotation1)
    x = x1
    y = y1
    pass


def MoveBackwardBlue(x1, y1, rotation1):
    global x, y
    alpha = rad2deg(math.atan((y1 - y) / (x1 - x)))
    if (x1 > x and y1 > y):
        rot((180 - alpha) * -1)
    elif (x1 > x and y > y1):
        rot((180 - alpha) * -1)
    elif (x > x1 and y > y1) or (y1 > y and x > x1):
        rot(alpha)
    d = math.sqrt((x1 - x) * (x1 - x) + (y1 -y) * (y1 - y)) * 10
    robot.straight(-d)
    rot(rotation1)
    x = x1
    y = y1
    pass

def MoveForwardRed(x1, y1, rotation1):
    global x, y
    alpha = rad2deg(math.atan((y1 - y) / (x1 - x)))
    if (x1 > x and y1 > y) or (x1 > x and y > y1): 
        rot(-alpha)
    elif (x > x1 and y > y1):
        rot((alpha - 180) * -1)
    elif (y1 > y and x > x1):
        rot(-alpha - 180)
    d = math.sqrt((x1 - x) * (x1 - x) + (y1 -y) * (y1 - y)) * 10
    robot.straight(d)
    rot(rotation1)
    x = x1
    y = y1
    pass
    

def MoveBackwardRed(x1, y1, rotation1):
    global x, y
    alpha = rad2deg(math.atan((y1 - y) / (x1 - x)))
    if (x1 > x and y1 > y): 
        rot((alpha - 180) * -1)
    elif (x1 > x and y > y1):
        rot(-alpha - 180)
    elif (x > x1 and y > y1) or (y1 > y and x > x1):
        rot(-alpha)
    d = math.sqrt((x1 - x) * (x1 - x) + (y1 -y) * (y1 - y)) * 10
    robot.straight(-d)
    rot(rotation1)
    x = x1
    y = y1
    pass

def lift(d):
    d = d * 360 / (2 * 1.6 * math.pi)
    brat.run_angle(4000, d)
    pass