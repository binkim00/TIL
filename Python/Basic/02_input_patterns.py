# 02_input_patterns.py
# 코딩테스트에서 자주 쓰는 입력 패턴 모음

# ✅ 1) 정수 1개
# n = int(input())

# ✅ 2) 정수 2개
# a, b = map(int, input().split())

# ✅ 3) 정수 3개
# a, b, c = map(int, input().split())

# ✅ 4) 한 줄에 여러 정수(리스트)
# arr = list(map(int, input().split()))

# ✅ 5) 문자열 1줄
# s = input().strip()

# ✅ 6) 단어 여러 개(문자열 리스트)
# words = input().split()

# ✅ 7) N줄 입력받아 리스트로 저장
# n = int(input())
# lines = [input().rstrip() for _ in range(n)]

# ✅ 8) N개의 정수(한 줄이 아니라 N줄로 주어질 때)
# n = int(input())
# nums = [int(input()) for _ in range(n)]

# ✅ 9) 2차원 행렬 입력(n행)
# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# ✅ 10) 빠른 입력 (백준에서 느릴 때)
# import sys
# input = sys.stdin.readline
# n = int(input())
# a, b = map(int, input().split())
