from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)


fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
captured_video=cv2.VideoWriter('output.mp4',fourcc,20.0,(width,height))
while True:
    pankaj=ImageGrab.grab(bbox=(0,0,width,height))
    pankaj_np=np.array(pankaj)
    pankaj_final=cv2.cvtColor(pankaj_np,cv2.COLOR_BGR2RGB)
    cv2.imshow("screen record",pankaj_final)
    captured_video.write(pankaj_final)
    
    if cv2.waitKey(10)==ord('p'):
        break
