n = int(input()) # 값 대입
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지 i에 대입하며 반복
    if i % 3 != 0 : # 조건문 if -> 3의 배수일 경우
        print(i, end = ' ') # 출력