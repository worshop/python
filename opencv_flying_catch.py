import cv2
import numpy as np
import mediapipe as mp
import random
import time

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

# 게임 설정
score = 0
game_duration = 30  # 게임 시간(초)
start_time = time.time()
fly_x, fly_y = random.randint(100, 1180), random.randint(100, 620)  # 초기 파리 위치
fly_radius = 20
fly_speed = 10  # 파리 이동 속도

# 파리 이미지 생성 함수
def draw_fly(frame, x, y):
    # 몸통: 세로 타원
    cv2.ellipse(frame, (x, y), (15, 25), 0, 0, 360, (0, 0, 0), -1)
    # 날개: 반투명한 타원
    overlay = frame.copy()
    cv2.ellipse(overlay, (x - 20, y - 10), (20, 10), 45, 0, 360, (200, 200, 200), -1)
    cv2.ellipse(overlay, (x + 20, y - 10), (20, 10), -45, 0, 360, (200, 200, 200), -1)
    frame[:] = cv2.addWeighted(overlay, 0.5, frame, 0.5, 0)
    # 눈: 두 개의 작은 원
    cv2.circle(frame, (x - 10, y - 15), 3, (255, 255, 255), -1)
    cv2.circle(frame, (x + 10, y - 15), 3, (255, 255, 255), -1)
    # 레이블
    cv2.putText(frame, "Fly", (x - 30, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 좌우 반전
    frame = cv2.flip(frame, 1)

    # 남은 시간 계산
    elapsed_time = time.time() - start_time
    time_left = max(0, game_duration - elapsed_time)
    if time_left <= 0:
        cv2.putText(frame, f"게임 종료! 점수: {score}", (400, 360), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
        cv2.imshow("Fly Catching Game", frame)
        cv2.waitKey(2000)  # 2초 대기 후 종료
        break

    # 손가락 추적
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # 파리 그리기
    draw_fly(frame, fly_x, fly_y)

    # 손가락 위치 확인
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_tip = hand_landmarks.landmark[8]  # 검지 끝
            h, w, _ = frame.shape
            finger_x, finger_y = int(index_tip.x * w), int(index_tip.y * h)

            # 손가락과 파리 충돌 체크
            distance = np.sqrt((finger_x - fly_x) ** 2 + (finger_y - fly_y) ** 2)
            if distance < fly_radius + 20:  # 손가락과 파리 충돌
                score += 10
                fly_x, fly_y = random.randint(100, 1180), random.randint(100, 620)  # 새 파리 위치

    # 파리 무작위 이동
    fly_x += random.randint(-fly_speed, fly_speed)
    fly_y += random.randint(-fly_speed, fly_speed)
    # 화면 밖으로 나가지 않도록 제한
    fly_x = max(100, min(1180, fly_x))
    fly_y = max(100, min(620, fly_y))

    # 점수 및 시간 표시
    cv2.putText(frame, f"Score: {score}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Time: {int(time_left)}s", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 결과 출력
    cv2.imshow("Fly Catching Game", frame)

    # 'q' 키로 조기 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
