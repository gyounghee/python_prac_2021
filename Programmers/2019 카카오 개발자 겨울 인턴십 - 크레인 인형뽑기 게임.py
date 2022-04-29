# 2019 카카오 개발자 겨울 인턴십 - 크레인 인형뽑기 게임
# 다양한 인형이 가장 아래 칸부터 순서대로 쌓여있다. 
# moves에 따라 뽑은 인형이 바구니에 순서대로 쌓인다.
# 이때, 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이면 두 인형은 터뜨려지면서 바구니에서 사라지게 된다. 

# * 제한사항 *
# 1. board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
# 2. board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
#  → 2-1.  0은 빈 칸을 나타냅니다.
#  → 2-2.  1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
# moves 배열의 크기는 1 이상 1,000 이하입니다.
# moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

# 내가 작성한 답안
def solution(board, moves):
    box = []
    delete = 0
    for i in moves :
        for j in range(len(board[1])):
            if board[j][i-1] != 0 :
                box.append(board[j][i-1])
                board[j][i-1] = 0 
                break
        if len(box) >= 2 and box[-1] == box[-2]:
            box.pop()
            box.pop()
            delete += 2
    return delete

# TEST CASE Ⅰ
board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))


