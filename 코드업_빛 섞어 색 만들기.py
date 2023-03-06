r, g, b = map(int, input().split()) # 값 대입
for i in range(r) : # 반복문 for -> 0부터 r - 1까지 i에 대입하며 반복
    for j in range(g) : # 반복문 for -> 0부터 g - 1까지 i에 대입하며 반복
        for k in range(b) : # 반복문 for -> 0부터 b - 1까지 i에 대입하며 반복
            print(i, j ,k) # 출력
print(r * g * b) # 출력