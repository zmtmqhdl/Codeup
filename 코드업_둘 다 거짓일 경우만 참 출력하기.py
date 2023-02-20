a, b = map(int, input().split()) # 값 대입
a = bool(int(a)) # bool변환
b = bool(int(b)) # bool변환
print(not(a or b))