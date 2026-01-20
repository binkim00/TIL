# 09_common_errors.py
# 자주 터지는 에러/실수 모음 (원인 + 예시)

# ✅ 1) NameError: 변수 이름 오타(대소문자 포함)
# A, B = map(int, input().split())
# print(A-b)  # b가 없음 (B는 대문자)

# ✅ 2) TypeError: 타입이 맞지 않음
# s = input()        # 문자열
# print(s - 1)       # 문자열 - 숫자 불가
# print(int(s) - 1)  # 이렇게 변환해야 함

# ✅ 3) input() 괄호 빠뜨림
# B = input   # 함수 자체가 들어감(문자열 아님)
# print(B[0]) # 함수는 인덱싱 불가

# ✅ 4) IndexError: 범위 밖 인덱스
# arr = [1, 2, 3]
# print(arr[3])  # 0~2까지만 존재

# ✅ 5) ValueError: 변환 불가능한 문자열을 int로
# print(int("3.14"))   # "3.14"는 int 변환 불가 -> float로 먼저
# print(int(float("3.14")))

# ✅ 6) EOFError: 입력을 더 받으려 하는데 입력이 없음
# s = input()
# t = input()  # 문제 입력이 1줄인데 2번 input() 하면 EOFError

print("이 파일은 에러 예시 모음입니다. 주석을 하나씩 풀어서 실험해보세요.")
