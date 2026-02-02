####################################################
# [문제]
# N개의 정수가 주어진다.
# 연속된 M개의 숫자 합 중
# 최대 합과 최소 합의 차이를 출력하시오.
#
# [입력 예시]
# 1
# 8 3
# 1 2 3 4 5 6 7 8
#
# [출력 예시]
# #1 15
####################################################

T = int(input())
for test_case in range(1, T + 1):
    # 여기부터 알고리즘 구현

    # 정수 갯수 N과 연속된 숫자 M개
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    # ★ 첫 구간 숫자 합 구하기
    M_sum = 0

    for i in range(M):
        M_sum += arr[i]

    # ★ 첫 구간 숫자 합을 초기 값으로 두기
    max_sum = M_sum
    min_sum = M_sum

    # start는 "구간의 시작 위치"
    # 길이가 M인 구간이 배열 안에 완전히 들어와야 한다
    # 구간 시작 위치는 0 ~ N-M 까지만 가능
    # range 특성상 N-M를 포함시키기 위해 +1
    # range는 끝 값을 포함하지 않으므로
    # 마지막 시작 위치 N-M를 포함시키려면 +1이 필요하다
    for start in range(1, N - M + 1):
        # 시작 인덱스를 1부터 N-M까지 이동하면서
        # 이전 합에서 arr[start-1]을 빼고, arr[start+M-1]을 더한다.
        # start → 구간 시작
        # - 1 → 이전 구간의 왼쪽 끝
        # + M - 1 → 현재 구간의 오른쪽 끝
        M_sum = M_sum - arr[start - 1] + arr[start + M - 1]

        if min_sum > M_sum:
            min_sum = M_sum
        if max_sum < M_sum:
            max_sum = M_sum

    answer = max_sum - min_sum
    print(f"#{test_case} {answer}")
