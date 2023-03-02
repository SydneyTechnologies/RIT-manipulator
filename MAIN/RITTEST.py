import cv2
import time 
import serial
from EpsonController import sendToEpson, Home, clientSocket
from take_picture import takePicture
from DetectedObjects import DetectedObjects
from getWorldCoordinates import getRealWorld
from TalkToServo import talkToServo, checkDistance


SERVO_PORT = "/dev/cu.usbserial-1140"
arduino = serial.Serial(port=SERVO_PORT, timeout=0, baudrate=9600)
HEIGHT = 206



while(True):
     

    # Open servo then go to the home point
    talkToServo("g0")

    Home()


    # Take picture 
    reference_path = takePicture()
    reference_image = cv2.imread(reference_path)


    # Get center points 
    # initialize detector
    Detector = DetectedObjects(reference_image)
    # gets the list objects in for of the object class
    # Detector.getCenterPoints()

    object_list = Detector.getContours()

    # sort the objects by the pickscore
    sorted_list = Detector.sortDetectedObjects(object_list)
    if len(sorted_list) == 0:
         break

    # get first center point 
    target_object = sorted_list[0]
    targetX = target_object.center_point[0]
    targetY = target_object.center_point[1]
    targetU = target_object.orientation


    # convert to world coordinates
    worldX, worldY = getRealWorld(targetX, targetY)
    # go to the first center point
    sendToEpson(x=worldX, y=worldY, robot_z=600, robot_u=targetU)

    # distance = int(talkToServo("s"))
    # print("distance from sensor: ")
    # print(distance)
    # if distance != 0 and distance != None:
    #     if distance < 206: 
    #         distance_z =  (600 - distance) + 60
    #         if distance > 95:
    #               distance_z =  (600 - distance) + 20

    #     else: 
    #          continue
        
    # print("z=")
    # print(distance_z)
    
    # # go down 
    sendToEpson(x=worldX, y=worldY, robot_z=480)
             

        




    # close gripper 
    time.sleep(0.2)
    talkToServo("g40")
    time.sleep(1)


    # go up 
    sendToEpson(x=worldX, y=worldY, robot_z=700)



    # go to drop point 
    if arduino.in_waiting > 0:  # check if there's data in the serial buffer
            data = arduino.readline().decode().strip()  # read the data from the serial port and decode it as a string
            print("Received:", data)  
            
    sendToEpson(x=-370, y=570, robot_z=850)


    # drop item in box, open gripper
    talkToServo("g0")
    time.sleep(1)



    #go home

    time.sleep(0.2)
    Home()




