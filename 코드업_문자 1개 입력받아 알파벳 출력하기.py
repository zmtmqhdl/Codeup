n = ord(input()) # 값 대입
start = ord('a') # a의 아스키코드 값
while start <= n : # 반복문 while -> 입력한 문자가 아닐 경우
    print(chr(start), end = ' ') # 출력
    start += 1 # start = start + 1