import cv2
import serial
import time
from HandTrackModule import handDetector

# Setup serial
ser = serial.Serial('COM13', 9600)
time.sleep(2)

detector = handDetector(detectionCon=0.7)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if lmList:
        fingers = detector.fingersUp()
        if fingers == [1, 1, 1, 1, 1]:
            ser.write(b'$255\n')
        elif fingers == [0, 0, 0, 0, 0]:
            ser.write(b'$0\n')
        else:
            ser.write(b'$128\n')

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
ser.close()
cv2.destroyAllWindows()
