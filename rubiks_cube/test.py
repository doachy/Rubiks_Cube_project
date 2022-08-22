import cv2
import numpy as np

def tracking():
    cap=cv2.VideoCapture(-1)
    x=cap.get(3)
    y=cap.get(4)
    print(x, y)
    
    while True:
        ret, frame =cap.read()
        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    cv2.destroyAllwindowsws()

tracking()