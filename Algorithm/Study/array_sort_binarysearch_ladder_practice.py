# -*- coding: utf-8 -*-
############################################################
# 오늘 수업/실습 통합 정리 (정렬 + 이진탐색 + 2차원 사다리 + 파라메트릭 서치)
#
# ✅ 목표
# 1) "코드가 왜 이렇게 돌아가는지"를 한 파일에서 복습
# 2) 내장함수(특히 sorted, max, min, sum 등) 없이도 풀이 흐름을 만들 수 있게 연습
#
# ✅ 오늘 다룬 핵심 키워드
# - 선택 정렬(Selection Sort)
# - 특별한 정렬(큰/작 번갈아 배치)  ← 선택정렬 아이디어 응용
# - 이진 탐색(Binary Search)        ← 범위 줄이기/반복 횟수 세기
# - 사다리(Ladder) 2차원 이동       ← 좌/우 우선 + 방문 처리
# - 파라메트릭 서치(결정 문제 + 이진 탐색) ← candybag
#
# ----------------------------------------------------------
# ⚠️ 공통 체크리스트(시험/실습에서 자주 틀리는 포인트)
# 1) 범위(인덱스) 체크: 0 <= x < N, 0 <= y < N
# 2) while/for 중단 위치: break가 "어느 반복문"을 끊는지 항상 확인
# 3) 2차원 탐색에서 방향 우선순위: 문제 조건이 곧 로직이다
# 4) 이진 탐색에서 l/r 갱신 규칙: mid 포함/제외 기준을 문제 정의대로
# 5) 출력 형식: SWEA는 대부분 '#tc 정답' 형태
############################################################


############################################################
# 0) 선택 정렬(Selection Sort)
#
# 아이디어:
# i번째 자리에 올 값을 "남은 구간에서 가장 작은 값"으로 고정한다.
#
# 동작(오름차순):
# i = 0이면, 0~N-1 중 최소값 찾아 0과 교환
# i = 1이면, 1~N-1 중 최소값 찾아 1과 교환
# ...
#
# 시간복잡도: O(N^2)
############################################################

def selection_sort(arr):
    # arr 자체를 오름차순으로 정렬(제자리 정렬)
    N = len(arr)

    for i in range(N - 1):
        # i부터 끝까지 중 최소값의 위치 찾기
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # i와 최소값 위치 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 선택 정렬 슈도코드(시험용 암기 형태)
SELECTION_SORT_PSEUDO = '''
SelectionSort(A):
    for i = 0 .. N-2:
        min = i
        for j = i+1 .. N-1:
            if A[j] < A[min]:
                min = j
        swap(A[i], A[min])
'''


############################################################
# 1) 특별한 정렬 (큰값/작은값 번갈아)
#
# 문제 요구:
# [가장 큰 값, 가장 작은 값, 2번째 큰 값, 2번째 작은 값, ...] 를 앞에서부터 10개 출력
#
# 핵심 포인트:
# - 전체를 다 정렬할 필요가 없다.
# - "앞에서 10개 자리만" 확정하면 됨
# - 선택정렬의 '자리 확정' 아이디어 그대로 사용
#
# i가 짝수(0,2,4,...) → 이번 자리는 '최대값' 자리
# i가 홀수(1,3,5,...) → 이번 자리는 '최소값' 자리
############################################################

def special_sort_first_10(arr):
    N = len(arr)

    # 앞 10칸만 확정
    limit = 10
    if N < 10:
        limit = N

    for i in range(limit):
        pick = i

        for j in range(i + 1, N):
            # i 짝수 → 최대값 찾기
            if i % 2 == 0:
                if arr[j] > arr[pick]:
                    pick = j
            # i 홀수 → 최소값 찾기
            else:
                if arr[j] < arr[pick]:
                    pick = j

        arr[i], arr[pick] = arr[pick], arr[i]

    # 앞 10개만 반환
    result = []
    for i in range(limit):
        result.append(arr[i])
    return result


############################################################
# 2) 이진 탐색 게임 (SWEA 4839 스타일)
#
# 문제의 "이진 탐색 규칙"이 핵심:
# l=1, r=P
# mid = (l + r) // 2
# - mid == target: 종료
# - mid > target: r = mid
# - mid < target: l = mid
#
# ✅ 여기서 많은 사람들이 mid-1 / mid+1을 쓰는데,
# 이 문제는 "그렇게 정의되지 않았다"면 틀릴 수 있다.
# 문제 정의 그대로 갱신해야 함.
############################################################

def binary_search_steps(P, target):
    # P: 전체 페이지(1~P)
    # target: 찾는 페이지
    l = 1
    r = P
    steps = 0

    while True:
        steps += 1
        mid = (l + r) // 2

        if mid == target:
            return steps
        elif mid > target:
            r = mid
        else:
            l = mid


