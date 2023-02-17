n = int(input()) # 출력
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지 i에 대입하며 반복
    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9 : # 조건문 if, elif, else -> 십의 자리가 3, 6, 9인 경우
        print('X', end = '') # 출력
    elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9 : # 일의 자리가 3, 6, 9인 경우
        print('X', end = ' ') # 출력
    else : # 3, 6, 9가 들어가지 않는 경우
        print(i, end = ' ') # 출력