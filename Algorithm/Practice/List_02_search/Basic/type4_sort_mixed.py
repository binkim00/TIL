####################################################
# [유형 4] 정렬 구현 (난이도 혼합)
#
# 길이가 N인 배열이 주어진다.
# 1) 버블 정렬
# 2) 선택 정렬
# 을 각각 구현하여 오름차순 정렬 결과를 출력하시오.
# (내장 정렬 함수 사용 금지)
####################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    bubble = arr[:]
    select = arr[:]

    # TODO: 버블 정렬 구현
    # TODO: 선택 정렬 구현

    print(f"#{tc}")
    print("bubble:", *bubble)
    print("select:", *select)
