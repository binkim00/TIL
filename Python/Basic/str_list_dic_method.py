############################################################
# 반환(return) · 참조 · 얕은 복사 · 깊은 복사 전체 정리
############################################################


############################
# 1. 반환 O (내부에 return 있음)
############################

# ----- 숫자 / 공통 -----
len(x)            # 길이/개수 반환
type(x)           # 타입 반환
int(x)            # 정수로 변환
float(x)          # 실수로 변환
str(x)            # 문자열로 변환
bool(x)           # True / False 반환

min(iterable)     # 최솟값 반환
max(iterable)     # 최댓값 반환
sum(iterable)     # 합계 반환
sorted(iterable)  # 정렬된 "새 리스트" 반환 (원본 유지)

abs(n)            # 절댓값 반환
round(n, k)       # 반올림 값 반환
divmod(a, b)      # (몫, 나머지) 튜플 반환


# ----- 문자열(str) : 전부 반환 O (새 문자열) -----
s.lower()         # 소문자 변환
s.upper()         # 대문자 변환
s.strip()         # 양쪽 공백 제거
s.replace(a, b)   # 문자열 치환
s.split(sep)      # 리스트로 분리
sep.join(lst)     # 리스트를 문자열로 결합

s.find(sub)       # 위치 반환 (없으면 -1)
s.count(sub)      # 개수 반환

s.isdigit()       # 숫자 문자열 여부
s.isalpha()       # 문자만 있는지
s.isalnum()       # 문자+숫자 여부


# ----- 리스트(list) : 반환 O -----
lst.count(x)      # 값 개수
lst.index(x)      # 값 위치
lst.copy()        # 얕은 복사 (새 리스트)
lst[:]            # 얕은 복사 (슬라이싱)

x in lst          # 포함 여부 True / False


# ----- 딕셔너리(dict) : 반환 O -----
d.get(k)           # 값 반환 (없으면 None)
d.get(k, default)  # 값 반환 (없으면 default)

d.keys()           # key 뷰 반환
d.values()         # value 뷰 반환
d.items()          # (key, value) 뷰 반환

k in d             # key 존재 여부


# ----- 집합(set) : 반환 O -----
st.union(other)         # 합집합 (새 set)
st.intersection(other)  # 교집합 (새 set)
st.difference(other)    # 차집합 (새 set)


############################
# 2. 반환 X (return 없음 / None)
############################

# ----- 출력 -----
print(x)           # 화면 출력만 함 (반환 None)


# ----- 리스트(list) : 원본 수정 -----
lst.append(x)      # 값 1개 추가
lst.extend(iter)   # 여러 값 추가
lst.insert(i, x)   # 특정 위치 삽입

lst.remove(x)      # 값 제거
lst.clear()        # 전체 비우기

lst.sort()         # 원본 정렬
lst.reverse()      # 원본 뒤집기


# ----- 딕셔너리(dict) : 원본 수정 -----
d.update(other)    # 여러 key/value 갱신
d.clear()          # 전체 비우기
del d[k]           # key 삭제


# ----- 집합(set) : 원본 수정 -----
st.add(x)                 # 값 추가
st.update(iterable)       # 여러 값 추가
st.remove(x)              # 값 제거 (없으면 에러)
st.discard(x)             # 값 제거 (없어도 OK)
st.clear()                # 전체 비우기


############################
# 3. 반환 + 원본 수정 (특별 케이스)
############################

x = lst.pop()       # 마지막 요소 반환 + 원본 수정
x = lst.pop(i)      # i 요소 반환 + 원본 수정

v = d.pop(k)        # value 반환 + key 삭제
kv = d.popitem()    # (key, value) 반환 + 삭제


############################
# 4. 참조 (복사 아님)
############################

a = [1, 2, 3]
b = a               # 같은 객체 참조 (복사 X)

b.append(4)
# a와 b 둘 다 [1, 2, 3, 4]


############################
# 5. 얕은 복사 (shallow copy)
############################

a = [1, 2, 3]
b = a.copy()        # 겉만 새 객체
c = a[:]            # 슬라이싱 얕은 복사

# 중첩 구조에서는 내부 객체 공유
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
# a도 같이 바뀜


############################
# 6. 깊은 복사 (deep copy)
############################

import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # 내부까지 완전히 새 객체

b[0].append(99)
# a는 안 바뀜


############################
# 7. 함수 설계 관점 정리
############################

def bad_func(lst):
    lst.append(1)       # 반환 X, 원본 직접 수정 (부작용)

def good_func(lst):
    new_lst = lst.copy()  # 얕은 복사
    new_lst.append(1)
    return new_lst        # 새 객체 반환 (안전)


############################################################
# 핵심 요약
#
# - 반환 O  → 값이 나온다 (return 있음)
# - 반환 X  → 원본만 바꾼다 (None)
# -_toggle
# - =        → 참조
# - copy()   → 얕은 복사
# - deepcopy → 깊은 복사
############################################################
