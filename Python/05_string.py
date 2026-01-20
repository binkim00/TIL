# 05_string.py
# 문자열: 인덱싱/슬라이싱/메서드/문자열 합치기

s = "python"

# ✅ 인덱싱
print(s[0])   # p
print(s[-1])  # n

# ✅ 슬라이싱: s[start:end:step]
print(s[1:4])   # yth
print(s[:3])    # pyt
print(s[::2])   # pto
print(s[::-1])  # nohtyp (뒤집기)

# ✅ 길이
print(len(s))

# ✅ 문자열 더하기/반복
print("py" + "thon")
print("ha" * 3)  # hahaha

# ✅ 자주 쓰는 메서드
t = "  Hello World  "
print(t.strip())          # 양쪽 공백 제거
print(t.lower())          # 소문자
print(t.upper())          # 대문자
print(t.replace("World", "Python"))
print("a,b,c".split(",")) # 분리
print("-".join(["a", "b", "c"]))  # 합치기

# ✅ 문자열은 불변(immutable)이라 직접 수정 불가
# s[0] = "P"  # TypeError
# 대신 새 문자열 생성
s2 = "P" + s[1:]
print(s2)
