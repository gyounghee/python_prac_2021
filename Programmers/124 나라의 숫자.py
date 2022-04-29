# 124 나라의 숫자
# 124 나라에는 자연수만 존재하며 모든 수를 표현할 때 1, 2, 4만 표현한다.
# ex)  1 → 1   /   2 → 2   /   3 → 4   /   4 → 11   /   5 → 12   /   6 → 14   /   7 → 21   /   8 → 22   /   9 → 24   /   10 → 41

# * 제한사항 *
# - n은 500,000,000이하의 자연수 입니다.

# 내 답안
def solution(n):
    answer = ''
    if n <= 3:
        if n % 3 == 0 :answer += str(4)
        else : answer += str(n % 3)
    if n > 3 :
        if n % 3 == 0 :
            answer += str(solution(n//3-1))
            answer += str(4)
        else : 
            answer += solution(n//3)
            answer += str(n%3)
    return answer

# TEST CASE Ⅰ
print(solution(21))

# 다른 사람 풀이 Ⅰ
def change124(n):
    num = ['1','2','4']
    answer = ""
    
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

# 다른 사람 풀이 Ⅱ
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]

print(change124(10))
