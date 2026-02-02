####################################################
# [문제]
# N개의 정수가 주어진다.
# 최댓값과 최솟값의 차이를 출력하시오.
#
# [입력 예시]
# 1
# 5
# 10 3 7 1 9
#
# [출력 예시]
# #1 9
####################################################

T = int(input())
for test_case in range(1, T + 1):
    # 여기부터 알고리즘 구현
    N = int(input())

    # 공백 없으면 split 없이 사용
    arr = list(map(int, input().split()))

    max_num = arr[0]
    min_num = arr[0]

    for i in range(1, N): # 이 부분 항상 잊지 않기~
        if min_num > arr[i]:
            min_num = arr[i]
    
    for i in range(1, N):
        if max_num < arr[i]:
            max_num = arr[i]

    print(f"#{test_case} {max_num - min_num}")
