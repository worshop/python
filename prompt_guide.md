# Windsurf Rules 작성 완전 가이드

## 📋 기본 구조

### 1. 파일 헤더
```markdown
# [프로그램명]

<coding_guidelines>
- 환경: Python 3.10 사용
- 대상: [초보자/중급자/고급자] ([구체적 설명])
- 제약: [사용 가능한 라이브러리 명시]
- 모든 코드에 [대상자]가 이해할 수 있는 주석 추가 필수
</coding_guidelines>
```

### 2. 핵심 XML 태그 구조
```xml
<data_structure>
- 데이터 저장 방식 정의
- 데이터 타입 명시
- 검증 규칙 정의
</data_structure>

<gui_requirements>
- UI 프레임워크 선택
- 필수 컴포넌트 리스트
- 사용자 상호작용 방식
</gui_requirements>

<file_operations>
- 파일 입출력 방식
- 파일 형식 정의
- 저장/불러오기 규칙
</file_operations>

<error_handling>
- 예외 상황 대응
- 에러 메시지 형식
- 사용자 피드백 방식
</error_handling>
```

---

## 🎯 프로그램 유형별 템플릿

### 📊 **데이터 분석 프로그램**
```markdown
# 데이터 분석 도구

<coding_guidelines>
- 환경: Python 3.10 + Pandas, NumPy, Matplotlib
- 대상: 데이터 분석 초보자
- 제약: 메모리 효율성 고려, 큰 데이터셋 처리
- 모든 함수에 docstring 필수
</coding_guidelines>

<data_processing>
- CSV/Excel 파일 읽기 우선
- 결측값 처리 방법 정의
- 데이터 검증 및 정제 규칙
- 메모리 효율적인 처리 방식
</data_processing>

<visualization_requirements>
- Matplotlib/Seaborn 사용
- 그래프 종류: 막대, 선, 산점도, 히스토그램
- 색상 팔레트 일관성 유지
- 그래프 저장 기능 (PNG, PDF)
</visualization_requirements>

<analysis_features>
- 기술통계 계산
- 상관관계 분석
- 그룹별 분석
- 트렌드 분석
</analysis_features>

**활성화 모드**: Glob - *_analysis.py, *_data.py
```

### 🎮 **게임 프로그램**
```markdown
# 게임 개발 도구

<coding_guidelines>
- 환경: Python 3.10 + Pygame
- 대상: 게임 개발 입문자
- 제약: 60FPS 유지, 메모리 누수 방지
- 객체지향 프로그래밍 원칙 적용
</coding_guidelines>

<game_structure>
- 게임 루프 패턴 사용
- 스프라이트 기반 객체 관리
- 씬 매니저 구현
- 입력 처리 시스템
</game_structure>

<graphics_requirements>
- 해상도: 800x600 기본
- 스프라이트 로딩 최적화
- 애니메이션 프레임 관리
- 화면 업데이트 효율성
</graphics_requirements>

<game_mechanics>
- 충돌 감지 시스템
- 점수 시스템
- 게임 상태 관리 (시작, 플레이, 일시정지, 종료)
- 사운드 효과 통합
</game_mechanics>

**활성화 모드**: Glob - *_game.py, game_*.py
```

### 🌐 **웹 스크래핑 프로그램**
```markdown
# 웹 스크래핑 도구

<coding_guidelines>
- 환경: Python 3.10 + requests, BeautifulSoup4
- 대상: 웹 스크래핑 초보자
- 제약: robots.txt 준수, 요청 간격 준수
- 예외 처리 필수 (네트워크 오류, 파싱 오류)
</coding_guidelines>

<scraping_rules>
- User-Agent 헤더 설정
- 요청 간격: 최소 1초
- 세션 관리 (로그인 필요시)
- 타임아웃 설정 (10초)
</scraping_rules>

<data_extraction>
- HTML 파싱: BeautifulSoup4 사용
- CSS 선택자 우선 사용
- 데이터 정제 및 검증
- 중복 데이터 제거
</data_extraction>

<output_format>
- JSON 형태로 데이터 저장
- CSV 내보내기 옵션
- 진행 상황 표시 (진행바)
- 로그 파일 생성
</output_format>

**활성화 모드**: Glob - *_scraper.py, scrape_*.py
```

### 🔐 **보안 도구**
```markdown
# 보안 분석 도구

<coding_guidelines>
- 환경: Python 3.10 + cryptography, hashlib
- 대상: 보안 초보자
- 제약: 표준 라이브러리 우선, 안전한 랜덤 생성
- 보안 관련 주석 상세히 작성
</coding_guidelines>

<security_features>
- 패스워드 해싱: bcrypt 사용
- 암호화: AES-256 사용
- 안전한 랜덤 생성: secrets 모듈
- 입력 검증 및 새니타이징
</security_features>

<file_security>
- 파일 권한 체크
- 안전한 임시 파일 생성
- 메모리 내 민감 데이터 처리
- 로그에 민감 정보 기록 금지
</file_security>

<audit_features>
- 작업 로그 기록
- 해시 검증 기능
- 파일 무결성 체크
- 취약점 스캔 기능
</audit_features>

**활성화 모드**: Glob - *_security.py, security_*.py
```

