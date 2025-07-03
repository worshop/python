```markdown
# ROS 2 Humble Python 개발을 위한 Windsurf Rules

이 가이드는 ROS 2 Humble에서 Python으로 로봇 애플리케이션을 개발하기 위한 **Windsurf Rules**를 체계적으로 정리한 문서입니다. 노드, 토픽, 서비스, 액션 등 ROS 2의 핵심 요소를 다루며, 초보자와 팀 프로젝트를 모두 고려해 명확하고 실용적으로 작성되었습니다. 새로운 XML 태그를 추가해 ROS 2의 특성을 반영하며, 유연성과 확장성을 제공합니다.

---

## 📖 Windsurf Rules란?

**Windsurf Rules**는 Python 프로젝트에서 코드 작성, 구조, 동작 방식을 표준화하기 위한 규칙 문서입니다. ROS 2 Humble에서는 노드(Node), 토픽(Topic), 서비스(Service), 액션(Action) 등을 효율적으로 구현하도록 돕습니다.

### 쉬운 설명
- **비유**: 요리 레시피처럼, ROS 2 프로그램을 만들 때 어떤 도구(Python, rclpy)를 사용하고, 어떤 순서로 개발할지, 결과를 어떻게 확인할지 가이드합니다.
- **왜 필요?**: 코드 일관성을 유지하고, 팀 협업을 원활하게 하며, 유지보수를 쉽게 합니다.
- **어떻게 사용?**: `.windsurf/rules/` 디렉토리에 `.md` 파일로 저장하고, 특정 파일이나 작업에 규칙을 적용합니다.

---

## 📋 기본 구조

### 1. 파일 헤더
- **역할**: 프로그램의 기본 정보와 코딩 가이드라인 정의
- **형식**:
  ```markdown
  # [프로그램명]

  <coding_guidelines>
  - 환경: Python 3.10, ROS 2 Humble
  - 대상: [초보자/중급자]
  - 제약: rclpy 사용, ROS 2 패키지 구조 준수
  - 주석: Google 스타일 docstring 필수
  </coding_guidelines>
  ```

### 2. 핵심 XML 태그
- `<ros_environment>`: ROS 2 워크스페이스 및 빌드 설정
- `<package_config>`: ROS 2 패키지 설정 (package.xml, setup.py)
- `<node_structure>`: 노드 구성 및 역할
- `<topic_rules>`: 토픽 퍼블리셔/서브스크라이버 설정
- `<service_rules>`: 서비스 서버/클라이언트 설정
- `<action_rules>`: 액션 서버/클라이언트 설정
- `<error_handling>`: 예외 처리 및 로깅
- `<testing_requirements>`: 단위/통합 테스트
- `<documentation_requirements>`: README 및 문서화
- `<performance_requirements>`: 성능 최적화

---

## 🎯 ROS 2 Humble Python 개발 템플릿

```markdown
# ROS 2 Humble Python 패키지

<coding_guidelines>
- 환경: Python 3.10, ROS 2 Humble, Ubuntu 22.04
- 대상: ROS 2 초보자 및 중급자
- 제약: rclpy 사용, 표준 ROS 2 패키지 구조 준수
- 주석: 모든 노드, 함수에 Google 스타일 docstring 필수
- PEP 8 준수, 최대 줄 길이 100자
</coding_guidelines>

<ros_environment>
- 워크스페이스: ~/ros2_ws/src/
- 소싱: source /opt/ros/humble/setup.bash
- 빌드: colcon build --symlink-install
- 의존성: rosdep install로 해결
</ros_environment>

<package_config>
- 패키지 생성: ros2 pkg create --build-type ament_python <package_name>
- package.xml: 의존성(rclpy, std_msgs 등) 명시
- setup.py: 실행 가능 노드 entry_points 추가
- setup.cfg: 스크립트 경로 lib/<package_name>
</package_config>

<node_structure>
- 노드: rclpy.node.Node 상속
- 이름: 소문자와 언더스코어 (예: minimal_publisher)
- 타이머: 주기적 실행 시 create_timer 사용
- 로깅: self.get_logger() 사용
</node_structure>

<topic_rules>
- 퍼블리셔: create_publisher, QoS 설정 (기본: 10)
- 서브스크라이버: create_subscription, 콜백 함수 정의
- 메시지: std_msgs, sensor_msgs, geometry_msgs 등 사용
- 토픽 이름: /로 시작, 소문자와 언더스코어
</topic_rules>

<service_rules>
- 서비스: create_service, .srv 파일로 정의
- 비동기 호출: call_async 사용 권장
- 이름: /<node_name>/<service_name> 형식
</service_rules>

<action_rules>
- 액션: create_action, .action 파일로 정의
- 피드백: 주기적 피드백 전송
- 이름: /<node_name>/<action_name> 형식
</action_rules>

