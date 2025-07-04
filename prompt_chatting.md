# 웹 채팅 프로그램 (Tornado 기반)

<coding_guidelines>
- 환경: Python 3.10 + Tornado
- 대상: 웹 개발 및 네트워크 프로그래밍 초보자
- 제약: 표준 라이브러리와 Tornado만 사용, IP 대역 192.168.0.x 제한
- 주석: WebSocket 로직과 비동기 처리 상세히 설명
</coding_guidelines>

<web_structure>
- 프레임워크: Tornado
- URL 라우팅: /chat (WebSocket 엔드포인트)
- 포트: 8888
- 정적 파일: HTML, CSS, JS (정적 디렉토리 설정)
</web_structure>

<network_requirements>
- 프로토콜: WebSocket
- 서버: 비동기 처리, 다중 클라이언트 지원
- IP 필터: 192.168.0.x 대역만 허용
- 데이터: JSON 포맷 (예: {"type": "login", "nickname": "user"})
</network_requirements>

<login_process>
- 인증: 1차적으로 닉네임 입력만 요구
- 닉네임 규칙: 3~20자, 알파벳/숫자만 허용
- 초기화: 로그인 성공 시 대화방 목록 표시
- 에러: 중복 닉네임 시 경고 메시지 ("닉네임이 이미 사용 중입니다")
</login_process>

<chatroom_features>
- 다중 대화방: 최소 3개 방 (예: General, Tech, Random)
- 방 전환: 클라이언트에서 선택 가능, 실시간 업데이트
- 메시지 표시: "[방이름] [닉네임]: 메시지" 형식
- 사용자 목록: 연결된 사용자 실시간 표시 (옵션)
</chatroom_features>

<client_ui>
- HTML: 채팅 창, 입력창, 대화방 선택 드롭다운
- CSS: 고대비 색상 (검정/흰 배경), 반응형 디자인
- JavaScript: WebSocket 연결, 메시지 전송/수신 처리
- 컴포넌트: 닉네임 입력, 메시지 입력, 전송 버튼
</client_ui>

<error_handling>
- ConnectionError: "서버에 연결할 수 없습니다"
- ValueError: "잘못된 닉네임 형식입니다"
- WebSocketError: "연결이 끊겼습니다"
- 사용자 피드백: 클라이언트에 알림 표시
</error_handling>

<testing_requirements>
- 테스트: 로그인, 메시지 전송, 대화방 전환
- pytest 사용, 최소 70% 커버리지
- 테스트 파일: test_chat.py
- 모의 데이터: WebSocket 모의 서버
</testing_requirements>

<documentation_requirements>
- README: 설치, 실행 방법, 웹 접속 URL
- docstring: 주요 함수 (예: on_message, send_message)
- 네트워크 흐름: 텍스트 다이어그램 포함
</documentation_requirements>

<performance_requirements>
- 응답 시간: 500ms 이내
- 동시 사용자: 최대 50명
- 메모리: 300MB 이하 유지
</performance_requirements>

<accessibility_requirements>
- 키보드: Enter로 메시지 전송 가능
- 색상: WCAG 2.1 준수 (고대비 팔레트)
- 다국어: 기본 영어, 옵션 한국어 지원
</accessibility_requirements>

**활성화 모드**: Glob - *webchat*.py, chat_*.py
