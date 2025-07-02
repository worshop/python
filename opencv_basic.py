
import cv2

def main():
    # 카메라 열기 (기본 장치 인덱스는 0, 필요시 조정)
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    # MJPG 포맷 설정 (해상도 및 프레임률 안정화에 도움됨)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    
    # 해상도 설정: 1280x720
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 프레임률 설정 (데이터시트 기준 최대 30FPS)
    cap.set(cv2.CAP_PROP_FPS, 15)

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        cv2.imshow("HQ-USB-1080HD (1280x720)", frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