def binary_search_game(P, A, B):
    # A와 B가 각각 몇 번 만에 찾는지 비교
    a_steps = binary_search_steps(P, A)
    b_steps = binary_search_steps(P, B)

    if a_steps < b_steps:
        return "A"
    elif b_steps < a_steps:
        return "B"
    else:
        return 0


############################################################
# 3) 사다리(Ladder) 2차원 이동
#
# 핵심 조건:
# - 아래에서 위로 올라가며 출발점 찾기
# - 좌/우 이동이 가능하면 "우선" 좌/우로 이동
# - 좌/우로 이동할 때는 그 방향 길(1)이 끝날 때까지 쭉 이동
# - 그 후에 한 칸 위로 이동
#
# 실수 포인트:
# - 방문처리(또는 지나온 길 제거)를 안 하면 좌우 왕복으로 무한루프 가능
# - 출력이 for tc 루프 밖으로 나가면 테스트케이스별 출력이 망가짐
############################################################

def ladder_start_x(board):
    # board: 100x100 (0/1/2)
    # 마지막 줄에서 2의 위치 찾기
    x = 0
    for j in range(100):
        if board[99][j] == 2:
            x = j
            break

    y = 99

    # 아래 -> 위로 올라가기
    while y > 0:
        # 왼쪽 길이 있으면 왼쪽 끝까지
        if x - 1 >= 0 and board[y][x - 1] == 1:
            while x - 1 >= 0 and board[y][x - 1] == 1:
                x -= 1

        # 오른쪽 길이 있으면 오른쪽 끝까지
        elif x + 1 < 100 and board[y][x + 1] == 1:
            while x + 1 < 100 and board[y][x + 1] == 1:
                x += 1

        # 위로 1칸
        y -= 1

    return x


############################################################
# 4) CandyBag (파라메트릭 서치 = 결정 문제 + 이진 탐색)
#
# 조건:
# - 가방 1개에는 정확히 M개 사탕
# - 모든 가방의 "종류별 구성"이 동일해야 함
#
# 관찰:
# K개 가방을 만든다고 가정하면,
# i번째 종류 사탕 Ai를 K개로 똑같이 나눠 담을 때
# 한 가방에는 최대 Ai // K개까지 넣을 수 있음
#
# 그래서 한 가방에 넣을 수 있는 총 사탕 최대치 = sum(Ai // K)
# 이 값이 M 이상이면 "K개 가방 가능"
#
# K가 커질수록 Ai//K 는 작아지므로,
# "K 가능/불가능"은 단조성(모노토닉)을 가진다.
# → 이진 탐색으로 최대 K를 찾을 수 있다.
############################################################

def candybag_max_k(A, M):
    # A: 각 종류별 사탕 개수 리스트
    # M: 가방 1개에 들어가야 하는 총 사탕 개수
    N = len(A)

    # total = sum(A) (내장 sum 대신 직접)
    total = 0
    for i in range(N):
        total += A[i]

    if total < M:
        return 0

    def can_make(k):
        # k개 가방이 가능한가?
        possible = 0
        for i in range(N):
            possible += A[i] // k
            if possible >= M:
                return True
        return False

    lo = 1
    hi = total // M   # k개 가방이면 최소 k*M개 필요 → k <= total//M
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if can_make(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans


############################################################
# 5) (실습용) 입력 템플릿 모음
#
# 아래는 "원본 실습 파일들"의 입출력 형태에 맞춘 메인 루프 예시.
# (필요한 것만 골라서 쓰세요.)
############################################################

# ---------------------------
# (A) 특별한 정렬 입력 형태
# ---------------------------
def run_special_sort():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        result = special_sort_first_10(arr)
        print(f"#{tc}", *result)

# ---------------------------
# (B) 이진 탐색 게임 입력 형태
# ---------------------------
def run_binary_search_game():
    T = int(input())
    for tc in range(1, T + 1):
        P, A, B = map(int, input().split())
        winner = binary_search_game(P, A, B)
        print(f"#{tc} {winner}")

# ---------------------------
# (C) 사다리 입력 형태 (SWEA Ladder는 보통 T=10 고정)
# ---------------------------
def run_ladder():
    T = 10
    for tc in range(1, T + 1):
        input()  # 테스트케이스 번호(사용 안 함)
        board = [list(map(int, input().split())) for _ in range(100)]
        ans = ladder_start_x(board)
        print(f"#{tc} {ans}")

# ---------------------------
# (D) CandyBag 입력 형태
# ---------------------------
def run_candybag():
    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        ans = candybag_max_k(A, M)
        print(f"#{tc} {ans}")


############################################################
# ✅ 사용 방법
#
# 1) 오늘 문제 하나만 실행하고 싶으면,
#    아래에서 원하는 run_XXX()만 호출하면 됩니다.
#
# 2) 기본은 "아무것도 실행하지 않는 상태"로 둡니다.
#    (시험 환경에선 main 호출을 주석 처리하는 습관)
############################################################

if __name__ == "__main__":
    # run_special_sort()
    # run_binary_search_game()
    # run_ladder()
    # run_candybag()
    pass
