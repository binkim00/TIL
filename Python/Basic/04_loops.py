# 04_loops.py
# 반복문 for / while

# ✅ for + range
for i in range(5):  # 0~4
    print("i =", i)

# ✅ range(start, end, step)
for i in range(1, 10, 2):  # 1,3,5,7,9
    print("odd:", i)

# ✅ 리스트 반복
arr = [10, 20, 30]
for x in arr:
    print("x =", x)

# ✅ enumerate(인덱스 + 값)
for idx, val in enumerate(arr):
    print(idx, val)

# ✅ while
n = 3
while n > 0:
    print("n =", n)
    n -= 1

# ✅ break / continue
for i in range(10):
    if i == 3:
        continue  # 3은 건너뜀
    if i == 7:
        break     # 7에서 중단
    print(i)
