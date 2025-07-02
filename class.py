# 클래스와 객체, 메서드
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}이(가) 소리를 냅니다.")

# 상속과 다형성
class Dog(Animal):
    def speak(self):
        print(f"{self.name}이(가) 멍멍 짖습니다.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}이(가) 야옹합니다.")

# 캡슐화와 속성 관리
class Person:
    def __init__(self, name):
        self.__name = name  # 비공개 속성

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

# 사용 예시
dog = Dog("초코")
cat = Cat("나비")
dog.speak()     # 초코이(가) 멍멍 짖습니다.
cat.speak()     # 나비이(가) 야옹합니다.

person = Person("민수")
print(person.get_name())  # 민수
person.set_name("수진")
print(person.get_name())  # 수진
