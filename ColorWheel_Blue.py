import cv2 as cv2
import numpy as np
def main():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    while ret:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #Blue

        low_blue = np.array([100, 70, 70])
        high_blue = np.array([140, 255, 255])
        image_mask = cv2.inRange(hsv, low_blue, high_blue)
        cv2.imshow("Image Mask", image_mask)
        cv2.imshow("Original Webcam Feed", frame)
    
        
        if cv2.waitKey(1) == 27:
          break
    cv2.destroyAllWindows()
    cap.release()
if __name__ == "__main__":
    main()