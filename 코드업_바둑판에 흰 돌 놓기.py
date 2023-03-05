n = int(input()) # 값 대입
data = [[0 for _ in range(19)] for _ in range(19)] # list생성
for _ in range(n) : # 반복문 for -> n회 반복
    x, y = map(int, input().split()) # 값 대입
    data[x - 1][y - 1] = 1 # 값 변경
for i in range(19) : # 반복문 for -> 0부터 18까지 i에 대입하며 반복
    for j in range(19) : # 반복문 for -> 0부터 18까지 j에 대입하며 반복
        print(data[i][j], end = ' ') # 출력
    print() # 출력