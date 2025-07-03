```markdown
# OpenCV Python 개발을 위한 Windsurf Rules

이 가이드는 OpenCV를 사용해 Python으로 이미지/비디오 처리 프로그램을 개발하기 위한 **Windsurf Rules**를 체계적으로 정리한 문서입니다. 이미지 필터링, 객체 탐지, 실시간 웹캠 처리 등 컴퓨터 비전 작업을 다루며, 초보자와 팀 프로젝트를 모두 고려해 작성되었습니다. 새로운 XML 태그를 추가해 OpenCV의 특성을 반영하며, 유연성과 확장성을 제공합니다.

---

## 📖 Windsurf Rules란?

**Windsurf Rules**는 Python 프로젝트에서 코드 작성, 구조, 동작 방식을 표준화하기 위한 규칙 문서입니다. OpenCV에서는 이미지/비디오 처리, 객체 탐지, 시각화 등을 효율적으로 구현하도록 돕습니다.

### 쉬운 설명
- **비유**: 요리 레시피처럼, OpenCV 프로그램을 만들 때 어떤 도구(cv2, numpy)를 사용하고, 어떤 순서로 처리할지, 결과를 어떻게 저장할지 가이드합니다.
- **왜 필요?**: 코드 일관성을 유지하고, 팀 협업을 원활하게 하며, 유지보수를 쉽게 합니다.
- **어떻게 사용?**: `.windsurf/rules/` 디렉토리에 `.md` 파일로 저장하고, 특정 파일이나 작업에 규칙을 적용합니다.

---

## 📋 기본 구조

### 1. 파일 헤더
```markdown
# OpenCV Python 프로그램

<coding_guidelines>
- 환경: Python 3.10, OpenCV (cv2) 4.8.0 이상
- 대상: OpenCV 초보자 및 중급자
- 제약: numpy, matplotlib 사용 가능, 표준 라이브러리 우선
- 주석: 모든 함수에 Google 스타일 docstring 필수
</coding_guidelines>
```

### 2. 핵심 XML 태그
- `<environment_setup>`: OpenCV 설치 및 환경 설정
- `<image_processing>`: 이미지/비디오 처리 로직
- `<input_output>`: 이미지/비디오 입출력 규칙
- `<visualization>`: 결과 시각화 및 저장
- `<error_handling>`: 예외 처리 및 사용자 피드백
- `<testing_requirements>`: 단위 테스트 및 검증
- `<documentation_requirements>`: README 및 문서화
- `<performance_requirements>`: 성능 최적화

---

## 🎯 OpenCV Python 개발 템플릿

```markdown
# OpenCV Python 프로그램

<coding_guidelines>
- 환경: Python 3.10, OpenCV (cv2) 4.8.0 이상, numpy, matplotlib
- 대상: OpenCV 초보자 및 중급자
- 제약: 메모리 효율적 처리, 표준 이미지 포맷 사용
- 주석: 모든 함수에 Google 스타일 docstring 필수
- PEP 8 준수, 최대 줄 길이 100자
</coding_guidelines>

<environment_setup>
- 설치: pip install opencv-python numpy matplotlib
- 운영체제: Ubuntu 22.04 또는 Windows 10/11 권장
- 의존성: numpy 1.23 이상, matplotlib 3.5 이상
- 확인: import cv2; print(cv2.__version__)
</environment_setup>

<image_processing>
- 처리: 이미지/비디오를 numpy 배열로 처리
- 색상 공간: BGR 기본, RGB/HSV 변환 명시
- 필터: GaussianBlur, Canny, thresholding 등 사용
- 검증: 이미지 크기, 채널 수 확인
</image_processing>

<input_output>
- 입력: JPG, PNG, MP4 포맷 지원
- 출력: JPG, PNG (이미지), AVI, MP4 (비디오)
- 경로: ./data/input/, ./data/output/
- 파일명: 소문자, 언더스코어 사용 (예: input_image.jpg)
</input_output>

<visualization>
- 라이브러리: matplotlib 또는 cv2.imshow
- 표시: 창 크기 조정 가능, 창 이름 명시
- 저장: PNG (이미지), MP4 (비디오), 최소 300dpi
- 색상: BGR → RGB 변환 필수 (matplotlib 사용 시)
</visualization>

<error_handling>
- 예외: cv2.error, FileNotFoundError, ValueError 처리
- 메시지: 사용자 친화적 에러 메시지 (예: "이미지 파일을 찾을 수 없습니다")
- 로깅: logging 모듈 사용, INFO/ERROR 수준
</error_handling>

<testing_requirements>
- 테스트 도구: pytest 사용
- 테스트 케이스: 이미지 로드, 처리, 출력 확인
- 파일: test_*.py, 최소 80% 커버리지
- 모의 데이터: 테스트용 샘플 이미지/비디오
</testing_requirements>

<documentation_requirements>
- README: 프로젝트 개요, 설치, 사용 예시
- docstring: 함수의 입력, 출력, 예외 설명
- 예시: 샘플 이미지/비디오 처리 결과 포함
</documentation_requirements>

<performance_requirements>
- 메모리: 이미지당 500MB 이하 목표
- 처리 시간: 1초 이내 (단일 이미지 기준)
- 최적화: numpy 벡터화, 멀티스레딩 (threading 사용)
</performance_requirements>

**활성화 모드**: Glob - *opencv*.py, *vision*.py
**활성화 모드**: Model Decision - "OpenCV 이미지/비디오 처리 요청 시"
```

---

## 🛠️ 작성 Best Practices

### ✅ 해야 할 것
1. **구체적으로**:
   ```markdown
   ❌ "이미지 처리"
   ✅ "cv2.imread로 이미지 로드, cv2.cvtColor로 BGR→RGB 변환"
   ```
2. **XML 태그로 구조화**:
   ```xml
   <image_processing>
   - 필터: cv2.GaussianBlur, kernel=(5,5)
   - 검출: cv2.Canny, threshold1=100, threshold2=200
   </image_processing>
   ```
3. **OpenCV 표준 준수**:
   - 설치: `pip install opencv-python`
   - 색상: BGR 기본, matplotlib 사용 시 RGB 변환
   - 저장: `cv2.imwrite`로 이미지 저장

### ❌ 피해야 할 것
1. **모
