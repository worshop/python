# 학생 성적 관리 프로그램

<coding_guidelines>
- 환경: Python 3.10 사용
- 대상: Python 초보자(대학 2학년)
- 제약: 외부 라이브러리는 표준 라이브러리(tkinter 포함) 및 Matplotlib만 사용
- 모든 코드에 초보자가 이해할 수 있는 주석 추가 필수
</coding_guidelines>

<data_structure>
- 학생 정보는 딕셔너리 형태로 저장: {"이름": str, "과목": str, "점수": int}
- 점수 범위: 0-100, 범위 벗어나면 재입력 요청
- 등급 기준: A(90-100), B(80-89), C(70-79), D(60-69), F(<60)
</data_structure>

<gui_requirements>
- tkinter를 사용한 GUI 인터페이스 구현
- 필수 컴포넌트:
  - 학생 이름 입력 필드 (Entry)
  - 과목 입력 필드 (Entry)
  - 점수 입력 필드 (Entry with validation)
  - "학생 추가" 버튼
  - 학생 목록 표시 (Listbox 또는 Text widget)
  - "평균 계산" 버튼
  - "파일 저장" 버튼
  - "시각화" 버튼
  - "초기화" 버튼
- 에러 메시지는 messagebox.showerror 사용
- 성공 메시지는 messagebox.showinfo 사용
</gui_requirements>

<file_operations>
- 저장 형식: CSV 파일 (.csv) 우선, TXT 파일 (.txt) 옵션 제공
- 파일 구조: "이름,과목,점수,등급" 형태
- tkinter.filedialog.asksaveasfilename 사용
- 파일 불러오기 기능 포함 (Load 버튼)
- 저장/불러오기 성공/실패 메시지 표시
</file_operations>

<visualization_features>
- Matplotlib 막대그래프 생성
- 그래프 설정:
  - 제목: "학생 점수 분포"
  - X축: "학생", Y축: "점수"
  - 등급별 색상: A(green), B(blue), C(yellow), D(orange), F(red)
- plt.show()로 별도 창에 표시
- 그래프 저장 기능 포함 (PNG 형식)
</visualization_features>
