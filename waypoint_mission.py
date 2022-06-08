from dronekit import *
import time

vehicle = connect('127.0.0.1:14551', baud=921600, wait_ready=True)

#takeoff function
def arm_takeoff(height):
    #check if drone is ready
    while not vehicle.is_armable:
        print("waiting for drone")
        time.sleep(1)
    
    #change mode and arm
    print("Arming")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    #check if drone is armed
    while not vehicle.armed:
        print("Waiting for arm")
        time.sleep(1)

    #takeoff
    print("Takeoff")
    vehicle.simple_takeoff(height)
    
    #report values back every 1s and finally break out
    while vehicle.location.global_relative_frame.alt<=(height*0.95):
        print("Reached", vehicle.location.global_relative_frame.alt, "m")
        time.sleep(0.5)
    print("Reached target altitude")

arm_takeoff(10)

print('Mission')
vehicle.mode = VehicleMode('AUTO')
time.sleep(300)

#landing
print("Landing")
vehicle.mode = VehicleMode('RTL')
while vehicle.location.global_relative_frame.alt>=(0.5):
    print("Vehilce at",vehicle.location.global_relative_frame.alt,"m")
    time.sleep(1)

print("Landed")

time.sleep(10)

#close vehicle
vehicle.close()