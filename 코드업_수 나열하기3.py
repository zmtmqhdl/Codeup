a, m, d, n = map(int, input().split()) # 값 대입
for _ in range(n - 1) : # 반복문 for -> n - 1회 반복
    a = a * m + d # a = a * m + d 
print(a) # 출력