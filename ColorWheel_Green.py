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
        
        #green

        low_green = np.array([40, 50, 50])
        high_green = np.array([80, 255, 255])
        image_mask = cv2.inRange(hsv, low_green, high_green)
        cv2.imshow("Image Mask", image_mask)
        cv2.imshow("Original Webcam Feed", frame)
        
        if cv2.waitKey(1) == 27:
          break
    cv2.destroyAllWindows()
    cap.release()
if __name__ == "__main__":
    main()