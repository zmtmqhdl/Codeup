h, w = map(int, input().split()) # �� ����
n = int(input()) # �� ����
data = [[0] * w for _ in range(h)] # list����
for _ in range(n) : # �ݺ��� for -> nȸ �ݺ�
    l, d, x, y = map(int, input().split()) # �� ����
    for i in range(l) : # �ݺ��� for -> 0���� l - 1���� i�� �����ϸ� �ݺ�
        if d == 0 : # ���ǹ� if, else -> ������ ���
            data[x - 1][y - 1 + i] = 1 # ���� ��ġ
        else : # ������ ���
            data[x - 1 + i][y - 1] = 1 # ���� ��ġ
for i in range(h) : # �ݺ��� for -> 0���� h - 1���� i�� �����ϸ� �ݺ�
    for j in range(w) : # �ݺ��� for -> 0���� w - 1���� j�� �����ϸ� �ݺ�
        print(data[i][j], end = ' ') # ���
    print() # ���