<error_handling>
- 예외: rclpy.exceptions, ValueError, ConnectionError 처리
- 로깅: self.get_logger().error로 에러 기록
- 사용자 메시지: 명확하고 간결한 에러 메시지
</error_handling>

<testing_requirements>
- 테스트 도구: pytest, ros2 test 사용
- 테스트 케이스: 노드 동작, 토픽/서비스 통신
- 파일: test_*.py, 최소 80% 커버리지
</testing_requirements>

<documentation_requirements>
- README: 패키지 개요, 설치, 실행 예시
- docstring: 노드, 함수, 클래스에 입력/출력/예외 설명
- ROS 2 문서: ros2 interface show로 메시지/서비스 문서화
</documentation_requirements>

<performance_requirements>
- QoS: 신뢰성(reliable) 또는 베스트 에포트 설정
- 메모리: 노드당 500MB 이하 목표
- 비동기: async/await로 서비스 호출 최적화
</performance_requirements>

**활성화 모드**: Glob - *.py, exclude: test_*.py
**활성화 모드**: Model Decision - "ROS 2 노드 개발 요청 시"
```

---

## 🛠️ 작성 Best Practices

### ✅ 해야 할 것
1. **구체적으로**:
   ```markdown
   ❌ "ROS 2 노드 작성"
   ✅ "rclpy.node.Node 상속, create_publisher로 토픽 생성"
   ```
2. **XML 태그로 구조화**:
   ```xml
   <topic_rules>
   - 퍼블리셔: create_publisher, QoS 10
   - 토픽 이름: /<node_name>/<topic>
   </topic_rules>
   ```
3. **ROS 2 표준 준수**:
   - 패키지 생성: `ros2 pkg create --build-type ament_python`
   - 환경 소싱: `source /opt/ros/humble/setup.bash`
   - 빌드: `colcon build --symlink-install`

### ❌ 피해야 할 것
1. **모호한 표현**:
   ```markdown
   ❌ "좋은 ROS 2 코드"
   ❌ "효율적인 노드"
   ```
2. **잘못된 환경 설정**:
   - Python 3.8 사용 금지 (Humble은 Python 3.10 요구)
   - conda 사용 시 시스템 인터프리터 불일치 주의
3. **과도한 규칙**: 12,000자 제한 준수

---

## 🎯 활성화 모드 선택 가이드
- **Glob 패턴**:
  ```markdown
  **활성화 모드**: Glob - *.py                # 모든 Python 파일
  **활성화 모드**: Glob - *node*.py           # 노드 관련 파일
  **활성화 모드**: Glob - src/**/*.py         # src 폴더 내 Python 파일
  ```
- **Model Decision**:
  ```markdown
  **활성화 모드**: Model Decision - "ROS 2 토픽 퍼블리셔/서브스크라이버 구현 시"
  **활성화 모드**: Model Decision - "ROS 2 서비스 또는 액션 개발 시"
  ```
- **Always On**: 신중히 사용
  ```markdown
  **활성화 모드**: Always On
  ```

---

## 📝 완성된 규칙 예시

### 1. 간단한 토픽 퍼블리셔/서브스크라이버
```markdown
# ROS 2 토픽 퍼블리셔/서브스크라이버

<coding_guidelines>
- 환경: Python 3.10, ROS 2 Humble, rclpy
- 대상: ROS 2 초보자
- 제약: std_msgs.msg 사용, QoS 10
- 주석: Google 스타일 docstring 필수
</coding_guidelines>

<ros_environment>
- 워크스페이스: ~/ros2_ws/src/
- 소싱: source /opt/ros/humble/setup.bash
- 빌드: colcon build --symlink-install
</ros_environment>

<package_config>
- 패키지: ros2 pkg create --build-type ament_python py_pubsub
- 의존성: rclpy, std_msgs
- setup.py: entry_points에 publisher, subscriber 추가
</package_config>

<node_structure>
- 퍼블리셔 노드: MinimalPublisher, /my_topic에 String 메시지
- 서브스크라이버 노드: MinimalSubscriber, /my_topic 구독
- 타이머: 0.5초 주기 퍼블리싱
</node_structure>

<topic_rules>
- 토픽: /my_topic, std_msgs.msg.String
- QoS: depth=10, reliable
- 콜백: 서브스크라이버에서 메시지 로깅
</topic_rules>

<error_handling>
- 예외: rclpy.exceptions.ROSInterruptException 처리
- 로깅: self.get_logger().error 사용
</error_handling>

<testing_requirements>
- 테스트: 토픽 메시지 송수신 확인
- pytest 사용, test_pubsub.py
</testing_requirements>

**활성화 모드**: Glob - *pubsub*.py
```

### 2. 서비스 서버/클라이언트
```markdown
# ROS 2 서비스 서버/클라이언트

<coding_guidelines>
- 환경: Python 3.10, ROS 2 Humble, rclpy
- 대상: ROS 2 초보자
- 제약: example_interfaces.srv 사용
- 주석: Google 스타일 docstring 필수
</coding_guidelines>

