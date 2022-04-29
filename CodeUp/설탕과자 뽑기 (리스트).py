# 설탕과자 뽑기 (리스트)
# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l), 
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

# * 입력 *
# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1
# 1 <= x <= 100-h
# 1 <= y <= 100-w


# 내 답안
x_y = input().split()   # 만들고자 하는 행렬의 행과 열 정하기
space = [[0 for i in range(int(x_y[1]))] for j in range(int(x_y[0]))]  # 행렬(격자판) 만들기
c = int(input())  # 막대의 개수

for n in range(c):
    ldxy = input().split()
    row, col = int(ldxy[2])-1,int(ldxy[3])-1
    if ldxy[1] == '0' :
        for r in range(int(ldxy[0])):
            space[row][col+r] = 1
    elif ldxy[1] == '1' :
        for d in range(int(ldxy[0])):   
            space[row+d][col] = 1

for i in range(int(x_y[0])):
    for j in range(int(x_y[1])):
        print(space[i][j], end=' ')
    print()



# 입력 예시
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5

# 출력 예시
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
