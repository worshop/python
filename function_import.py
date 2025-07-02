#예제 1: 함수 정의와 호출


def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)

#예제 2: 여러 값을 반환하는 함수

def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [4, 7, 1, 9, 2]
minimum, maximum = get_min_max(nums)
print("최솟값:", minimum)
print("최댓값:", maximum)


# 예제 3: 표준 모듈(import) 사용
import math

print("PI 값:", math.pi)
print("16의 제곱근:", math.sqrt(16))
