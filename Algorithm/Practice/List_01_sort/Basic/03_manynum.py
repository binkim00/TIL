####################################################
# [문제 3]
# 0부터 9까지의 숫자로 이루어진 N개의 숫자가 주어진다.
# 가장 많이 등장한 숫자와 그 개수를 출력하시오.
# (개수가 같다면 숫자가 큰 쪽을 출력)
#
# [개념] 카운트 배열 / 카운팅 정렬 사고
#
# [입력]
# 첫 줄 테스트 케이스 개수 T
# 각 테스트 케이스마다
#   - 첫 줄: 정수 N
#   - 둘째 줄: 공백 없이 주어진 숫자 N개
#
# [입력 예시]
# 1
# 8
# 12233444
#
# [출력 예시]
# #1 4 3
####################################################
T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().strip()))  # 숫자 하나씩 리스트로 변환

    # 숫자(0~9)별로 "나온 횟수"를 저장하는 배열
    cnt = [0] * 10

    # arr를 한 번 쭉 보면서
    # 해당 숫자 칸(cnt[x])에 나온 횟수를 누적
    for x in arr:
        cnt[x] += 1   # x라는 숫자가 나올 때마다 1씩 증가

    max_cnt = 0
    max_num = 0

    for num in range(10):
        # cnt[num] = num이라는 숫자가 전체에서 나온 횟수
        if cnt[num] > max_cnt:
            max_cnt = cnt[num]
            max_num = num
        elif cnt[num] == max_cnt and num > max_num:
            max_num = num

    print(f"#{test_case} {max_num} {max_cnt}")

