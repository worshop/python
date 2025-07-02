for i in range(1, 21):
    if i % 2 != 0:
        continue            # 홀수는 건너뜀
    if i == 10:
        print("10은 건너뜁니다.")
        continue            # 10은 건너뜀
    if i > 15:
        print("15보다 커서 반복을 종료합니다.")
        break               # 15보다 크면 반복 종료
    print("현재 숫자:", i)

print("\nwhile문으로 동일한 동작 구현")

i = 1
while i <= 20:
    if i % 2 != 0:
        i += 1
        continue           # 홀수는 건너뜀
    if i == 10:
        print("10은 건너뜁니다.")
        i += 1
        continue           # 10은 건너뜀
    if i > 15:
        print("15보다 커서 반복을 종료합니다.")
        break              # 15보다 크면 반복 종료
    print("현재 숫자:", i)
    i += 1