---

## 🛠️ 작성 Best Practices

### ✅ **DO - 해야 할 것들**

#### 1. **구체적이고 명확하게**
```markdown
❌ 나쁨: "좋은 코드 작성"
✅ 좋음: "함수명은 snake_case, 클래스명은 PascalCase 사용"

❌ 나쁨: "에러 처리"
✅ 좋음: "ValueError 발생 시 '잘못된 입력값입니다' 메시지 출력"
```

#### 2. **XML 태그로 그룹화**
```xml
<database_operations>
- SQLite 사용
- 연결 풀링 구현
- 트랜잭션 처리
</database_operations>
```

#### 3. **API 명시**
```markdown
- 파일 대화상자: tkinter.filedialog.askopenfilename
- 에러 메시지: messagebox.showerror
- 데이터 검증: isinstance(value, int) and 0 <= value <= 100
```

### ❌ **DON'T - 피해야 할 것들**

#### 1. **모호한 표현 사용**
```markdown
❌ "사용자 친화적인 인터페이스"
❌ "효율적인 코드"
❌ "적절한 에러 처리"
```

#### 2. **너무 긴 규칙 (12,000자 제한)**
```markdown
❌ 장황한 설명과 예시 코드 포함
✅ 핵심 요구사항만 간결하게
```

#### 3. **일반적인 규칙**
```markdown
❌ "좋은 코드를 작성하세요"
❌ "PEP 8을 따르세요"
```

---

## 🎯 활성화 모드 선택 가이드

### **Glob 패턴 (권장)**
```markdown
**활성화 모드**: Glob - *.py                    # 모든 Python 파일
**활성화 모드**: Glob - *_test.py, test_*.py    # 테스트 파일
**활성화 모드**: Glob - src/**/*.py             # src 폴더 내 모든 Python 파일
**활성화 모드**: Glob - *_gui.py, gui_*.py      # GUI 관련 파일
```

### **Model Decision (특정 상황)**
```markdown
**활성화 모드**: Model Decision - "데이터 시각화나 차트 생성 요청 시"
**활성화 모드**: Model Decision - "API 서버 개발 요청 시"
**활성화 모드**: Model Decision - "머신러닝 모델 구현 요청 시"
```

### **Always On (신중 사용)**
```markdown
**활성화 모드**: Always On  # 모든 작업에 적용 (신중하게 사용)
```

---

## 📝 완성된 규칙 예시

### 간단한 계산기 프로그램
```markdown
# 계산기 프로그램

<coding_guidelines>
- 환경: Python 3.10 + tkinter
- 대상: Python 초보자
- 제약: 표준 라이브러리만 사용
- 모든 함수에 docstring 추가
</coding_guidelines>

<gui_structure>
- 메인 창 크기: 300x400
- 숫자 버튼: 0-9 (3x4 그리드)
- 연산 버튼: +, -, *, /, =, C
- 결과 표시: Entry 위젯 (읽기 전용)
</gui_structure>

<calculation_rules>
- 소수점 계산 지원
- 0으로 나누기 에러 처리
- 연속 계산 지원
- 최대 10자리 수 표시
</calculation_rules>

<error_handling>
- ZeroDivisionError: "0으로 나눌 수 없습니다"
- OverflowError: "계산 결과가 너무 큽니다"
- 잘못된 입력: "올바른 숫자를 입력하세요"
</error_handling>

**활성화 모드**: Glob - *calculator*.py
```

---

## 🚀 규칙 적용 및 테스트

### 1. **파일 저장 위치**
```
프로젝트 루트/
├── .windsurf/
│   └── rules/
│       ├── python_general.md
│       ├── data_analysis.md
│       └── gui_apps.md
```

### 2. **규칙 활성화 확인**
- Python 파일 생성 후 Cascade에 작업 요청
- 규칙이 적용되는지 확인
- 필요시 규칙 수정

### 3. **규칙 최적화**
- 너무 제한적이면 완화
- 너무 느슨하면 구체화
- 실제 사용 피드백 반영

---

## 💡 추가 팁

### **메모리 관리**
- 규칙 파일당 12,000자 제한
- 중요한 규칙부터 우선 작성
- 불필요한 설명 제거

### **유지보수**
- 정기적으로 규칙 검토
- 프로젝트 진행에 맞춰 업데이트
- 팀원과 규칙 공유

### **성능 최적화**
- 너무 많은 규칙 파일 생성 방지
- 관련 규칙은 하나 파일에 통합
- 활성화 조건 최적화

이제 어떤 Python 프로그램이든 효과적인 Windsurf Rules를 작성할 수 있습니다! 🎯
