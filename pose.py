import cv2
import mediapipe as mp
import time


mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture("pose_Identification/run1.mp4")
pTime = 0
cTime = 0

while True:
    success, frame = cap.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(frameRGB)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(frame, result.pose_landmarks,
                              mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = frame.shape

            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
            # print(cx, cy)
            print(id, lm)
            # if id == 30:
            #     cv2.circle(frame, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (2, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break
