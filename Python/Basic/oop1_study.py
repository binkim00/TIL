# -*- coding: utf-8 -*-

"""
OOP 오늘 배운 내용 정리 (학습용 py 파일)
- 클래스/인스턴스(객체)
- __init__ (생성자)
- 인스턴스 메서드(self)
- 클래스 변수 / 클래스 전체에 공통인 값
- 클래스 변수 조작(클래스 메서드 느낌) vs @staticmethod
- __str__ 매직 메서드( print(객체) 시 문자열 표현 )
- dir / help 로 객체가 가진 기능 확인

※ 이 파일은 "공부 자료"라서, 실행하면 예시 출력이 쭉 나옴.
"""

# ============================================================
# 0) 실행 안내
# ------------------------------------------------------------
# 아래 코드를 그대로 실행해도 되고,
# 각 섹션을 조금씩 수정하면서 실험해보면 이해가 빨라짐.
# ============================================================


# ============================================================
# 1) 클래스와 객체(인스턴스) : "설계도"와 "실제 물건"
# ------------------------------------------------------------
# - class: 설계도
# - obj  : 설계도로 만든 실제 물건(객체/인스턴스)
# ============================================================

class StringRepeater:
    """
    문자열을 count번 반복 출력하는 기능을 가진 클래스
    """

    def repeat_string(self, count, text):
        # self: "이 메서드를 호출한 객체 자신"
        for _ in range(count):
            print(text)


print("===== [1] StringRepeater 예시 =====")
repeater1 = StringRepeater()            # 객체 생성(설계도로 물건 만들기)
repeater1.repeat_string(3, "Hello")     # 객체의 행동(메서드) 호출
print()


# ============================================================
# 2) __init__ (생성자) : "객체가 만들어질 때 자동으로 1번 실행"
# ------------------------------------------------------------
# - 객체가 계속 기억해야 하는 값(상태)을 여기서 저장하는 편이 깔끔함
# - self.변수명 으로 저장하면 "인스턴스 변수"가 됨
# ============================================================

class Shape:
    """
    width, height(가로/세로)를 가지는 도형
    """

    def __init__(self, width, height):
        # 객체 생성 시 전달받은 값을 객체 안에 저장(상태 저장)
        self.width = width
        self.height = height

    def calculate_area(self):
        # 객체가 가진 상태를 이용해서 행동(면적 계산)
        return self.width * self.height

    def calculate_perimeter(self):
        # 둘레 = 2*가로 + 2*세로
        return self.width * 2 + self.height * 2

    def print_info(self):
        # 여러 정보를 한 번에 출력하는 "행동"
        area = self.calculate_area()
        peri = self.calculate_perimeter()
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {area}")
        print(f"Perimeter: {peri}")

    def __str__(self):
        # ★ 중요: __str__은 print가 아니라 "문자열 return" 해야 함
        # print(객체) 하면 파이썬이 자동으로 __str__을 호출해서 그 결과 문자열을 출력함
        return f"Shape: width={self.width}, height={self.height}"


print("===== [2] Shape 예시 =====")
shape1 = Shape(5, 3)  # 객체 생성 + 상태 저장
print("area:", shape1.calculate_area())
print("perimeter:", shape1.calculate_perimeter())
shape1.print_info()
print("print(shape1) ->", shape1)  # __str__ 확인
print()


# ============================================================
# 3) 클래스 변수 (class variable) : "모든 객체가 공통으로 공유"
# ------------------------------------------------------------
# - class 안에서, 메서드 밖에 선언된 변수
# - Car.wheels 처럼 "클래스 이름"으로 접근하는게 정석
# - self.wheels 로도 읽히긴 하지만(찾는 순서 때문에), 의도 표현상 Car.wheels가 깔끔함
# ============================================================

class Car:
    # 모든 자동차가 공통으로 가지는 값(클래스 변수)
    wheels = 4

    def __init__(self, engine, driving_system, sound):
        # 각 자동차(객체)마다 다른 값(인스턴스 변수)
        self.engine = engine
        self.driving_system = driving_system
        self.sound = sound

    def drive(self):
        # 인스턴스 메서드: self가 필요
        print(self.sound)
        # 요구사항 예시: drive는 engine을 반환
        return self.engine

    def introduce(self):
        # 인스턴스 메서드: 엔진/구동방식 소개
        print(f"제 차의 엔진은 {self.engine} 방식이고, {self.driving_system} (으)로 동작합니다.")

    # 클래스 변수(wheels)를 바꾸는 동작: 클래스 이름으로 호출하는 게 자연스러움
    # (엄밀히는 @classmethod로 만드는 방법도 있지만, 오늘 배운 흐름 기준으로 "클래스 호출"만 지키면 됨)
    def increase_wheels():
        Car.wheels += 1
        print("법이 개정되어 모든 자동차의 필요 바퀴 수가 1 증가하였습니다.")

    @staticmethod
    def description():
        # staticmethod: self/cls가 없음
        # -> 특정 자동차 1대가 아니라 "자동차라는 개념 설명" 같은 것에 어울림
        print("자동차(car)는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통수단이다.")


