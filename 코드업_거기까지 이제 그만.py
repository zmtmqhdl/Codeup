n = int(input()) # 값 대입
result, num = 0, 1 # 변수 생성
while True : # 반복문 while -> False가 반환될 때까지 반복
    result += num # result = result + num
    num += 1 # num = num + 1
    if result >= n : # 조건문 if -> result가 n이상인 경우
        break # 중지
print(result) # 출력