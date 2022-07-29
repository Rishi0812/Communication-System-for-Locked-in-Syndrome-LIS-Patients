import cv2
import playsound
import time
from cvzone.FaceMeshModule import FaceMeshDetector


class Video(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = FaceMeshDetector(maxFaces=1)
        self.blinkCounter = 0
        self.counter = 0
        self.start_time = time.time()
        self.end_time = time.time()

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
        ratioList = []
        color = (255, 255, 0)

        if self.cap.get(cv2.CAP_PROP_POS_FRAMES) == self.cap.get(cv2.CAP_PROP_FRAME_COUNT):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, img = self.cap.read()
        img, faces = self.detector.findFaceMesh(img, draw=True)

        if faces:
            face = faces[0]
            for id in idList:
                cv2.circle(img, face[id], 5, color, cv2.FILLED)

            leftUp = face[159]
            leftDown = face[23]
            leftLeft = face[130]
            leftRight = face[243]
            lenghtVer, _ = self.detector.findDistance(leftUp, leftDown)
            lenghtHor, _ = self.detector.findDistance(leftLeft, leftRight)

            cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
            cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

            ratio = int((lenghtVer / lenghtHor) * 100)
            ratioList.append(ratio)
            if len(ratioList) > 3:
                ratioList.pop(0)
            ratioAvg = sum(ratioList) / len(ratioList)

            if ratioAvg < 35 and self.counter == 0:
                self.blinkCounter += 1
                color = (0, 200, 0)
                self.counter = 1
            if self.counter != 0:
                self.counter += 1
                if self.counter > 10:
                    self.counter = 0
                    color = (255, 255, 0)

            cv2.putText(img, "Blink Count: {}".format(self.blinkCounter), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            img = cv2.resize(img, (600, 500))

        else:
            img = cv2.resize(img, (600, 500))

        if self.blinkCounter == 2:
            self.start_time = time.time()

        time_list1 = []

        if self.blinkCounter == 3:
            self.end_time = time.time()
            total_time = self.end_time - self.start_time
            time_list1.append(total_time)

        if self.blinkCounter == 3:
            cv2.putText(img, "Help Me!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            if time_list1[-1] >= 4:
                for _ in range(10):
                    playsound.playsound("audios/aud_1.mp3")

        elif self.blinkCounter == 4:
            cv2.putText(img, "Sanitary Discomfort", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            # playsound.playsound("aud_2.mp3")
        elif self.blinkCounter == 5:
            cv2.putText(img, "Contact Family", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            # playsound.playsound("aud_3.mp3")
        elif self.blinkCounter == 6:
            self.blinkCounter = 0

        success, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()
