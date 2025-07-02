# 4. 입력과 출력

# input()으로 사용자 입력, print()로 출력 (f-string 사용)
print("\n=== 입력과 출력 ===")
name = input("이름을 입력하세요: ")  # 사용자 입력 받기
age = int(input("나이를 입력하세요: "))  # 입력을 정수로 변환
print(f"{name}님, {age}세입니다.")  # 출력 예: Alice님, 25세입니다.
print("Hello", name, sep=", ", end="!")  # 출력 예: Hello, Alice!
