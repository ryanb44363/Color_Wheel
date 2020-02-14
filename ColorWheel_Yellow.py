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
        
        #yellow

        low_yellow = np.array([5, 252, 255])
        high_yellow = np.array([36, 224, 220])
        image_mask = cv2.inRange(hsv, low_yellow, high_yellow)
        cv2.imshow("Image Mask", image_mask)
        cv2.imshow("Original Webcam Feed", frame)
        
        if cv2.waitKey(1) == 27:
          break
    cv2.destroyAllWindows()
    cap.release()
if __name__ == "__main__":
    main()