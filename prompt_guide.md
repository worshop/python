# Windsurf Rules 작성 완전 가이드

이 가이드는 Python 프로그램 개발을 위한 **Windsurf Rules** 작성 방법을 체계적으로 정리한 최종 버전입니다. 기존 가이드를 바탕으로 테스트, 문서화, 성능, 협업, 접근성 등 추가 요소를 포함해 완성도를 높였습니다. 초보자도 이해하기 쉽게 간단한 설명과 구체적인 예시를 추가했습니다.

---

## 📖 Windsurf Rules란?

**Windsurf Rules**는 Python 프로젝트를 개발할 때 코드 작성, 구조, 동작 방식을 표준화하기 위한 규칙을 정의하는 문서입니다. 이를 통해 코드 품질을 높이고, 팀원 간 협업을 원활하게 하며, 유지보수를 쉽게 할 수 있습니다. 규칙은 Markdown 형식으로 작성되며, XML 태그를 사용해 구조화됩니다.

### 쉬운 설명
- **비유**: Windsurf Rules는 요리 레시피와 비슷합니다. 요리(프로그램)를 만들 때 어떤 재료(Python, 라이브러리)를 사용하고, 어떤 순서로 조리(코딩)할지, 어떤 접시에 담을지(UI, 출력)를 명확히 알려주는 가이드입니다.
- **왜 필요?**: 팀 프로젝트나 복잡한 프로그램에서 일관된 코드를 작성하고, 오류를 줄이며, 다른 사람이 코드를 쉽게 이해하도록 돕습니다.
- **어떻게 사용?**: 프로젝트 폴더에 `.windsurf/rules/` 디렉토리를 만들고, `.md` 파일로 규칙을 작성합니다. 특정 파일이나 작업에 규칙을 적용하도록 설정합니다.

---

## 📋 기본 구조

### 1. 파일 헤더
- **역할**: 프로그램의 기본 정보와 코딩 가이드라인 정의
- **형식**:
  ```markdown
  # [프로그램명]

  <coding_guidelines>
  - 환경: Python 3.10, [사용 라이브러리]
  - 대상: [초보자/중급자/고급자]
  - 제약: [사용 가능한 라이브러리, 제한 조건]
  - 주석: [대상자 수준에 맞는 주석 필수]
  </coding_guidelines>
  ```

### 2. 핵심 XML 태그
- **데이터 구조** (`<data_structure>`): 데이터 저장 방식, 타입, 검증 규칙
- **UI 요구사항** (`<gui_requirements>`): UI 프레임워크, 컴포넌트, 사용자 상호작용
- **파일 처리** (`<file_operations>`): 파일 입출력, 형식, 저장/불러오기
- **에러 처리** (`<error_handling>`): 예외 상황, 에러 메시지, 사용자 피드백
- **추가 태그**:
  - `<testing_requirements>`: 단위 테스트, 커버리지, 테스트 케이스
  - `<documentation_requirements>`: README, API 문서, 주석
  - `< Ame_requirements>`: 실행 시간, 메모리 사용 최적화
  - `<version_control>`: Git 브랜치 전략, 커밋 메시지
  - `<accessibility_requirements>`: 다국어, 접근성 지원

---

## 🎯 프로그램 유형별 템플릿

### 📊 데이터 분석 프로그램
```markdown
# 데이터 분석 도구

<coding_guidelines>
- 환경: Python 3.10 + Pandas, NumPy, Matplotlib, Seaborn
- 대상: 데이터 분석 초보자
- 제약: 메모리 효율성 고려, 1GB 이상 데이터셋 처리 가능
- 주석: 모든 함수에 Google 스타일 docstring 필수
</coding_guidelines>

<data_processing>
- 파일 형식: CSV, Excel 우선
- 결측값: 평균/중앙값 대체 또는 삭제
- 데이터 검증: 타입 체크, 범위 검증
- 처리: chunk 단위 처리로 메모리 절약
</data_processing>

<visualization_requirements>
- 라이브러리: Matplotlib, Seaborn
- 그래프: 막대, 선, 산점도, 히스토그램
- 색상: 고대비 팔레트, 다크/라이트 테마 호환
- 저장: PNG, PDF (최소 300dpi)
</visualization_requirements>

<analysis_features>
- 기술통계: 평균, 중앙값, 표준편차
- 상관관계: Pearson/Spearman 분석
- 그룹별 분석: groupby 사용
- 트렌드 분석: 이동평균 계산
</analysis_features>

<testing_requirements>
- pytest 사용, 최소 80% 커버리지
- 테스트 케이스: 정상/결측값/잘못된 입력
- 테스트 파일: test_*.py
</testing_requirements>

<documentation_requirements>
- README: 프로젝트 개요, 설치, 사용 예시
- 함수 docstring: 입력, 출력, 예외 설명
- 데이터 구조 문서화: 데이터프레임 스키마 포함
</documentation_requirements>

**활성화 모드**: Glob - *_analysis.py, *_data.py
```

