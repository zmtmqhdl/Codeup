r, g, b = map(int, input().split()) # �� ����
for i in range(r) : # �ݺ��� for -> 0���� r - 1���� i�� �����ϸ� �ݺ�
    for j in range(g) : # �ݺ��� for -> 0���� g - 1���� i�� �����ϸ� �ݺ�
        for k in range(b) : # �ݺ��� for -> 0���� b - 1���� i�� �����ϸ� �ݺ�
            print(i, j ,k) # ���
print(r * g * b) # ���