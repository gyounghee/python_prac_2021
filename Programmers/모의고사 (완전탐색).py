# 수포자 삼인방은 모의고사 수학문제를 전부 찍으려고 한다.
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성하라

# * 제한사항 *
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.


# 내 답안
def solution(answers):
    answer = []
    count= [0,0,0]
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
        
    for i in range(len(answers)):
        if p1[i%5] == answers[i] : count[0] += 1
        if p2[i%8] == answers[i] : count[1] += 1
        if p3[i%10] == answers[i] : count[2] += 1
            
    M = max(count)
    for i in range(0,3):
        if count[i] == M:
            answer.append(i+1)
    return answer

# TEST CASE Ⅰ
answers = [1,3,2,4,2]
print(solution(answers))

# 다른 사람 풀이
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):                                  # q = 0 일 때 a는  answers의 첫 번째 값
        for i, v in enumerate(p):                                        # i = 0 일 때 v는 p의 첫 번째 값 즉,[1,2,3,4,5]
            if a == v[q % len(v)]:                                        # a의 값은 answers의 첫 번 째 값 == 첫 번째 값[0 나누기 5의 나머지]를 하여 
                s[i] += 1                                                      #  답이 맞을 경우 i 번째 학생의 카운트가 올라감
    return [i + 1 for i, v in enumerate(s) if v == max(s)]      # 최대값인 i 번째 학생들을 리턴 
