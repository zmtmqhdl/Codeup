h, w = map(int, input().split()) # 값 대입
n = int(input()) # 값 대입
data = [[0] * w for _ in range(h)] # list생성
for _ in range(n) : # 반복문 for -> n회 반복
    l, d, x, y = map(int, input().split()) # 값 대입
    for i in range(l) : # 반복문 for -> 0부터 l - 1까지 i에 대입하며 반복
        if d == 0 : # 조건문 if, else -> 가로인 경우
            data[x - 1][y - 1 + i] = 1 # 막대 배치
        else : # 세로인 경우
            data[x - 1 + i][y - 1] = 1 # 막대 배치
for i in range(h) : # 반복문 for -> 0부터 h - 1까지 i에 대입하며 반복
    for j in range(w) : # 반복문 for -> 0부터 w - 1까지 j에 대입하며 반복
        print(data[i][j], end = ' ') # 출력
    print() # 출력