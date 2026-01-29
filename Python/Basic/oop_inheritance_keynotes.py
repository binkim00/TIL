""" 
[수업자료 핵심 정리] 상속 / 오버라이딩 / 다중상속(MRO) / super()

- 이 파일은 '개념 + 바로 실행되는 예시' 형태로 정리한 공부용 자료입니다.
- 출력 결과를 보면서 흐름을 확인할 수 있도록 print를 충분히 넣었습니다.

목차
1) 상속이 필요한 이유 & 기본 상속
2) 상속으로 계층 구조 만들기 (Person-Student/Professor)
3) 메서드 오버라이딩 vs (파이썬에서) 오버로딩
4) 다중 상속 & MRO(Method Resolution Order)
5) super() 단일 상속
6) super() 다중 상속: "직계 부모"가 아니라 "MRO 다음"을 가리킨다
"""

# ============================================================
# 1) 상속(Inheritance) 기본
# ============================================================
# 상속: 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것
# 왜 쓰나?
# - 코드 재사용: 중복 제거
# - 계층 구조: 관계 표현 (Animal -> Dog/Cat)
# - 유지보수: 부모만 고치면 자식도 개선되는 효과

class Animal:
    def eat(self):
        print("Animal: 먹는 중")


class Dog(Animal):  # Dog는 Animal을 상속받음
    def bark(self):
        print("Dog: 멍멍")


def demo_1_inheritance_basic():
    print("\n[1] 상속 기본")
    my_dog = Dog()
    my_dog.bark()   # 자식 메서드
    my_dog.eat()    # 부모 메서드도 그대로 사용 가능


# ============================================================
# 2) 상속으로 계층 구조 만들기 (중복 제거)
# ============================================================
# Person을 공통 부모로 두고 Professor/Student가 확장한다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"반갑습니다. {self.name}입니다.")


class Professor(Person):
    def __init__(self, name, age, department):
        # 핵심 포인트:
        # Person의 초기화 로직(name, age)을 재사용하면 중복이 줄어듦.
        # (여기서는 super() 버전은 아래 5)에서 본격적으로 다룹니다.)
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


def demo_2_hierarchy():
    print("\n[2] 계층 구조 (Person -> Professor/Student)")
    p1 = Professor("박교수", 49, "컴퓨터공학과")
    s1 = Student("김학생", 20, 3.5)
    p1.talk()
    s1.talk()
    print("교수 department:", p1.department)
    print("학생 gpa:", s1.gpa)


# ============================================================
# 3) 메서드 오버라이딩 vs 오버로딩(파이썬 미지원)
# ============================================================
# 오버라이딩: 부모의 메서드를 자식에서 재정의(같은 이름/같은 파라미터)
# 오버로딩: 같은 이름, 다른 파라미터로 여러 메서드를 정의 (파이썬은 지원 X)

class Animal2:
    def eat(self):
        print("Animal2: 먹는 중")


class Dog2(Animal2):
    def eat(self):  # 오버라이딩
        print("Dog2: 먹는 중")


class ExampleOverload:
    def do_something(self, x):
        print("첫 번째 do_something:", x)

    # 파이썬은 이름이 같으면 뒤의 정의가 앞을 덮어씀(오버로딩처럼 동작 X)
    def do_something(self, x, y):
        print("두 번째 do_something:", x, y)


def demo_3_overriding_overloading():
    print("\n[3] 오버라이딩 / (파이썬에서) 오버로딩 불가")
    d = Dog2()
    d.eat()  # Dog2가 먹는 중

    ex = ExampleOverload()
    print("ExampleOverload.do_something은 '두 번째 정의'만 남아있음")
    try:
        ex.do_something(10)  # y가 없어서 TypeError
    except TypeError as e:
        print("TypeError 발생:", e)


# ============================================================
# 4) 다중 상속 & MRO
# ============================================================
# 다중 상속: 둘 이상의 부모 클래스로부터 상속
# 충돌(중복 메서드/속성)이 있으면 "상속 순서"와 MRO 규칙으로 결정됨.
#
# MRO 원칙(요약)
# 1) 자식 우선
# 2) 왼쪽 부모 우선(먼저 적힌 부모)
# 3) 중복 방문 방지(공통 조상은 한 번만)

class Person2:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"안녕, {self.name}"


class Mom(Person2):
    gene = "XX"
    def swim(self):
        return "엄마가 수영"


class Dad(Person2):
    gene = "XY"
    def walk(self):
        return "아빠가 걷기"


class FirstChild(Dad, Mom):
    def swim(self):
        return "첫째가 수영"

    def cry(self):
        return "첫째가 응애"


