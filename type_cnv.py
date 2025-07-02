# 3. 타입 확인 및 변환

# type()으로 타입 확인, int(), str(), float()으로 변환
x = 42
y = "100"
z = 3.14
print("\n=== 타입 확인 및 변환 ===")
print(f"x의 타입: {type(x)}")         # 출력: <class 'int'>
print(f"y의 타입: {type(y)}")         # 출력: <class 'str'>
print(f"문자열 y를 정수로: {int(y)}") # 출력: 100
print(f"정수 x를 문자열로: {str(x)}") # 출력: 42
print(f"정수 x를 부동소수점으로: {float(x)}")  # 출력: 42.0
