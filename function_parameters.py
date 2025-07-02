

# 1. 기본값 매개변수(Default Parameter)

 
def greet(name, message="안녕하세요!"):
    print(f"{name}님, {message}")

greet("지민")                # 기본값 사용
greet("수진", "좋은 하루!")  # 기본값 대신 다른 값 전달


# 2. 가변 인자(Variable Arguments)

 
def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_all(1, 2, 3))        # 6
print(add_all(5, 10, 15, 20))  # 50


# 가변 키워드 인자(**kwargs): 여러 개의 키워드 인자를 딕셔너리로 받음

 
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="지민", age=23, city="부산")
