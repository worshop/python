OpenCV 이미지 처리 프로젝트 규칙
1. 프로젝트 개요
이 프로젝트는 Python과 OpenCV를 사용하여 다양한 이미지 처리 기능을 구현합니다. 주요 목표는 이미지를 불러오고, 변환 및 분석하며, 결과 이미지를 저장하거나 시각화하는 것입니다. GUI가 필요한 경우 Tkinter를 사용할 수 있습니다.

2. 파일 및 폴더 구조
루트 디렉토리: /home/jarabot/opencv_project

파일:

main.py: 애플리케이션 실행 진입점. 최소한의 코드로 핵심 로직 호출.

image_processor.py: 이미지 처리 함수 및 클래스 정의.

utils.py: 공통 유틸리티 함수(예: 파일 입출력, 경로 처리 등).

폴더:

images/: 입력 및 출력 이미지 저장(예: 샘플, 결과 이미지 등).

tests/: 유닛 테스트 코드 저장.

plugs/: 외부 플러그인(확장 기능) 저장.

3. 사용 라이브러리
필수 라이브러리:

opencv-python: 이미지 처리 핵심 라이브러리.

numpy: 배열 및 수치 연산.

Pillow: 이미지 파일 포맷 지원 및 추가 이미지 처리.

(선택) tkinter: GUI 구현 시 사용.

모든 의존성은 requirements.txt에 최신 호환 버전으로 기록.

예시:

python
import cv2
import numpy as np
from PIL import Image
4. 코드 작성 규칙
언어: Python 3.x

주석: 모든 주석은 한글로 작성

코드 재사용성:

공통 기능은 별도 모듈(utils.py 등)로 분리

재사용 가능한 함수/클래스는 명확한 이름과 한글 주석 포함

중복 코드 최소화, 모듈화된 구조 사용

명명 규칙:

파일/폴더: 소문자와 언더스코어 사용(예: image_processor.py)

함수/변수: PEP 8 준수, 명확하고 설명적인 이름

에러 처리: 예외 처리로 안정성 보장

의존성 관리: requirements.txt에 정확한 버전 명시

5. 이미지 처리 설정
입출력: images/ 폴더에서 이미지 파일을 읽고 저장

처리: image_processor.py에서 이미지 불러오기, 변환, 저장, 시각화 등 구현

예시 기능: 그레이스케일 변환, 블러링, 엣지 검출, 채널 분리, 이미지 합성 등

6. UI(선택사항)
Tkinter를 사용할 경우:

왼쪽 패널(10%): 파일 열기/저장, 필터 선택 등

가운데 패널(80%): 이미지 미리보기 및 처리 결과 표시

오른쪽 패널(10%): 이미지 정보(크기, 채널, 포맷 등) 표시

이미지 처리:

OpenCV로 이미지 처리 후, Pillow와 연동하여 Tkinter에 표시 가능

이미지 파일명은 명확하게(예: sample_input.jpg, result_edge.png)

7. 모듈별 역할
main.py: 애플리케이션 실행 및 진입점, 최소한의 코드로 핵심 로직 호출

image_processor.py: 이미지 처리 함수(예: def to_gray(img): ...) 및 클래스 정의

utils.py: 파일 입출력, 경로 처리 등 공통 유틸리티 함수

tests/: 유닛 테스트 코드(test_image_processor.py 등)

images/: 입력 및 출력 이미지 저장

plugs/: 외부 플러그인 관리, 동적 로드 구현 가능

8. 구현 세부사항
스레딩: 대용량 이미지 처리나 UI 응답성 개선이 필요할 때 threading 사용

파일 선택: Tkinter의 filedialog로 이미지 파일 선택 기능 제공 가능

의존성 설치: pip install -r requirements.txt

실행: python main.py로 애플리케이션 시작

9. 추가 고려사항
보안: 외부 플러그인 로드 시 안전성 검증, 이미지 파일 유효성 검사

확장성: 새로운 플러그인 추가를 위한 모듈 로더 구현, 함수/클래스 분리 철저

디버깅: logging 모듈로 로깅 추가, 에러 발생 시 콘솔 출력

10. 작업 흐름
images/와 plugs/ 폴더 생성

requirements.txt 작성 및 의존성 설치

image_processor.py로 이미지 처리 기능 구현

main.py로 실행 코드 작성

(필요시) tests/에 테스트 코드 작성

테스트 및 디버깅
