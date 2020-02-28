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

screen = pygame.display.set_mode((240, 240))
ser1 = serial.Serial("/dev/ttyACM0",115200) 
print("connected to: " + ser1.portstr)
ser1.flush()
flag = False
data = ""

class Robot:

    def __init__():
        pygame.init()
        ser1 = serial.Serial("/dev/ttyACM0",115200) 
        ser2 = serial.Serial("/dev/ttyACM1",115200) 
        screen = pygame.display.set_mode((240, 240))
        ser1.flush()
        ser2.flush()
        flag = False
        data = ""

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
