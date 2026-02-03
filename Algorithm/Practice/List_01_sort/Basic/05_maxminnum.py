####################################################
# [문제 5]
# 서로 다른 N개의 정수가 주어진다.
# 이 숫자들을 한 번씩만 사용하여 만들 수 있는
# 모든 순열 중,
# 인접한 두 수의 차의 절댓값 합이 가장 큰 값을 출력하시오.
#
# [개념] 순열 + 완전 검색
#
# [입력]
# 첫 줄 테스트 케이스 개수 T
# 각 테스트 케이스마다
#   - 첫 줄: 정수 N
#   - 둘째 줄: N개의 정수
#
# [입력 예시]
# 1
# 3
# 1 2 3
#
# [출력 예시]
# #1 3
# (예: 2 1 3 → |2-1| + |1-3| = 1 + 2 = 3)
####################################################
T = int(input())                     # 테스트 케이스 개수 입력
for test_case in range(1, T + 1):    # 테스트 케이스 반복

    N = int(input())                 # 숫자의 개수 N
    arr = list(map(int, input().split()))  # N개의 정수 리스트

    visited = [0] * N                # 각 숫자를 사용했는지 표시 (0: 안 씀, 1: 씀)
    perm = [0] * N                   # 현재 만들고 있는 순열 저장용 배열

    # depth : 현재 채우고 있는 자리 번호 (0번 자리부터 시작)
    def dfs(depth):

        # 모든 자리를 다 채웠다면 (순열 완성)
        if depth == N:
            total = 0                # 이 순열의 점수(차이 합)

            # 인접한 두 숫자의 차이 계산
            for i in range(N - 1):
                diff = perm[i] - perm[i + 1]   # 두 수의 차이
                if diff < 0:                   # 절댓값 처리
                    diff = -diff
                total += diff                  # 차이 누적

            return total            # 이 순열의 점수 반환

        max_value = 0               # 현재 단계에서의 최대 점수

        # 아직 사용하지 않은 숫자들을 하나씩 선택
        for i in range(N):
            if visited[i] == 0:     # 아직 안 쓴 숫자라면
                visited[i] = 1      # 사용했다고 표시
                perm[depth] = arr[i]  # 현재 자리에 숫자 넣기

                # 다음 자리를 채우러 이동
                value = dfs(depth + 1)

                # 더 큰 점수면 갱신
                if value > max_value:
                    max_value = value

                visited[i] = 0      # 다시 사용 안 한 상태로 되돌림 (백트래킹)

        return max_value            # 이 depth에서 만들 수 있는 최대 점수 반환

    answer = dfs(0)                 # 0번 자리부터 순열 만들기 시작

    print(f"#{test_case} {answer}") # 결과 출력

