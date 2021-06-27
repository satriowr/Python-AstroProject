from typing import ItemsView
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

signGesture = [8, 12, 16, 20]
jempol_sign = 4

while True :
    ret, img, = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)

    if results.multi_hand_landmarks :
        for hand_landmark in results.multi_hand_landmarks :
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark) :
                lm_list.append(lm)
            
            sign_status = []

            for sign in signGesture :
                x, y = int(lm_list[sign].x * w), int(lm_list[sign].y * h)
                # print(id, ":", x, y)
                cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)

                if lm_list[sign].x < lm_list[sign - 3].x :
                     cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                     sign_status.append(True)
                
                else :
                    sign_status.append(False)

            print(sign_status)

            if lm_list[jempol_sign].y < lm_list[jempol_sign - 1].y < lm_list[jempol_sign - 2].y :
                if all(sign_status) :
                    cv2.putText(img, "minum", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
                    print("minum")
                
                elif lm_list[jempol_sign].y > lm_list[jempol_sign - 1].y > lm_list[jempol_sign - 2].y :
                    cv2.putText(img, "MAKAN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255), 3)
                    print("MAKAN")

            mp_draw.draw_landmarks(img, hand_landmark,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((0, 0, 255), 2, 2),
                                   mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                   )

    cv2.imshow("Sign Language", img)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
