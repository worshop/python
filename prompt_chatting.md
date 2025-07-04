<coding_guidelines>

환경: Python 3.10, Tornado 6.4, pytest, pytest-asyncio
대상: 웹 개발 및 네트워크 프로그래밍 초보자
제약: 표준 라이브러리, Tornado, pytest 관련 라이브러리만 사용
주석: WebSocket 로직, 비동기 처리, 전역 상태 관리의 이유, 테스트 프레임워크 변경 등 주요 결정 사항을 상세히 설명 
</coding_guidelines>

<development_history>
초기 테스트 실패: pytest-tornado 사용 시 원인 불명의 TimeoutError가 지속적으로 발생.
오류 분석 및 해결 과정:
IP 필터링: 테스트 환경(localhost)이 IP 필터에 의해 차단되는 문제 발견. 127.0.0.1 및 ::1을 허용하도록 수정.
비동기 메시지 처리: 
on_message
 핸들러에서 await 누락으로 인한 경쟁 조건 발견. async def로 변경하고 await를 추가하여 해결.
연결 조기 종료: 오류 메시지 전송 직후 self.close() 호출로 인한 메시지 유실 문제 발견. 해당 로직 제거.
테스트 프레임워크 교체: 위 문제들을 해결했음에도 간헐적 시간 초과가 발생. pytest-tornado와 최신 Tornado 버전 간의 호환성 문제로 결론짓고, 공식 권장 사항인 pytest-asyncio로 전환.
상태 관리 리팩토링: pytest-asyncio 전환 후, 테스트 격리를 위한 상태 초기화 과정에서 ImportError 발생. clients, nicknames, chat_rooms를 클래스 속성에서 전역 변수로 변경하여 해결. 
</development_history>

<web_structure>
프레임워크: Tornado
URL 라우팅: /chat (WebSocket), / (정적 파일)
포트: 8888
정적 파일: static 디렉토리에서 HTML, CSS, JS 제공 </web_structure>
<network_requirements>
프로토콜: WebSocket
서버: 비동기 처리, 다중 클라이언트 지원
IP 필터: 192.168.0.x 대역과 테스트를 위한 127.0.0.1, ::1 (localhost)만 허용
데이터: JSON 포맷 (예: {"type": "login", "nickname": "user"})
상태 관리: 테스트 코드에서의 접근성 및 상태 초기화(ImportError 해결)를 위해 clients, nicknames, chat_rooms를 전역 변수로 관리. </network_requirements>

<login_process>
인증: 닉네임 입력만 요구
닉네임 규칙: 3~20자, 알파벳/숫자만 허용
초기화: 로그인 성공 시 login_success 메시지 전송
에러: 중복/유효하지 않은 닉네임 시 
error
 메시지 전송
</login_process>

<chatroom_features>
다중 대화방: General, Tech, Random
방 전환: 클라이언트에서 선택 가능, 참여/퇴장 알림 실시간 전송
메시지 표시: [방이름] [닉네임]: 메시지 형식
</chatroom_features>

<error_handling>
메시지 전송 보장: TimeoutError를 유발했던 경쟁 조건을 피하기 위해, 클라이언트에 오류 메시지 전송 후 즉시 연결을 닫지 않음.
피드백: ConnectionError, ValueError 등 주요 오류 발생 시 클라이언트에 명확한 알림 표시
</error_handling>

<testing_requirements>
테스트 프레임워크: pytest-tornado의 호환성 문제로 인해 pytest와 pytest-asyncio를 사용.
테스트 대상: 로그인, 중복 닉네임, 메시지 전송, 방 전환 등 핵심 기능
테스트 격리: 각 테스트 실행 전, 
reset_state
 픽스처를 사용해 서버의 전역 상태(clients, nicknames, chat_rooms)를 초기화
커버리지: 최소 70%
테스트 파일: 
test_chat.py
 </testing_requirements>
<documentation_requirements>

README: 설치, 실행 방법, 웹 접속 URL 명시
docstring: 주요 함수 및 
ChatWebSocket
 클래스의 각 메서드에 대한 설명 추가
아키텍처 결정: development_history에 기술된 주요 결정 사항(전역 상태 관리, 테스트 프레임워크 교체 등)을 문서에 명확히 기록 </documentation_requirements>
활성화 모드: Glob - *webchat*.py, chat_*.py
