data = [] # list����
for i in range(10) : # �ݺ��� for -> 10ȸ �ݺ� 
    data.append(list(map(int, input().split()))) # ���� ����
x, y = 1, 1 # ���� ��ġ ��ǥ
while True : # �ݺ��� while -> false�� ��ȯ�� ������ �ݺ�
    if data[x][y] == 0 : # ���ǹ� if, elif -> ���� ������ ��ġ�� ��ȣ�� 0�� ���
        data[x][y] = 9 # �� ��ȯ
    elif data[x][y] == 2 : # ���� ������ ��ġ�� ���̰� �ִ� ���
        data[x][y] = 9 # �� ��ȯ
        break # ����
    if data[x][y+1] == 1 and data[x+1][y] == 1 : # ���ǹ� if -> ���̰� �̵� �Ұ����� ���
        break # ����
    if data[x][y + 1] != 1 : # ���ǹ� if, elif -> ���̰� ���������� �̵� ������ ���
        y = y + 1 # ���� ��ġ ��ǥ ����
    elif data[x + 1][y] != 1 : # ���̰� �Ʒ������� �̵� ������ ���
        x = x + 1 # ���� ��ġ ��ǥ ����
for i in range(10) : # �ݺ��� for -> 0���� 9���� i�� �����ϸ� �ݺ�
    for j in range(10) : # �ݺ��� for -> 0���� 9���� j�� �����ϸ� �ݺ�
        print(data[i][j], end=' ') # ���
    print() # ���