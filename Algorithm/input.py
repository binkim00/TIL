# 첫 줄: 숫자 개수 입력
N = int(input())
print(N)

# 두 번째 줄:
# "1 2 3 4 5 6" 처럼 공백으로 구분된 숫자를 입력받음
# input().split() → 공백 기준으로 문자열을 나눔
# map(int, ...) → 각각을 정수로 변환
# list() → 리스트로 묶기
arr = list(map(int, input().split()))

print(arr)

###################################################################

# 첫 줄: 숫자 개수 입력
N = int(input())
print(N)

# 두 번째 줄:
# "123456" 처럼 공백 없이 붙어 있는 숫자를 입력받음
# split()을 사용하지 않음
# input() 자체가 문자열이므로, 한 글자씩 순회됨
# map(int, input()) → 문자 하나씩 정수로 변환
# list() → 리스트로 묶기
arr = list(map(int, input()))

print(arr)

###################################################################

import sys  # 파이썬의 표준 입출력 제어를 위해 sys 모듈 불러오기

# 표준 입력(stdin)을 sample_input.txt 파일로 변경
# 이제 input()은 키보드가 아니라 sample_input.txt에서 값을 읽어온다
sys.stdin = open("sample_input.txt", "r")

# 표준 출력(stdout)을 sample_output.txt 파일로 변경
# 이제 print()는 터미널이 아니라 sample_output.txt 파일에 출력된다
sys.stdout = open("sample_output.txt", "w")

# 파일 열기 모드 설명
# open("파일명", "w")  → write 모드 (기존 내용 삭제 후 새로 작성)
# open("파일명", "a")  → append 모드 (기존 내용 유지, 뒤에 추가)
# open("파일명", "r")  → read 모드 (읽기 전용)

# 첫 줄 입력을 정수로 변환하여 저장
# sample_input.txt의 첫 줄을 읽어와 int로 변환
N = int(input())

# 다음 줄을 공백 기준으로 나눠 정수 리스트로 변환
# 예: "1 2 3 4 5" → [1, 2, 3, 4, 5]
arr = list(map(int, input().split()))

# N 값을 출력 (현재는 파일에 저장됨)
print(N)

# 정수 리스트 arr 출력 (현재는 파일에 저장됨)
print(arr)