### 🎮 게임 프로그램
```markdown
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

**활성화 모드**: Glob - *_game.py, game_*.py
```

### 🌐 웹 스크래핑 프로그램
```markdown
# 웹 스크래핑 도구

<coding_guidelines>
- 환경: Python 3.10 + requests, BeautifulSoup4
- 대상: 웹 스크래핑 초보자
- 제약: robots.txt 준수, 요청 간격 1초
- 주석: 파싱 로직 상세히 설명
</coding_guidelines>

<scraping_rules>
- 헤더: User-Agent 설정 필수
- 요청: 최소 1초 간격, 타임아웃 10초
- 세션: 로그인 필요한 사이트 지원
- 오류: 네트워크/파싱 오류 처리
</scraping_rules>

<data_extraction>
- 파싱: BeautifulSoup4, CSS 선택자 우선
- 검증: 데이터 형식, 중복 제거
- 저장: JSON 기본, CSV 옵션
</data_extraction>

<output_format>
- JSON: 구조화된 데이터 저장
- CSV: UTF-8 인코딩, 헤더 포함
- 진행바: tqdm 라이브러리 사용
- 로그: 텍스트 파일로 기록
</output_format>

<testing_requirements>
- 테스트: HTML 파싱, 데이터 검증
- 모의 데이터: 테스트용 HTML 파일 사용
- 테스트 파일: test_*.py
</testing_requirements>

<performance_requirements>
- 요청 최적화: 최대 100개 동시 요청
- 메모리: 500MB 이하 유지
- 비동기: asyncio 고려
</performance_requirements>

**활성화 모드**: Glob - *_scraper.py, scrape_*.py
```

### 🔐 보안 도구
```markdown
# 보안 분석 도구

<coding_guidelines>
- 환경: Python 3.10 + cryptography, hashlib
- 대상: 보안 초보자
- 제약: 표준 라이브러리 우선, 안전한 랜덤 생성
- 주석: 보안 로직 상세히 작성
</coding_guidelines>

<security_features>
- 해싱: bcrypt (비밀번호), SHA-256 (파일)
- 암호화: AES-256, 키 관리 필수
- 랜덤: secrets 모듈 사용
- 입력: 새니타이징 필수
</security_features>

<file_security>
- 권한: 최소 권한 원칙
- 임시 파일: tempfile 모듈 사용
- 민감 데이터: 메모리에서 즉시 삭제
- 로그: 민감 정보 기록 금지
</file_security>

<audit_features>
- 로그: 모든 작업 기록 (타임스탬프 포함)
- 무결성: 파일 해시 검증
- 스캔: 취약점 탐지 기능
</audit_features>

<testing_requirements>
- 테스트: 해싱, 암호화, 무결성 체크
- 케이스: 잘못된 키, 손상된 파일
- 테스트 파일: test_*.py
</testing_requirements>

**활성화 모드**: Glob - *_security.py, security_*.py
```

