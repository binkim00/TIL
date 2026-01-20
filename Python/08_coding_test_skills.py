# 08_coding_test_skills.py
# 코딩테스트에서 자주 쓰는 기능 모음(기본 내장 중심)

# ✅ 정렬
arr = [5, 2, 9, 1]
arr.sort()               # 오름차순
print(arr)

arr.sort(reverse=True)   # 내림차순
print(arr)

# ✅ sorted(): 원본 유지
arr2 = [3, 7, 4]
print(sorted(arr2))
print(arr2)

# ✅ key 정렬
words = ["apple", "kiwi", "banana"]
print(sorted(words, key=len))  # 길이순

# ✅ max/min/sum
nums = [10, 20, 30]
print(max(nums), min(nums), sum(nums))

# ✅ enumerate
for i, v in enumerate(nums):
    print(i, v)

# ✅ zip
a = [1, 2, 3]
b = ["a", "b", "c"]
for x, y in zip(a, b):
    print(x, y)

# ✅ 문자열/리스트 뒤집기
s = "abcd"
print(s[::-1])

# ✅ 리스트 컴프리헨션
sq = [x * x for x in range(5)]
print(sq)

# ✅ 조건 포함 컴프리헨션
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# ✅ 딕셔너리 컴프리헨션
d = {x: x * x for x in range(5)}
print(d)
