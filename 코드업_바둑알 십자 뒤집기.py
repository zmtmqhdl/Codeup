data = [] # list����
for _ in range(19) : # �ݺ��� for -> 19ȸ �ݺ�
    data.append(list(map(int, input().split()))) # ���� ����
n = int(input()) # �� ����
for _ in range(n) : # �ݺ��� for -> nȸ �ݺ�
    x, y = map(int, input().split()) # �� ����
    x, y = x - 1, y - 1 # �� ����
    for i in range(19) : # �ݺ��� for -> 19ȸ �ݺ�
        if data[i][y] == 0 : # ���ǹ� if, else -> �������� 0�� ���
            data[i][y] = 1 # �� ����
        else : # �������� 1�� ���
            data[i][y] = 0 # �� ����
        if data[x][i] == 0 : # ���ǹ� if, else -> �������� 0�� ���
            data[x][i] = 1 # �� ����
        else : # �������� 1�� ���
            data[x][i] = 0 # �� ����
for i in range(19) : # �ݺ��� for -> 0���� 18���� i�� �����ϸ� �ݺ�
    for j in range(19) : # �ݺ��� for -> 0���� 18���� j�� �����ϸ� �ݺ�
        print(data[i][j], end = ' ') # ���
    print() # ���