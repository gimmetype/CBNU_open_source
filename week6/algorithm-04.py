# 비재귀적으로 재귀 함수 구현하기

def recur(n: int) -> int:
    while n > 0:
        recur(n - 1)
        print(n)
        n = n -2
