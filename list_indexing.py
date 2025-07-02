#리스트 생성과 인덱싱
fruits = ["사과", "바나나", "오렌지", "포도"]
print("첫 번째 과일:", fruits[0])     # 인덱스 0
print("마지막 과일:", fruits[-1])    # 음수 인덱스

#리스트 슬라이싱
numbers = [10, 20, 30, 40, 50, 60]
print("처음 세 개:", numbers[:3])       # [10, 20, 30]
print("네 번째부터 끝까지:", numbers[3:]) # [40, 50, 60]
print("중간 일부:", numbers[2:5])        # [30, 40, 50]

#리스트 기본 메서드
animals = ["강아지", "고양이", "토끼"]
animals.append("햄스터")         # 요소 추가
print("추가 후:", animals)

animals.remove("고양이")         # 요소 제거
print("제거 후:", animals)

animals.sort()                  # 정렬
print("정렬 후:", animals)
