####################################################
# [유형 1] 2차원 배열 (난이도 혼합)
#
# N x N 배열이 주어진다.
# 각 행의 합, 각 열의 합, 두 대각선의 합 중
# 최댓값을 출력하시오.
####################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    # TODO: 행 합
    # TODO: 열 합
    # TODO: 대각선 합

    print(f"#{tc} {max_sum}")