### 🖥️ API 서버 프로그램
```markdown
# API 서버 도구

<coding_guidelines>
- 환경: Python 3.10 + FastAPI, SQLAlchemy
- 대상: 백엔드 개발 초보자
- 제약: RESTful API 원칙 준수
- 주석: 엔드포인트별 설명 필수
</coding_guidelines>

<api_structure>
- 엔드포인트: /create, /read, /update, /delete
- 인증: JWT 토큰 사용
- 데이터베이스: SQLite 기본, PostgreSQL 옵션
- 응답: JSON 포맷, 상태 코드 명시
</api_structure>

<request_handling>
- 입력 검증: Pydantic 모델 사용
- 요청 제한: 초당 100 요청
- 에러 응답: HTTP 상태 코드 및 메시지
</request_handling>

<performance_requirements>
- 응답 시간: 200ms 이내 목표
- 비동기: async/await 사용
- 캐싱: Redis 고려
</performance_requirements>

<testing_requirements>
- 테스트: 엔드포인트별 CRUD 테스트
- 모의 데이터: 테스트 DB 사용
- 테스트 파일: test_*.py
</testing_requirements>

<documentation_requirements>
- API 문서: FastAPI 자동 문서 (/docs)
- README: API 사용법, 인증 방법
- 주석: 엔드포인트 목적 설명
</documentation_requirements>

**활성화 모드**: Glob - *_api.py, api_*.py
```

### 📱 간단한 CLI 도구
```markdown
# CLI 유틸리티 도구

<coding_guidelines>
- 환경: Python 3.10 + argparse
- 대상: CLI 초보자
- 제약: 표준 라이브러리만 사용
- 주석: 명령어 옵션 설명 필수
</coding_guidelines>

<cli_structure>
- 명령어: 최소 3개 이상 옵션
- 입력: argparse로 파싱
- 출력: 콘솔에 깔끔한 포맷
</cli_structure>

<error_handling>
- 잘못된 입력: 사용자 친화적 메시지
- 예외: SystemExit으로 종료
- 로그: 선택적 파일 출력
</error_handling>

<testing_requirements>
- 테스트: 명령어 옵션별 동작 확인
- 모의 입력: sys.argv 모킹
- 테스트 파일: test_*.py
</testing_requirements>

**활성화 모드**: Glob - *_cli.py, cli_*.py
```

---

## 🛠️ 작성 Best Practices

### ✅ 해야 할 것
1. **구체적으로**:
   ```markdown
   ❌ "좋은 코드"
   ✅ "함수명: snake_case, 클래스명: PascalCase"
   ```
2. **XML 태그로 구조화**:
   ```xml
   <database_operations>
   - SQLite, 연결 풀링
   - 트랜잭션 관리
   </database_operations>
   ```
3. **명시적 API 사용**:
   ```markdown
   - 파일 선택: tkinter.filedialog.askopenfilename
   - 에러 메시지: messagebox.showerror
   ```

### ❌ 피해야 할 것
1. **모호한 표현**:
   ```markdown
   ❌ "효율적인 코드"
   ❌ "사용자 친화적 UI"
   ```
2. **너무 긴 규칙**: 12,000자 제한 준수
3. **일반적 지침**:
   ```markdown
   ❌ "PEP 8 준수"
   ```

---

## 🎯 활성화 모드 선택 가이드
- **Glob 패턴**:
  ```markdown
  **활성화 모드**: Glob - *.py                 # 모든 Python 파일
  **활성화 모드**: Glob - test_*.py            # 테스트 파일
  **활성화 모드**: Glob - src/**/*.py          # src 폴더
  **활성화 모드**: Glob - *.ipynb              # Jupyter Notebook
  ```
- **Model Decision**:
  ```markdown
  **활성화 모드**: Model Decision - "데이터 시각화 요청 시"
  **활성화 모드**: Model Decision - "머신러닝 모델 학습 시"
  ```
- **Always On**: 신중히 사용
  ```markdown
  **활성화 모드**: Always On
  ```

---

## 📝 완성된 규칙 예시

