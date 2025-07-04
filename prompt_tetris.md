
# 게임 개발 도구

<coding_guidelines>
- 환경: Python 3.10 + Pygame
- 대상: 게임 개발 입문자
- 제약: 60FPS 유지, 메모리 누수 방지
- 주석: 객체지향 구조 설명 필수
</coding_guidelines>

<game_structure>
- 게임 루프: update-render 패턴
- 객체: 스프라이트 기반 클래스
- 씬 관리: 시작, 게임, 종료 화면
- 입력: 키보드, 마우스 처리
</game_structure>

<graphics_requirements>
- 해상도: 800x600 기본
- 스프라이트: PNG, 최대 256x256
- 애니메이션: 초당 30프레임
- 최적화: 화면 갱신 최소화
</graphics_requirements>

<game_mechanics>
- 충돌 감지: AABB 알고리즘
- 점수: 실시간 업데이트
- 상태: 시작, 플레이, 일시정지, 종료
- 사운드: WAV 포맷, 볼륨 0.5
</game_mechanics>

<testing_requirements>
- 단위 테스트: 충돌 감지, 점수 계산
- 테스트 케이스: 경계값, 비정상 입력
- 테스트 파일: test_*.py
</testing_requirements>

<accessibility_requirements>
- 키보드: 방향키로 게임 조작 가능
- 색상: 고대비 팔레트 (WCAG 2.1 준수)
- 사운드: 자막 옵션 추가
</accessibility_requirements>

<explainable_code_prompt>
- **목적**: 사용자가 작성(또는 생성)한 프로그램을 LLM이 쉽게 분석, 전체 구조와 동작 원리를 시각적으로(텍스트 다이어그램 포함) 설명
- **출력 요구**:
    1. **전체 구조 요약**: 주요 모듈, 함수, 데이터 흐름, 책임 분리 등 한눈에 보기
    2. **핵심 로직 설명**: 각 함수/클래스별 역할, 파라미터, 반환값, 내부 동작
    3. **흐름도/다이어그램**: 텍스트 기반(예: 트리, 순서도)로 시각화
    4. **실행 순서 예시**: 실제 입력/출력 흐름 예시
    5. **초보자 친화적 설명**: 쉬운 용어, 비유, 예시 활용
- **코드와 설명 구분**:  
    - `### 코드`  
    - `### 구조 요약`  
    - `### 함수별 설명`  
    - `### 흐름도`  
    - `### 실행 예시`
- **주석**: 코드 내 핵심 부분 주석 필수
- **에러/예외 처리**: 주요 예외 상황과 처리 방법도 설명
- 저장: program_examples.md 로 저장
<prompt_example>

**활성화 모드**: Glob - *_game.py, game_*.py
