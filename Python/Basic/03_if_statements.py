# 03_if_statements.py
# 조건문 if / elif / else

# ✅ 기본 if
x = 10
if x > 0:
    print("양수")
else:
    print("0 또는 음수")

# ✅ elif
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("등급:", grade)

# ✅ 논리 연산자: and / or / not
a, b = 5, 12
if a > 0 and b > 0:
    print("둘 다 양수")

# ✅ 비교 연산자: == != < <= > >=
if a == 5:
    print("a는 5")

# ✅ in 연산자 (포함 여부)
fruits = ["apple", "banana", "kiwi"]
if "banana" in fruits:
    print("바나나 있음")
