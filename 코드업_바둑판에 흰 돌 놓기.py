n = int(input()) # �� ����
data = [[0 for _ in range(19)] for _ in range(19)] # list����
for _ in range(n) : # �ݺ��� for -> nȸ �ݺ�
    x, y = map(int, input().split()) # �� ����
    data[x - 1][y - 1] = 1 # �� ����
for i in range(19) : # �ݺ��� for -> 0���� 18���� i�� �����ϸ� �ݺ�
    for j in range(19) : # �ݺ��� for -> 0���� 18���� j�� �����ϸ� �ݺ�
        print(data[i][j], end = ' ') # ���
    print() # ���