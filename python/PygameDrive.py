import serial
import pygame
pygame.init()
screen = pygame.display.set_mode((240, 240))
ser1 = serial.Serial("COM3",115200)
print("connected to: " + ser1.portstr)
ser1.flush()
data = ""

    
while True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                data = "L"
                ser1.write(data.encode())
            if event.key == pygame.K_RIGHT:
                data = "R"
                ser1.write(data.encode())
            if event.key == pygame.K_UP:
                data = "U"
                ser1.write(data.encode())
            if event.key == pygame.K_DOWN:
                data = "D"
                ser1.write(data.encode())
            if event.key == pygame.K_Q:
                print("Exit")
                break



