'''
by Hermann18 ( aka Ubermenchanin or Philistine Typical ) 
This is the basic version of the program that processes video from cameras. 
Could be improved as 
*optimize code; *work with file storage; *optimize processing 
'''
from imageai.Detection import VideoObjectDetection, ObjectDetection
import os
import cv2
from matplotlib import pyplot as plt
import time
b = 0
bb = 0
color_index = {'bus': 'red', 'truck': 'indigo', 'motorcycle': 'azure', 'refrigerator': 'gold',
               'bicycle': 'olivedrab', 'car': 'silver', 'traffic light': 'mediumblue', 'person': 'honeydew',
               'stop sign': 'beige'}


cap = cv2.VideoCapture("rtsp://stream:ljOL8fDu@10.0.231.60")

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
custom = detector.CustomObjects(bus=True, truck=True, motorcycle=True, refrigerator=True,
                                bicycle=True, car=True, traffic_light=True, person=True, stop_sign=True)
detector.loadModel()


#cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
#out = cv2.VideoWriter('video22.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (1280,720))
ret, frame = cap.read()
height, width = frame.shape[:2]
out = cv2.VideoWriter(f'communism/video{bb}.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (width // 2, height // 2))
while True:
    try:
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        print('wow')
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        height, width = frame.shape[:2]
        frame = cv2.resize(frame, (width // 2, height // 2))
        print(b)
        cv2.imwrite(f'communism/{b}.png', frame)
        detections = detector.detectCustomObjectsFromImage(
            custom_objects=custom,
            input_image=f'communism/{b}.png',
            output_image_path= f'communism/{b}p.png',
            minimum_percentage_probability=30)
        a = cv2.imread(f'communism/{b}p.png')
        cv2.imshow('result', a)
        for i in range(5):
            out.write(a)
        time.sleep(1)
        b += 1
    except Exception as e :
        print(e)
        print('/ / / ')
        bb += 1
        print(bb)
        cap.release()
        out.release()
        cap = cv2.VideoCapture(f'communism/video0.avi')
        ret, frame = cap.read()
        height, width = frame.shape[:2]
        out = cv2.VideoWriter('videoend.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))
        cap.release()
        for i in range(bb):
            cap = cv2.VideoCapture(f'communism/video{i}.avi')
            print(i, '-тут')
            ret, frame = cap.read()
            out.write(frame)
            while ret:
                ret, frame = cap.read()
                out.write(frame)
            cap.release()
        out.release()
        print('sieg')
        cap = cv2.VideoCapture("rtsp://stream:ljOL8fDu@10.0.231.60")
        cap.set(3, 1280)
        cap.set(4, 720)
        ret, frame = cap.read()
        height, width = frame.shape[:2]
        out = cv2.VideoWriter(f'communism/video{bb}.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (width // 2, height // 2))
        
        
print('/')
bb+=1
cap.release()
out.release()
cv2.destroyAllWindows()
cap = cv2.VideoCapture(f'communism/video0.avi')
ret, frame = cap.read()
height, width = frame.shape[:2]
out = cv2.VideoWriter('videoend.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))
cap.release()
for i in range(bb):
    cap = cv2.VideoCapture(f'communism/video{i}.avi')
    print(i, '-тут')
    ret, frame = cap.read()
    out.write(frame)
    while ret:
        ret, frame = cap.read()
        out.write(frame)
    cap.release()
out.release()

