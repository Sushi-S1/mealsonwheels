import pygame
import pyserial
#vision import stuff
import os
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
from google.protobuf import text_format
import argparse
import sys
import json
import time



class Robot:

    def __init__():
        pygame.init()
        #Arduino for Drive and lift motors + CS
        ser1 = serial.Serial("/dev/ttyACM0",115200) 
        #Arduino for Spikes
        ser2 = serial.Serial("/dev/ttyACM1",115200) 
        screen = pygame.display.set_mode((240, 240))
        ser1.flush()
        ser2.flush()
        print("connected to: " + ser1.portstr + " at baudrate: " + ser1.baudrate)
        print("connected to: " + ser2.portstr + " at baudrate: " + ser2.baudrate)

        
    def MoveForward():
        ser1.write('F')

    def MoveBackward():
        ser1.write('B')

    def MoveRight():
        ser1.write('R')

    def MoveLeft():
        ser1.write('L')

    def StopAll():
        ser1.write('Q')
        ser2.write('Q')

    def KBdrive():
        flag = False
        data = ""
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
    
    def Vision():

        

