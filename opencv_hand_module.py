import cv2
import mediapipe as mp
import numpy as np

# MediaPipe 손 모듈 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# 웹캠 초기화
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break
    
    # 좌우 반전 (미러 효과)
    frame = cv2.flip(frame, 1)

    # BGR 이미지를 RGB로 변환
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # 손 랜드마크 그리기 및 제스처 인식
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 랜드마크 그리기
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 손가락 끝 좌표 (인덱스: 8, 중지: 12, 약지: 16, 새끼: 20)
            landmarks = hand_landmarks.landmark
            h, w, _ = frame.shape
            tips = [8, 12, 16, 20]  # 손가락 끝 인덱스
            wrist = 0  # 손목 인덱스
            fingers_up = 0

            # 손가락이 펴져 있는지 확인 (손가락 끝이 손목보다 위에 있는지)
            for tip in tips:
                if landmarks[tip].y < landmarks[wrist].y:
                    fingers_up += 1

            # 제스처 텍스트 출력
            gesture = f"Fingers: {fingers_up}"
            cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 결과 출력
    cv2.imshow("Hand Gesture Recognition", frame)

    # 'q' 키로 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
