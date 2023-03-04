data = [] # list생성
for _ in range(19) : # 반복문 for -> 19회 반복
    data.append(list(map(int, input().split()))) # 원소 대입
n = int(input()) # 값 대입
for _ in range(n) : # 반복문 for -> n회 반복
    x, y = map(int, input().split()) # 값 대입
    x, y = x - 1, y - 1 # 값 변경
    for i in range(19) : # 반복문 for -> 19회 반복
        if data[i][y] == 0 : # 조건문 if, else -> 세로줄이 0인 경우
            data[i][y] = 1 # 값 변경
        else : # 세로줄이 1인 경우
            data[i][y] = 0 # 값 변경
        if data[x][i] == 0 : # 조건문 if, else -> 가로줄이 0인 경우
            data[x][i] = 1 # 값 변경
        else : # 가로줄이 1인 경우
            data[x][i] = 0 # 값 변경
for i in range(19) : # 반복문 for -> 0부터 18까지 i에 대입하며 반복
    for j in range(19) : # 반복문 for -> 0부터 18까지 j에 대입하며 반복
        print(data[i][j], end = ' ') # 출력
    print() # 출력