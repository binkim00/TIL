# 07_functions.py
# 함수: 정의/반환/기본값/가변인자/스코프

# ✅ 기본 함수
def add(a, b):
    return a + b

print(add(3, 5))

# ✅ 반환값 여러 개(튜플)
def min_max(arr):
    return min(arr), max(arr)

mn, mx = min_max([3, 1, 9])
print(mn, mx)

# ✅ 기본값(디폴트 파라미터)
def greet(name="손님"):
    print(f"안녕하세요, {name}님!")

greet()
greet("영빈")

# ✅ 가변 인자 *args
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))

# ✅ 키워드 인자 **kwargs
def show_profile(**info):
    for k, v in info.items():
        print(k, "=", v)

show_profile(name="영빈", role="student")

# ✅ 스코프: 지역/전역
x = 10

def foo():
    x = 5  # 지역 변수
    print("inside:", x)

foo()
print("outside:", x)
