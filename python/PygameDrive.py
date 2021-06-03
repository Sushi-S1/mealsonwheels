import serial
import pygame
pygame.init()
screen = pygame.display.set_mode((240, 240))
ser1 = serial.Serial("/dev/ttyACM0",115200) 
print("connected to: " + ser1.portstr)
ser1.flush()
data = ""

    
while True:
    for event in pygame.event.get():
        keys = key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[K_UP]:
                data = "U"
                ser1.write(data.encode())
            if keys[K_DOWN]:
                data = "D"
                ser1.write(data.encode())
            if keys[K_RIGHT]:
                data = "R"
                ser1.write(data.encode())
            if keys[K_LEFT]:
                data = "L"
                ser1.write(data.encode())
            ser1.flush()
    
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

"""
while True:
    for event in pygame.event.get():
        keys = key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[K_UP]:
                flag = True
                data = "U"
            if keys[K_DOWN]:
                flag = True
                data = "D"
            if keys[K_RIGHT]:
                flag = True
                data = "R"
            if keys[K_LEFT]:
                flag = True
                data = "L"
        elif event.type == pygame.KEYUP:
            flag = False
     if flag == True:
        ser1.write(data.encode())
        ser1.flush()     
      """

          




