import cv2
import numpy as np
import PIL
import io
import html
import time
import imageio
import matplotlib.pyplot as plt
import BodyTracker as Bt
from utils import *
from dtaidistance import dtw


video1='videos/77.mp4'
video2='videos/33.mp4'
detector = Bt.poseDetector()


#EXTRACTION key points
def pose(img):
    pTime = 0    
    lmList=[]

    nframes=30 # is the number of saved frames for the function live_tracker
    iterator=0
    angles=[]
    refTime=time.time()
    tracker=live_tracker(nframes)

     #positioning of text and dimensions
    h_angle=50
    w_angle=100
    h_j=65
    w_j=w_angle
    fontScale=2
    thickness=2

    width,height, c=img.shape
    size=(width, height)
    #writer= cv2.VideoWriter('runpose.mp4', cv2.VideoWriter_fourcc('M','J','P','G'), 20, (width,height))
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    print(img)
    points=[12, 14, 16]
    p=points
    maxim=max(points)
    angle=0
    lmList1=[]
    inf=60
    sup=140
    #draw angle and perform evaluation
    """if(maxim>len(lmList)):
        draw=False
    if(search(lmList, p[0])  and search(lmList, p[1] ) ) and ( search(lmList, p[2]) ):
        draw=True"""
    angle=detector.findAngle(img, p[0], p[1], p[2]), 
    angles.append(angle)
    if(True):
        judge(img, angle, inf, sup)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    lmList1.append(lmList)
    cv2.imshow("Capture1",img)
    #writer.write(img)
    return cTime,lmList1

def main(video1,video2):
    cap=cv2.VideoCapture(video1)
    cap1=cv2.VideoCapture(video2)
    time.sleep(2)
    pTime = 0    
    lmList=[]
    nframes=30 # is the number of saved frames for the function live_tracker
    iterator=0
    angles=[]
    refTime=time.time()
    tracker=live_tracker(nframes)

     #positioning of text and dimensions
    h_angle=50
    w_angle=100
    h_j=65
    w_j=w_angle
    fontScale=2
    thickness=2

     
    try:
        duration=args.max_len
        if duration is None:
            duration=25
    except:
        duration=40
    
    while cap.isOpened():

        success, img = cap.read()
        success1, img1 = cap1.read() 
        
        if success is False or img is None:
            break
        print(success)
        cTime, Kp=pose(img)
        #cTime, Kp1=pose(img1)        
        #print(Kp) 
        #d =dtw.warping_path(Kp, Kp1)
        #dtwvis.plot_warping(Kp, Kp1, path, filename="warp.png")
        
        key=cv2.waitKey(10)
        if key == ord('q'):
          break
        if (cTime-refTime)>duration:
            print("end ")
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main(video1, video2)