def demo_4_multiple_inheritance_mro():
    print("\n[4] 다중 상속 & MRO")
    baby1 = FirstChild("아가")
    print(baby1.cry())
    print(baby1.swim())      # FirstChild가 오버라이딩
    print(baby1.walk())      # Dad에서 상속
    print("gene:", baby1.gene)  # Dad.gene (왼쪽 부모 우선)
    print(baby1.greeting())  # Person2.greeting
    print("MRO:", [cls.__name__ for cls in FirstChild.mro()])


# ============================================================
# 5) super() 단일 상속
# ============================================================
# super(): "부모 클래스"에 접근하는 느낌으로 쓰지만,
# 정확히는 "현재 클래스의 MRO 다음 클래스"를 찾아서 호출해주는 내장함수.
#
# 단일 상속에서는 사실상 '부모 호출'과 거의 동일하게 느껴짐.
# 장점: 중복 제거, 부모 수정 시 자식 수정 최소화

class Person3:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student3(Person3):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)  # 부모 초기화 재사용
        self.student_id = student_id


def demo_5_super_single():
    print("\n[5] super() 단일 상속")
    s = Student3("영빈", 20, "010-0000-0000", "test@test.com", "S001")
    print(s.name, s.age, s.number, s.email, s.student_id)


# ============================================================
# 6) super() 다중 상속: MRO 기반 '다음'을 호출
# ============================================================
# 아래 예시는 'super()가 직계부모만 부른다'는 오해를 깨기 위한 것.
# Child(ParentA, ParentB) 인데 Child에서 super().__init__()은 ParentA로 감.
# 그런데 ParentA 내부에서도 super().__init__()을 호출하면,
# MRO에서 ParentA 다음인 ParentB.__init__()이 호출될 수 있다.
#
# 즉, 다중 상속에서 "모든 부모 초기화"를 원하면
# 각 부모의 __init__에서 super().__init__()를 협조적으로 호출해줘야 한다.

class ParentA:
    def __init__(self):
        # 여기 super().__init__()이 없으면 ParentB 초기화로 못 내려감
        self.value_a = "ParentA"

    def show_value(self):
        print(f"Value from ParentA: {self.value_a}")


class ParentB:
    def __init__(self):
        self.value_b = "ParentB"

    def show_value(self):
        print(f"Value from ParentB: {self.value_b}")


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # MRO상 ParentA.__init__ 호출
        self.value_c = "Child"

    def show_value(self):
        super().show_value()  # MRO상 ParentA.show_value 호출
        print(f"Value from Child: {self.value_c}")


def demo_6_super_multiple_without_coop():
    print("\n[6-1] super() 다중 상속 (부모들이 협조적이지 않을 때)")
    c = Child()
    c.show_value()
    print("value_c:", c.value_c)
    print("value_a:", c.value_a)
    # ParentB.__init__이 실행되지 않았으니 value_b가 없음
    try:
        print("value_b:", c.value_b)
    except AttributeError as e:
        print("AttributeError 발생:", e)
    print("MRO:", [cls.__name__ for cls in Child.mro()])


# 협조적(cooperative) 다중 상속 버전
class ParentA2:
    def __init__(self):
        super().__init__()  # ← 핵심: 다음(MRO)으로 넘김
        self.value_a = "ParentA2"

    def show_value(self):
        print(f"Value from ParentA2: {self.value_a}")


class ParentB2:
    def __init__(self):
        super().__init__()
        self.value_b = "ParentB2"

    def show_value(self):
        print(f"Value from ParentB2: {self.value_b}")


class Child2(ParentA2, ParentB2):
    def __init__(self):
        super().__init__()
        self.value_c = "Child2"

    def show_value(self):
        # ParentA2.show_value -> (그 메서드에서 super 호출 없으므로) 여기선 ParentA2만 실행됨
        super().show_value()
        print(f"Value from Child2: {self.value_c}")


def demo_6_super_multiple_with_coop():
    print("\n[6-2] super() 다중 상속 (부모들이 협조적일 때)")
    c = Child2()
    c.show_value()
    print("value_c:", c.value_c)
    print("value_a:", c.value_a)
    print("value_b:", c.value_b)
    print("MRO:", [cls.__name__ for cls in Child2.mro()])


# ============================================================
# 실행 구간
# ============================================================
if __name__ == "__main__":
    demo_1_inheritance_basic()
    demo_2_hierarchy()
    demo_3_overriding_overloading()
    demo_4_multiple_inheritance_mro()
    demo_5_super_single()
    demo_6_super_multiple_without_coop()
    demo_6_super_multiple_with_coop()
