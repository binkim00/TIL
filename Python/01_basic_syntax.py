# 01_basic_syntax.py
# 파이썬 기본 문법: 변수/자료형/출력/주석/입력/형변환

# ✅ 주석
# 한 줄 주석은 # 로 작성합니다.

"""
여러 줄 주석(또는 멀티라인 문자열)은 이렇게 작성할 수 있습니다.
(주석처럼 쓰지만 사실 문자열입니다.)
"""

# ✅ 변수(파이썬은 타입 선언 없이 대입)
a = 10        # int
b = 3.14      # float
c = "hello"   # str
d = True      # bool

# ✅ 출력
print(a, b, c, d)
print("a =", a)

# ✅ f-string (문자열 포맷팅)
name = "영빈"
score = 85
print(f"{name}의 점수는 {score}")

# ✅ 입력: input()은 항상 문자열(str)로 들어옴
# s = input()  # 예: "123"
# print(type(s))  # <class 'str'>

# ✅ 형변환
# n = int(input())      # 정수로 변환
# x = float(input())    # 실수로 변환

# ✅ 여러 값 입력(공백 구분)
# A, B = map(int, input().split())
# print(A + B)

# ✅ 들여쓰기(Indent) 중요
# 파이썬은 중괄호 대신 들여쓰기로 블록을 구분합니다.
