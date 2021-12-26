import cv2
import mediapipe as mp
import time


class poseIdentification():
    def __init__(self, mode=False, complexity=1, smooth=True, segmentation=False, smoothseg=True, detectionConf=0.5, trackConf=0.5):

        self.mode = mode
        self.complexity = complexity
        self.smooth = smooth
        self.segmentation = segmentation
        self.smoothseg = smoothseg
        self.detectionConf = detectionConf
        self.trackConf = trackConf

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            self.mode, self.complexity, self.smooth, self.detectionConf, self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self, frame, draw=True):

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.pose.process(frameRGB)

        if result.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(frame, result.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)

        return frame

        # for id, lm in enumerate(result.pose_landmarks.landmark):
        #     h, w, c = frame.shape

        #     cx, cy = int(lm.x * w), int(lm.y * h)
        #     cv2.circle(frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
        #     # print(cx, cy)
        #     print(id, lm)
        # if id == 30:
        #     cv2.circle(frame, (cx, cy), 10, (0, 0, 255), cv2.FILLED)


def main():
    cap = cv2.VideoCapture("pose_Identification/run1.mp4")
    pTime = 0
    Time = 0
    detector = poseIdentification()

    while True:
        success, frame = cap.read()
        frame = detector.findPose(frame)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, str(int(fps)), (2, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

        cv2.imshow("Image", frame)
        key = cv2.waitKey(1)
        if key == 81 or key == 113:
            break


if __name__ == "__main__":
    main()
