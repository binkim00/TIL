####################################################
# [문제 4]
# 길이가 N인 상자 높이 배열이 주어진다.
# 가장 높은 곳에서 1을 빼서 가장 낮은 곳에 1을 
# 더하는 작업을 덤프라고 하고 K번 수행한다.
# K번 수행 후, 최고점과 최저점의 차이를 출력하시오.
#
# [개념] 탐욕 알고리즘 + 시뮬레이션
#
# [입력]
# 첫 줄 테스트 케이스 개수 T
# 각 테스트 케이스마다
#   - 첫 줄: 정수 N K
#   - 둘째 줄: N개의 상자 높이
#
# [입력 예시]
# 1
# 5 2
# 7 4 2 9 1
#
# [출력 예시]
# #1 5
####################################################
T = int(input())
for test_case in range(1, T + 1):

    N, K = map(int, input().split())
    boxs = list(map(int, input().split()))

    # 덤프를 K번 반복
    for _ in range(K):

        # 이번 덤프에서 사용할
        # 가장 높은 위치 / 가장 낮은 위치 찾기
        max_idx = 0
        min_idx = 0

        for i in range(1, N):
            # 가장 높은 곳 찾기
            if boxs[i] > boxs[max_idx]:
                max_idx = i

            # 가장 낮은 곳 찾기
            if boxs[i] < boxs[min_idx]:
                min_idx = i

        # 평탄화가 의미 없으면 중단
        # (이미 최고 - 최저 차이가 1 이하)
        if boxs[max_idx] - boxs[min_idx] <= 1:
            break

        # 덤프 1회 수행
        # 가장 높은 곳에서 1 빼고
        # 가장 낮은 곳에 1 더하기
        boxs[max_idx] -= 1
        boxs[min_idx] += 1

    # 최종 최고점과 최저점 구하기
    max_box = boxs[0]
    min_box = boxs[0]

    for i in range(1, N):
        if boxs[i] > max_box:
            max_box = boxs[i]
        if boxs[i] < min_box:
            min_box = boxs[i]

    print(f"#{test_case} {max_box - min_box}")