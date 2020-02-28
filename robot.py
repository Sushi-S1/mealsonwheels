import pygame
import pyserial
import tensorflow

class Robot:
    pygame.init()
    ser1 = serial.Serial("/dev/ttyACM0",115200) 
    ser2 = serial.Serial("/dev/ttyACM1",115200) 

    def KBdrive():
        while True:
            for event in pygame.event.get():
               keys = key.get_pressed()
               if event.type == pygame.KEYDOWN:
                    if keys[K_UP]:
                        flag = True
                        data = "UP"
                    elif keys[K_DOWN]:
                        flag = True
                        data = "DOWN"
                    elif keys[K_RIGHT]:
                        flag = True
                        data = "RIGHT"
                    elif keys[K_LEFT]:
                        flag = True
                        data = "LEFT"
                elif event.type == pygame.KEYUP:
                    if keys[K_UP]:
                        flag = False
                        data = ""
                    elif keys[K_DOWN]:
                        flag = False
                        data = ""
                    elif keys[K_RIGHT]:
                        flag = False
                        data = ""
                    elif keys[K_LEFT]:
                        flag = False
                        data = "" 
                if flag == True:
                    ser1.write(data.encode())
                    ser1.flush()

    def ColorSensing():
        