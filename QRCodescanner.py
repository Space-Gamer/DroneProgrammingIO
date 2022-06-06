import cv2
from cv2 import QRCodeDetector

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

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

def land():
    print("Landing")
    vehicle.mode = VehicleMode('RTL')
    while vehicle.location.global_relative_frame.alt>=(0.5):
        print("Vehilce at",vehicle.location.global_relative_frame.alt,"m")
        time.sleep(1)

    print("Landed")


while True:
    _,image = cap.read()
    res,_,_ = detector.detectAndDecode(image)
    if res == '1':
        arm_takeoff(25)
    elif res == '2':
        land()
        break
    cv2.imshow('Video',image)
    cv2.waitKey(100)



time.sleep(1)

#close vehicle
vehicle.close()
cv2.destroyAllWindows()