# 06_collections.py
# 리스트 / 튜플 / 딕셔너리 / 집합 기본

# ✅ 리스트(list)
arr = [1, 2, 3]
arr.append(4)       # 뒤에 추가
arr.insert(1, 99)   # 특정 위치에 삽입
arr.pop()           # 마지막 제거
arr.remove(99)      # 값으로 제거(첫 번째만)
arr.sort()          # 정렬
print(arr)

# ✅ 리스트 슬라이싱
print(arr[:2])

# ✅ 튜플(tuple): 불변
t = (1, 2, 3)
print(t[0])

# ✅ 딕셔너리(dict): key-value
d = {"a": 1, "b": 2}
d["c"] = 3
print(d["a"])
print(d.get("x", 0))  # 없으면 기본값 0

# ✅ 딕셔너리 반복
for k in d:
    print("key:", k, "value:", d[k])

for k, v in d.items():
    print(k, v)

# ✅ 집합(set): 중복 제거, 순서 없음
s = {1, 2, 2, 3}
print(s)  # {1,2,3}
s.add(4)
s.discard(2)  # 없어도 에러 X
print(s)

# ✅ set 연산
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합
