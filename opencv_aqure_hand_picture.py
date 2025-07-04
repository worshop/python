import cv2
import mediapipe as mp
import numpy as np
import datetime
import os

def is_forming_rectangle(hand1_landmarks, hand2_landmarks, frame_shape):
    """
    두 손의 랜드마크가 네모 모양을 형성하는지 확인합니다.

    Args:
        hand1_landmarks: 첫 번째 손의 랜드마크.
        hand2_landmarks: 두 번째 손의 랜드마크.
        frame_shape: 프레임의 높이와 너비 (h, w).

    Returns:
        네모를 형성하면 꼭지점 좌표 리스트를, 그렇지 않으면 None을 반환합니다.
    """
    h, w = frame_shape
    
    # 각 손의 엄지(4)와 검지(8) 랜드마크 좌표를 가져옵니다.
    h1_thumb = (int(hand1_landmarks.landmark[4].x * w), int(hand1_landmarks.landmark[4].y * h))
    h1_index = (int(hand1_landmarks.landmark[8].x * w), int(hand1_landmarks.landmark[8].y * h))
    h2_thumb = (int(hand2_landmarks.landmark[4].x * w), int(hand2_landmarks.landmark[4].y * h))
    h2_index = (int(hand2_landmarks.landmark[8].x * w), int(hand2_landmarks.landmark[8].y * h))

    # 손의 좌우를 구분합니다. x좌표가 작은 쪽이 왼손.
    if h1_thumb[0] < h2_thumb[0]:
        left_thumb, left_index = h1_thumb, h1_index
        right_thumb, right_index = h2_thumb, h2_index
    else:
        left_thumb, left_index = h2_thumb, h2_index
        right_thumb, right_index = h1_thumb, h1_index

    # 네모 조건 확인:
    # 1. 두 검지 손가락의 y좌표가 비슷해야 합니다 (상단).
    # 2. 두 엄지 손가락의 y좌표가 비슷해야 합니다 (하단).
    # 3. 왼쪽 손가락들의 x좌표가 오른쪽 손가락들의 x좌표보다 작아야 합니다.
    # 4. 검지들이 엄지들보다 위에 있어야 합니다.
    
    y_threshold = abs(left_index[1] - right_index[1])
    y_thumb_threshold = abs(left_thumb[1] - right_thumb[1])
    
    # y좌표 허용 오차 (손가락 높이의 50% 정도)
    y_tolerance = abs(left_index[1] - left_thumb[1]) * 0.5 

    if (y_threshold < y_tolerance and 
        y_thumb_threshold < y_tolerance and
        left_index[1] < left_thumb[1] and 
        right_index[1] < right_thumb[1]):
        
        # 네 꼭지점 반환: 좌상단, 우상단, 우하단, 좌하단
        points = [left_index, right_index, right_thumb, left_thumb]
        return points

    return None

def main():
    """웹캠에서 손으로 만든 네모를 감지하여 사진을 촬영하는 메인 함수."""
    # MediaPipe Hands 모듈 초기화
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
    mp_drawing = mp.solutions.drawing_utils

    # 웹캠 설정
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 15)

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    # 네모 감지 및 캡처 관련 변수
    rect_detected_frames = 0
    CAPTURE_THRESHOLD = 15  # 1초 동안 유지 시 캡처 (15fps 기준)
    last_capture_time = 0
    COOLDOWN_SECONDS = 5  # 캡처 후 5초 대기
    
    output_dir = './data/output/'
    os.makedirs(output_dir, exist_ok=True)

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
        
        rectangle_points = None
        if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 2:
            hand1_landmarks = results.multi_hand_landmarks[0]
            hand2_landmarks = results.multi_hand_landmarks[1]
            
            # 랜드마크 그리기
            mp_drawing.draw_landmarks(frame, hand1_landmarks, mp_hands.HAND_CONNECTIONS)
            mp_drawing.draw_landmarks(frame, hand2_landmarks, mp_hands.HAND_CONNECTIONS)

            rectangle_points = is_forming_rectangle(hand1_landmarks, hand2_landmarks, (480, 640))

        # 네모 감지 및 처리
        current_time = datetime.datetime.now().timestamp()
        if rectangle_points and (current_time - last_capture_time > COOLDOWN_SECONDS):
            rect_detected_frames += 1
            
            # 네모 그리기
            cv2.polylines(frame, [np.array(rectangle_points)], isClosed=True, color=(0, 255, 0), thickness=2)
            cv2.putText(frame, f"Capturing in... {((CAPTURE_THRESHOLD - rect_detected_frames) / 15):.1f}s", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            if rect_detected_frames >= CAPTURE_THRESHOLD:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = os.path.join(output_dir, f"capture_{timestamp}.png")
                cv2.imwrite(filename, frame)
                print(f"사진이 {filename}에 저장되었습니다.")
                
                # 캡처 성공 메시지 표시
                cv2.putText(frame, "Captured!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                last_capture_time = current_time
                rect_detected_frames = 0
        else:
            rect_detected_frames = 0 # 네모가 아니면 카운터 리셋
            if current_time - last_capture_time <= COOLDOWN_SECONDS:
                 cv2.putText(frame, f"Cooldown: {(COOLDOWN_SECONDS - (current_time - last_capture_time)):.1f}s", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)


        cv2.imshow("Hand Square Capture", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    hands.close()

if __name__ == "__main__":
    main()