### 1. 간단한 계산기 프로그램
```markdown
# 계산기 프로그램

<coding_guidelines>
- 환경: Python 3.10 + tkinter
- 대상: Python 초보자
- 제약: 표준 라이브러리만 사용
- 주석: 모든 함수에 docstring
</coding_guidelines>

<gui_structure>
- 창 크기: 300x400
- 버튼: 0-9, +, -, *, /, =, C (3x4 그리드)
- 결과: Entry 위젯, 읽기 전용
</gui_structure>

<calculation_rules>
- 소수점: 최대 2자리
- 0 나누기: 에러 처리
- 연속 계산: 지원
- 표시: 최대 10자리
</calculation_rules>

<error_handling>
- ZeroDivisionError: "0으로 나눌 수 없습니다"
- OverflowError: "결과가 너무 큽니다"
- 잘못된 입력: "숫자를 입력하세요"
</error_handling>

<testing_requirements>
- 테스트: 계산 결과, 에러 케이스
- pytest 사용, test_calculator.py
</testing_requirements>

**활성화 모드**: Glob - *calculator*.py
```

### 2. CSV 데이터 정리 도구
```markdown
# CSV 데이터 정리 도구

<coding_guidelines>
- 환경: Python 3.10 + Pandas
- 대상: 데이터 분석 초보자
- 제약: 최대 500MB CSV 파일 처리
- 주석: 데이터 처리 단계별 설명
</coding_guidelines>

<data_processing>
- 입력: CSV 파일 (UTF-8)
- 결측값: 삭제 또는 0으로 대체
- 검증: 숫자 컬럼은 float/int, 문자열은 str
- 출력: 정제된 CSV
</data_processing>

<error_handling>
- FileNotFoundError: "파일을 찾을 수 없습니다"
- ValueError: "잘못된 데이터 형식입니다"
</error_handling>

<testing_requirements>
- 테스트: 결측값 처리, 데이터 검증
- pytest 사용, test_csv_cleaner.py
</testing_requirements>

<documentation_requirements>
- README: 사용법, 입력/출력 예시
- docstring: 주요 함수 설명
</documentation_requirements>

**활성화 모드**: Glob - *csv_cleaner*.py
```

### 3. 간단한 To-Do 리스트 CLI
```markdown
# To-Do 리스트 CLI

<coding_guidelines>
- 환경: Python 3.10 + argparse, json
- 대상: CLI 초보자
- 제약: 표준 라이브러리만 사용
- 주석: 명령어 로직 설명
</coding_guidelines>

<cli_structure>
- 명령어: add, list, remove, clear
- 저장: JSON 파일 (todo.json)
- 출력: 목록은 테이블 형식
</cli_structure>

<error_handling>
- 잘못된 명령: "유효한 명령어를 입력하세요"
- 파일 오류: "데이터 파일을 읽/쓸 수 없습니다"
</error_handling>

<testing_requirements>
- 테스트: 명령어 동작, JSON 저장
- pytest 사용, test_todo.py
</testing_requirements>

**활성화 모드**: Glob - *todo*.py
```

---

## 🚀 규칙 적용 및 관리

### 1. 파일 저장
```
프로젝트 루트/
├── .windsurf/
│   └── rules/
│       ├── python_general.md
│       ├── data_analysis.md
│       ├── gui_apps.md
│       ├── api_servers.md
│       ├── cli_tools.md
```

### 2. 규칙 확인
- Python 파일 생성 후 Cascade로 테스트
- 규칙 적용 확인 후 수정

### 3. 최적화
- **제한적 규칙**: 완화
- **느슨한 규칙**: 구체화
- **피드백**: 사용자 경험 반영

---

## 💡 추가 팁

### 메모리 관리
- 파일당 12,000자 제한
- 핵심 규칙 우선 작성
- 불필요한 설명 제거

### 유지보수
- 정기 검토 및 업데이트
- 팀과 공유
- 변경 로그 유지

### 성능 최적화
- 규칙 파일 통합
- 활성화 조건 최소화
- 비동기/캐싱 고려

---

## 🌟 최종 점검
이 가이드는 다음을 충족합니다:
- **완전성**: 데이터 분석, 게임, 웹 스크래핑, 보안, API, CLI 등 다양한 유형 포함
- **구체성**: 모호한 표현 제거, 명확한 예시 제공
- **유연성**: 테스트, 문서화, 접근성 등 추가 요소로 확장 가능
- **실용성**: 초보자부터 팀 프로젝트까지 활용 가능

이제 이 가이드를 사용해 어떤 Python 프로젝트든 체계적이고 효율적인 Windsurf Rules를 작성할 수 있습니다!
