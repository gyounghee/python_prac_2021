# 월간 코드 챌린지 시즌 1 - 내적
# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다.
# a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

# * 제한사항 *
# a, b의 길이는 1 이상 1,000 이하입니다.
# a, b의 모든 수는 -1,000 이상 1,000 이하입니다.

# 내 답안
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

# TEST CASE Ⅰ
a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a,b))

# TEST CASE Ⅱ
a = [-1,0,1]
b = [1,0,-1]
print(solution(a,b))


# 다른 사람 풀이
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])   