print("===== [3] Car 예시 =====")
car1 = Car("gasoline", "후륜구동", "부릉부릉")
car2 = Car("diesel", "전륜구동", "달달달달")
car3 = Car("hybrid", "4wd", "슈웅")

car1.drive()
print("car2.drive() 반환:", car2.drive())
print("---")
car1.introduce()
car3.introduce()
print("---")
print(f"이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.")
Car.increase_wheels()
print(f"이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.")
print("---")
Car.description()  # ★ 스태틱 메서드 출력(호출)
print()


# ============================================================
# 4) 클래스 변수 카운트 패턴 (객체 생성 횟수 세기)
# ------------------------------------------------------------
# - "객체가 몇 개 만들어졌는지" 같은 건 클래스 변수가 잘 어울림
# - 보통은 __init__ 안에서 증가시키는 패턴을 많이 씀
# ============================================================

class Myth:
    type_of_myth = 0

    def __init__(self, name):
        self.name = name
        # 객체가 생성될 때마다 클래스 변수 증가
        Myth.type_of_myth += 1

    @staticmethod
    def story():
        return "신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 신을 둘러싼 이야기이다."


print("===== [4] Myth 예시 =====")
p1 = Myth("dangun")
p2 = Myth("greek & rome")
print("p1.name:", p1.name)
print("p2.name:", p2.name)
print(f"현재까지 생성된 신화 수: {Myth.type_of_myth}")
print("Myth.story():", Myth.story())
print()


# ============================================================
# 5) dir / help : 객체가 가진 기능(메서드/속성) 확인하기
# ------------------------------------------------------------
# - dir(obj)  : obj가 가진 이름 목록(메서드/속성 이름들)
# - help(obj) : 사용법/설명(출력이 길 수 있음)
# ============================================================

print("===== [5] dir / help 예시 (짧게) =====")
my_list = [1, 2, 3]
my_dict = {"A": 1, "B": 2, "C": 3}

print("dir(list) 일부:", dir(my_list)[:10])  # 너무 길어서 일부만
print("dir(dict) 일부:", dir(my_dict)[:10])
print()


# ============================================================
# 6) 오늘 핵심 실수 포인트 체크리스트
# ------------------------------------------------------------
# 1) 인스턴스 메서드 첫 인자는 self가 반드시 있어야 함
#    - def drive(self):  (O)
#    - def drive():      (X)
#
# 2) __str__은 print가 아니라 return 문자열
#    - def __str__(self): return "..."  (O)
#    - def __str__(self): print("...")  (X)
#
# 3) 객체 생성 시 인자를 받으려면 __init__이 그 인자를 받아야 함
#    - Shape(5,3) -> __init__(self, 5, 3) 형태로 전달됨
#
# 4) 클래스 변수는 Car.wheels 처럼 클래스 이름으로 접근하는 습관
#
# 5) staticmethod는 "객체 상태와 무관한 기능"에 붙이기
#    - Car.description() 처럼 호출하는 게 의도 표현상 깔끔함
# ============================================================


# ============================================================
# 7) (연습) 직접 해볼 미니 과제
# ------------------------------------------------------------
# 아래 TODO를 직접 채워보세요.
# - 정답은 제공하지 않음(연습용)
# ============================================================

# TODO 1) Rectangle 클래스를 만들고
# - __init__(width, height)
# - area() : 면적 반환
# - perimeter() : 둘레 반환
# - __str__ : "Rectangle: width=..., height=..." 반환
#
# TODO 2) Counter 클래스를 만들고
# - 클래스 변수 count = 0
# - __init__ 호출될 때마다 count 증가
# - @staticmethod로 info() 만들어서 "현재 count는 ..." 출력
#
# TODO 3) StringRepeater에 repeat_list(count, words) 메서드를 추가하고
# - words 리스트의 각 문자열을 count번씩 출력해보기
#
# (원하면 내일 이 TODO를 가지고 테스트 질문 방식으로 같이 풀어도 됨)