<ros_environment>
- 워크스페이스: ~/ros2_ws/src/
- 소싱: source /opt/ros/humble/setup.bash
- 빌드: colcon build --symlink-install
</ros_environment>

<package_config>
- 패키지: ros2 pkg create --build-type ament_python py_srvcli
- 의존성: rclpy, example_interfaces
- setup.py: entry_points에 service, client 추가
</package_config>

<node_structure>
- 서비스 노드: MinimalService, /add_two_ints 서비스
- 클라이언트 노드: MinimalClient, 비동기 호출
</node_structure>

<service_rules>
- 서비스: example_interfaces.srv.AddTwoInts
- 이름: /add_two_ints
- 호출: call_async 사용
</service_rules>

<error_handling>
- 예외: rclpy.exceptions.ServiceException 처리
- 로깅: self.get_logger().error 사용
</error_handling>

<testing_requirements>
- 테스트: 서비스 요청/응답 확인
- pytest 사용, test_service.py
</testing_requirements>

**활성화 모드**: Glob - *srvcli*.py
```

### 3. YOLOv8 객체 탐지 노드
```markdown
# YOLOv8 객체 탐지 노드

<coding_guidelines>
- 환경: Python 3.10, ROS 2 Humble, rclpy, ultralytics
- 대상: 컴퓨터 비전 및 ROS 2 개발자
- 제약: YOLOv8 모델 사용, sensor_msgs.msg.Image 처리
- 주석: Google 스타일 docstring 필수
</coding_guidelines>

<ros_environment>
- 워크스페이스: ~/ros2_ws/src/
- 소싱: source /opt/ros/humble/setup.bash
- 빌드: colcon build --symlink-install
- 의존성: pip install ultralytics
</ros_environment>

<package_config>
- 패키지: ros2 pkg create --build-type ament_python yolov8_node
- 의존성: rclpy, sensor_msgs, cv_bridge
- setup.py: entry_points에 yolo_node 추가
</package_config>

<node_structure>
- 노드: YoloNode, 이미지 수신 및 객체 탐지
- 입력 토픽: /camera/image_raw
- 출력 토픽: /yolo/detections
</node_structure>

<topic_rules>
- 입력: sensor_msgs.msg.Image, /camera/image_raw
- 출력: std_msgs.msg.String, /yolo/detections
- QoS: depth=10, reliable
</topic_rules>

<model_processing>
- 모델: YOLOv8 (ultralytics.YOLO)
- 전처리: cv_bridge로 ROS 이미지 변환
- 후처리: bounding box, confidence, label 추출
</model_processing>

<error_handling>
- 예외: ultralytics.YOLO 관련 오류 처리
- 로깅: self.get_logger().error 사용
</error_handling>

<testing_requirements>
- 테스트: 이미지 처리, 객체 탐지 출력
- pytest 사용, test_yolo.py
</testing_requirements>

**활성화 모드**: Glob - *yolo*.py
```

---

## 🚀 규칙 적용 및 관리

### 1. 파일 저장
```
프로젝트 루트/
├── .windsurf/
│   └── rules/
│       ├── ros2_general.md
│       ├── ros2_pubsub.md
│       ├── ros2_srvcli.md
│       ├── ros2_yolo.md
```

### 2. 규칙 확인
- 워크스페이스에서 `colcon build` 후 `ros2 run`으로 노드 실행
- `ros2 topic echo` 또는 `ros2 service call`로 동작 확인
- pytest로 테스트 실행

### 3. 최적화
- **복잡한 규칙**: 간소화 (예: 불필요한 QoS 설정 제거)
- **느슨한 규칙**: 구체화 (예: 토픽 이름 형식 명시)
- **의존성 관리**: `rosdep install`로 자동 해결

---

## 💡 추가 팁

- **환경 설정**: 항상 `source /opt/ros/humble/setup.bash` 실행
- **의존성 추가**: `package.xml`과 `setup.py`에 명시 (예: `rclpy`, `std_msgs`)
- **YOLO 통합**: YOLOv8 같은 최신 모델은 ROS 2 패키지로 바로 통합 가능
- **문서화**: `ros2 interface show`로 메시지/서비스 구조 확인
- **성능**: 비동기 호출(`call_async`)로 서비스 성능 최적화

---

## 🌟 최종 점검
이 규칙은 ROS 2 Humble Python 개발을 위한 완전한 가이드로, 다음을 충족합니다:
- **ROS 2 특화**: 노드, 토픽, 서비스, 액션 등 ROS 2 핵심 요소 반영
- **유연성**: 새로운 태그(`<model_processing>`, `<ros_environment>`)로 확장 가능
- **실용성**: 초보자와 팀 프로젝트 모두 지원
- **구체성**: 명확한 예시와 코드 제공

이제 이 규칙을 사용해 ROS 2 Humble에서 Python으로 로봇 애플리케이션을 체계적으로 개발할 수 있습니다!
```
