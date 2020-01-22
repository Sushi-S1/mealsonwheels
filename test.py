import serial
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
ser = serial.Serial("/dev/ttyACM0",9600)
print("connected to: " + ser.portstr)
ser.flush()
data = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
             data = "UP"
             print("up")
          elif event.key == pygame.K_DOWN:
             data = "DOWN"
             print("down")
          elif event.key == pygame.K_RIGHT:
             data = "RIGHT"
             print("right")
          elif event.key == pygame.K_LEFT:
             data = "LEFT"
             print("left")
          ser.write(data.encode())
          ser.flush()
    
    
    
    
    
'''   for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
             ser.write("UP")
             ser.flush()
             print("up")
          elif event.key == pygame.K_DOWN:
             ser.write("DOWN")
             ser.flush()
             print("down")
          elif event.key == pygame.K_RIGHT:
             ser.write("RIGHT")
             ser.flush()
             print("right")
          elif event.key == pygame.K_LEFT:
             ser.write("LEFT")
             ser.flush()
             print("left")'''
      

          




