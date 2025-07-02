# 예제 1: 문자열 메서드 활용

text = "Hello, Python!"

# 소문자로 변환
print(text.lower())           # hello, python!

# 대문자로 변환
print(text.upper())           # HELLO, PYTHON!

# 특정 문자 개수 세기
print(text.count("o"))        # 2

# 문자열 교체
print(text.replace("Python", "World"))  # Hello, World!


#예제 2: 문자열 분리와 결합

sentence = "사과,바나나,오렌지"
fruits = sentence.split(",")         # 리스트로 분리
print(fruits)                        # ['사과', '바나나', '오렌지']

joined = " & ".join(fruits)          # 리스트를 문자열로 결합
print(joined)                        # 사과 & 바나나 & 오렌지


#예제 3: 문자열 포매팅

name = "민수"
age = 20

# f-string 방식 (Python 3.6+)
print(f"이름: {name}, 나이: {age}")

# format() 메서드 방식
print("이름: {}, 나이: {}".format(name, age))

# % 연산자 방식
print("이름: %s, 나이: %d" % (name, age))
