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
        pygame.mixer.init()
        #Arduino for Drive and lift motors + CS
        ser1 = serial.Serial("/dev/ttyACM0",115200) 
        #Arduino for Spikes
        ser2 = serial.Serial("/dev/ttyACM1",115200) 
        screen = pygame.display.set_mode((240, 240))
        ser1.flush()
        ser2.flush()
        print("connected to: " + ser1.portstr + " at baudrate: " + ser1.baudrate)
        print("connected to: " + ser2.portstr + " at baudrate: " + ser2.baudrate)
        """
    def PlaySound():
        sound = Pygame.mixer.Sound("go_away.wav")
        sound.play()
"""
    def MoveForward():
        ser1.write('F/n')

    def MoveBackward():
        ser1.write('B/n')

    def MoveRight():
        ser1.write('R/n')

    def MoveLeft():
        ser1.write('L/n')

    def StopAll():
        ser1.write('Q/n')
        ser2.write('Q/n')

    def KBdrive():
        flag = False
        data = ""
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
                    if keys[K_UP]:
                        flag = False
                        data = ""
                    if keys[K_DOWN]:
                        flag = False
                        data = ""
                    if keys[K_RIGHT]:
                        flag = False
                        data = ""
                    if keys[K_LEFT]:
                        flag = False
                        data = "" 
                if flag == True:
                    ser1.write(data.encode())
                    ser1.flush()
    
    def Vision():
        IM_WIDTH = 640   
        IM_HEIGHT = 480   
        objects = []
        def write_json(data, filename='data.json'):
            with open(filename, 'w') as f:
                data = data.tolist()
                json.dump(data, f, indent=4)

        camera_type = 'picamera'

        sys.path.append('..')
        from utils import label_map_util
        from utils import visualization_utils as vis_util
        MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'
        CWD_PATH = os.getcwd()
        PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
        PATH_TO_LABELS = os.path.join(CWD_PATH,'data','mscoco_label_map.pbtxt')
        NUM_CLASSES = 90
        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        category_index = label_map_util.create_category_index(categories)
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

            sess = tf.Session(graph=detection_graph)
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')
        frame_rate_calc = 1
        freq = cv2.getTickFrequency()
        font = cv2.FONT_HERSHEY_SIMPLEX
        camera.resolution = (IM_WIDTH,IM_HEIGHT)
        camera.framerate = 10
        rawCapture = PiRGBArray(camera, size=(IM_WIDTH,IM_HEIGHT))
        rawCapture.truncate(0)
        for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
            t1 = cv2.getTickCount()
            frame = np.copy(frame1.array)
            frame.setflags(write=1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_expanded = np.expand_dims(frame_rgb, axis=0)
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.40)
            cv2.putText(frame,"FPS: {0:.2f}".format(frame_rate_calc),(30,50),font,1,(255,255,0),2,cv2.LINE_AA) 
            cv2.imshow('Object detector', frame)
            t2 = cv2.getTickCount()
            time1 = (t2-t1)/freq
            frame_rate_calc = 1/time1    
            if cv2.waitKey(1) == ord('q'):
                break
            rawCapture.truncate(0)
        camera.close()

        #webapp/json code
        '''
        objects = a.tolist()
        for x in num:
            objects = objects[:x.astype(np.int32)]
            #print(objects)
        print(objects)
        for i in range(0, len(objects)):
            if objects[i] in category_index:
                    objects[i] = category_index[objects[i]]
                
        print(objects)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        datas[current_time] = objects
        with open('data.json', 'w') as out:
            json.dump(datas, out)
        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate_calc = 1/time1
         '''       

    def ColorSensing()
        color = ""
        while True:
            color = ser.readline()
            if color = "R"
                MoveForward()
                color = ser.readline()
            elif color = "G"
                MoveBackward()
                color = ser.readline()
            elif color = "B"
                MoveRight()
                color = ser.readline()
            elif color = "Y"
                MoveLeft()
                color = ser.readline() 
            else:
                print("No color detected")

        
            

                

