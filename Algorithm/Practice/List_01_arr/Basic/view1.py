####################################################
# [문제]
# N개의 건물이 일렬로 서 있다.
# 각 건물의 높이가 주어진다.
#
# i번째 건물(단, i는 2 ~ N-3만 검사 가능)에 대해
# 좌우 2칸(총 4칸) 중 가장 높은 건물 높이를 neighbor_max라고 하자.
#
# 만약 h[i]가 neighbor_max보다 크다면
# 조망 점수는 (h[i] - neighbor_max)이다.
#
# 모든 i에 대한 조망 점수의 합을 출력하시오.
#
# [입력 예시]
# 1
# 9
# 0 0 3 5 7 4 2 0 0
#
# [출력 예시]
# #1 2
####################################################

T = int(input())
for test_case in range(1, T + 1):
    # 여기부터 알고리즘 구현
    
    N = int(input())

    h = list(map(int, input().split()))

    total_view = 0
    # [놓친 핵심]
    # neighbor_max = 0
    # 이 문제는 "가장 큰 차이 하나"를 고르는 문제가 아님
    # → "모든 건물 i에 대해 계산한 조망 점수의 합"을 구하는 문제
    # 그래서 누적 변수(total_view)가 반드시 필요함

    for i in range(2, N - 2):

        neighbor_max = max(
            h[i - 2],
            h[i - 1],
            h[i + 1],
            h[i + 2]
        )

        # "가장 높은 건물 전체"를 찾는 게 아님
        # → 오직 i 기준 좌우 2칸, 총 4칸 중에서만 최댓값을 구함
        # view_point = 0

        if h[i] > neighbor_max:
            # [가장 큰 오해 포인트]
            # 여기서 구한 (h[i] - neighbor_max)는
            # "이 i 하나의 조망 점수"일 뿐임
            # → 이 값이 '답'이 아니라
            # → 이 값을 total_view에 더해야 함
            # view_point = h[i] - neighbor_max
            total_view += (h[i] - neighbor_max)

        # 
        # 조망 점수가 없는 i들도 존재함
        # (h[i] <= neighbor_max 인 경우)
        # → 그런 i는 그냥 0점으로 넘어가는 구조

    print(f"#{test_case} {total_view}")
    # [헷갈린 부분 3]
    # 출력해야 하는 값은
    # "가장 큰 차이"가 아니라
    # "모든 i의 조망 점수를 더한 결과"