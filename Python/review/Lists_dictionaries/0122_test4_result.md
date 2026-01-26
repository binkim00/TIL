## 1) “같은 객체” vs “새 객체”를 헷갈리셨습니다

### 핵심 문장

- `lst.append(4)` / `info["age"] = 21` 처럼 **객체를 ‘수정’**하면 → **원본이 바뀝니다.**
- `lst = [...]` / `info = {...}` 처럼 **변수에 ‘재할당’**하면 → **원본은 안 바뀝니다.** (함수 안에서만 바뀜)

이걸 “객체 vs 변수”로 분리해서 보면 됩니다.

### 비유로 정리

- **객체(리스트/딕셔너리)** = 실제 물건(노트, 종이)
- **변수(lst, info)** = 그 물건을 가리키는 “포스트잇 이름표”

✅ `append`, `info["age"]=...` 는 **물건에 직접 낙서/수정**

✅ `lst = [...]` 는 **이름표를 다른 물건에 붙이는 것**

---

## 2) 함수의 return을 “수정 결과”로 착각하셨습니다

특히 이 부분이 반복해서 나오셨습니다:

### (A) 리스트를 수정하면, 함수 결과도 리스트일 것 같아 보임

하지만 **return이 없으면 결과는 무조건 `None`**입니다.

```python
numbers = [1,2,3]

def add_four(lst):
    lst.append(4)# ✅ 수정은 함
# ❌ return 없음

result = add_four(numbers)
print(numbers)# [1, 2, 3, 4]
print(result)# None

```

- `numbers`는 바뀝니다 (수정했으니까)
- `result`는 `None`입니다 (return 안 했으니까)

✅ 여기서 제일 중요한 건:

**“수정했다”와 “반환했다”는 서로 다른 개념**이라는 점입니다.

---

## 3) “새 리스트를 반환”하면 원본은 그대로입니다

```python
numbers = [1,2,3]

def add_four(lst):
    new_list = lst + [4]# ✅ 새 리스트 생성
return new_list

result = add_four(numbers)
print(numbers)# [1, 2, 3]     (원본 그대로)
print(result)# [1, 2, 3, 4]  (새 리스트)

```

여기서 포인트는:

- `lst + [4]`는 **새 객체**를 만듭니다.
- 원본 `numbers`를 “수정”한 게 아닙니다.

---

## 4) 딕셔너리도 똑같습니다: “수정”이면 원본 변경

```python
user = {"name":"kim","age":20}

def increase_age(info):
    info["age"] +=1# ✅ 원본 딕셔너리 수정
return info# ✅ 같은 객체를 반환

result = increase_age(user)
print(user)# {'name': 'kim', 'age': 21}
print(result)# {'name': 'kim', 'age': 21}

```

여기서 영빈님이 “result는 새 딕셔너리”라고 생각하신 부분이 핵심 오해 포인트입니다.

이 코드는 **새 딕셔너리를 만든 적이 없습니다.**

- `info["age"] += 1` → 기존 `user`를 직접 수정
- `return info` → 수정된 그 **같은 객체**를 그대로 돌려줌

즉,

- `user`와 `result`는 **같은 객체**입니다.

---

## 5) “재할당”은 원본을 안 바꿉니다 (함수 밖에는 영향 없음)

```python
user = {"name":"kim","age":20}

def update_age(info):
    info = {"name":"kim","age":21}# ✅ 새 딕셔너리 생성 + 재할당

update_age(user)
print(user)# {'name': 'kim', 'age': 20}  (원본 그대로)

```

여기서 일어난 일:

- 함수 안에서 `info`가 가리키던 대상이 **새 딕셔너리로 바뀐 것뿐**
- `user`라는 변수는 아무 변화가 없음

---

## 6) “내가 지금 헷갈리는지” 바로 판별하는 체크리스트

코드를 볼 때 아래 두 질문만 하시면 됩니다.

### 체크 1: 함수 안에서 **대괄호/키 접근으로 값을 바꾸고 있는가?**

- `lst.append(...)`
- `lst[0] = ...`
- `info["age"] = ...`
- `info["age"] += 1`

✅ 있으면 → **원본 변경 가능성 높음(대부분 변경됨)**

### 체크 2: 함수 안에서 **변수에 = 로 통째로 새로 넣고 있는가?**

- `lst = [...]`
- `info = {...}`

✅ 있으면 → **원본은 안 바뀜(재할당)**

### 체크 3: 결과 변수에 담긴 값이 이상하다?

- `result = func(...)` 했는데 `None`이 나온다?

✅ 그럼 거의 100% → **return이 없었던 것**

---

## 7) 영빈님이 딱 같은 실수를 반복한 지점 요약

- `append`를 보면서
    
    “리스트가 바뀌었으니 result도 리스트겠지?”
    
    → ❌ return이 없으면 result는 `None`
    
- `return info`를 보면서
    
    “return 했으니 새 객체가 만들어졌겠지?”
    
    → ❌ return은 새 객체를 만드는 게 아니라 **그냥 돌려주는 것**
    
    새 객체가 되려면 코드에 “새로 만드는 부분”이 있어야 합니다.