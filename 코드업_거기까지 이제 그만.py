n = int(input()) # �� ����
result, num = 0, 1 # ���� ����
while True : # �ݺ��� while -> False�� ��ȯ�� ������ �ݺ�
    result += num # result = result + num
    num += 1 # num = num + 1
    if result >= n : # ���ǹ� if -> result�� n�̻��� ���
        break # ����
print(result) # ���