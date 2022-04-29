# k 번째 수 (정렬)
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하라
# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.

# * 제한사항 *
# - array의 길이는 1 이상 100 이하입니다.
# - array의 각 원소는 1 이상 100 이하입니다.
# - commands의 길이는 1 이상 50 이하입니다.
# - commands의 각 원소는 길이가 3입니다.

# 내 답안
def solution(array, commands):
    answer = []
    for i in range(0,len(commands)):
        box = []
        for c in range(commands[i][0]-1,commands[i][1]):
            box.append(array[c])
            box.sort()
        answer.append(box[commands[i][2]-1])
    return answer

# TEST CASE Ⅰ 
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))

# 다른 사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


# 에러 났었던 부분
 for i in range(0,len(commands)):
            ~~
        box.sort()      //      ← 이부분을 고쳤더니 해결 됨
        answer.append(box[commands[i][2]-1])
    return answer

# 에러 난 이유 : box.sort()를 한 후 거기서 값을 추출하려고 하니 인덱스 범위 에러가 남.  →  sort method 자체가 return 값이 없기 때문에 해당 method의 return을 받는 box에는 none값이 할당되기 때문이다.
(애초에 값을 입력하면서 정렬을 한 후 answer에 값을 추가하도록 코드를 수정함)
