data = [] # list생성
for i in range(10) : # 반복문 for -> 10회 반복 
    data.append(list(map(int, input().split()))) # 원소 대입
x, y = 1, 1 # 개미 위치 좌표
while True : # 반복문 while -> false가 반환될 때까지 반복
    if data[x][y] == 0 : # 조건문 if, elif -> 현재 개미의 위치의 번호가 0인 경우
        data[x][y] = 9 # 값 변환
    elif data[x][y] == 2 : # 현재 개미의 위치에 먹이가 있는 경우
        data[x][y] = 9 # 값 변환
        break # 중지
    if data[x][y+1] == 1 and data[x+1][y] == 1 : # 조건문 if -> 개미가 이동 불가능한 경우
        break # 중지
    if data[x][y + 1] != 1 : # 조건문 if, elif -> 개미가 오른쪽으로 이동 가능한 경우
        y = y + 1 # 개미 위치 좌표 변경
    elif data[x + 1][y] != 1 : # 개미가 아래쪽으로 이동 가능한 경우
        x = x + 1 # 개미 위치 좌표 변경
for i in range(10) : # 반복문 for -> 0부터 9까지 i에 대입하며 반복
    for j in range(10) : # 반복문 for -> 0부터 9까지 j에 대입하며 반복
        print(data[i][j], end=' ') # 출력
    print() # 출력