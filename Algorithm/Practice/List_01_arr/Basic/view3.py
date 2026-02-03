####################################################
# [문제]
# N개의 건물이 일렬로 서 있다.
# 각 건물의 높이가 주어진다.
#
# i번째 건물(단, i는 2 ~ N-3만 검사 가능)에 대해
# 좌우 2칸(총 4칸) 중 가장 높은 건물 높이를 neighbor_max라고 하자.
#
# 만약 h[i]가 neighbor_max보다 크다면 조망 점수는 (h[i] - neighbor_max)이다.
# 이때 조망 점수는 최대 5를 넘지 못한다. (5를 초과하면 5로 처리)
#
# 모든 i에 대한 조망 점수의 합을 출력하시오.
#
# [입력 예시]
# 1
# 9
# 0 0 5 7 9 4 3 0 0
#
# [출력 예시]
# #1 2
####################################################

T = int(input())
for test_case in range(1, T + 1):
    # 여기부터 알고리즘 구현
    N = int(input())
    h = list(map(int, input().split()))
    
    total_point = 0

    for i in range(2, N - 2):

        neighbor_max = max(
            h[i - 2],
            h[i - 1],
            h[i + 1],
            h[i + 2]
        )

        view_point = 0

        if h[i] > neighbor_max:
            view_point = h[i] - neighbor_max
            if view_point > 5:
                view_point = 5

        total_point += view_point

    
    print(f"#{test_case} {total_point}")
