from dronekit import *

#connect to vehicle
vehicle = connect('127.0.0.1:14551', baud=921600, wait_ready=True)#ip=loop to same system, baud->bits per second

#get vehicle mode
print(vehicle.mode)

#Checks if vehicle is armable
print(vehicle.is_armable)

#Checks if vehicle is armed
print(vehicle.armed)

#Arming vehicle
if vehicle.is_armable:
    if vehicle.mode != 'STABILIZE': #Can be armed only in some modes
        vehicle.mode = "STABILIZE"
    vehicle.armed = True


#Close the vehicle
vehicle.close()
