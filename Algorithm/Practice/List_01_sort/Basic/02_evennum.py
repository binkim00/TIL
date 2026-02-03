####################################################
# [문제 2]
# N개의 정수가 주어진다.
# 이 중 짝수만 골라 그 합을 출력하시오.
#
# [개념] 완전 검색 + 조건 분기
#
# [입력]
# 첫 줄에 테스트 케이스 개수 T
# 각 테스트 케이스마다
#   - 첫 줄: 정수 N
#   - 둘째 줄: N개의 정수
#
# [입력 예시]
# 1
# 6
# 1 2 3 4 5 6
#
# [출력 예시]
# #1 12
####################################################

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    num_sum = 0

    for i in range(N):
        if arr[i] % 2 == 0:
            num_sum += arr[i]

    # 이거랑 같음
    # for num in arr:
    #     if num % 2 == 0:
    #         num_sum += num

    print(f"#{test_case} {num_sum}")