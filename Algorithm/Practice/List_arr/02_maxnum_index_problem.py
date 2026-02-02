####################################################
# [문제]
# N개의 정수가 주어진다.
# 가장 큰 값과 그 값의 인덱스를 출력하시오.
# (인덱스는 0부터 시작)
# 같은 최대값이 여러 개일 경우, 앞쪽 인덱스를 출력한다.
#
# [입력 예시]
# 1
# 6
# 4 9 2 9 1 5
#
# [출력 예시]
# #1 9 1
####################################################

T = int(input())
for test_case in range(1, T + 1):
    # 여기부터 알고리즘 구현
    N = int(input())
    
    arr = list(map(int, input().split()))
    
    max_num = arr[0]
    max_index = 0 # index 값은 0으로 하기

# ❌ for i in arr[0]:
# arr[0]은 숫자 하나임 → 숫자는 여러 개를 담고 있지 않아서 반복 불가
# ✅ for i in range(1, N):
# 인덱스 1부터 끝까지 하나씩 보면서 arr[i]를 확인하려는 반복문
    for i in range(1, N):
        if max_num < arr[i]:
            max_num = arr[i]
            max_index = i # i번 째 있는 값이니까 i 값을 인덱스로 주면 됨
    print(f"#{test_case} {max_num} {max_index}")