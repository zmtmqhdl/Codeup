n = int(input()) # ���
for i in range(1, n + 1) : # �ݺ��� for -> 1���� n���� i�� �����ϸ� �ݺ�
    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9 : # ���ǹ� if, elif, else -> ���� �ڸ��� 3, 6, 9�� ���
        print('X', end = '') # ���
    elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9 : # ���� �ڸ��� 3, 6, 9�� ���
        print('X', end = ' ') # ���
    else : # 3, 6, 9�� ���� �ʴ� ���
        print(i, end = ' ') # ���