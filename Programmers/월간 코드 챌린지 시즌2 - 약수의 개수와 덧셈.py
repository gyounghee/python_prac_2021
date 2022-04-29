# 월간 코드 챌린지 시즌2 - 약수의 개수와 덧셈
# 두 정수 left와 right가 매개변수로 주어진다.
# left부터 right까지의 모든 수 들 중, 약수의 개수가 짝수인 수는 더하고, 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해라.

# * 제한사항 *
# 1 ≤ left ≤ right ≤ 1,000

# 내 답안 
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        count = 0
        for n in range(1,i+1):
            if i % n == 0 : count += 1
        if count % 2 == 0 : answer += i
        else : answer -= i
    return answer

# TEST CASE Ⅱ
left, right = 13, 17
print(solution(left, right))

# TEST CASE Ⅰ
left, right = 24, 27
print(solution(left, right))


## 다른 사람 풀이
#def solution(left, right):
#    answer = 0
#    for i in range(left,right+1):
#        if int(i**0.5)==i**0.5:
#            answer -= i
#        else:
#            answer += i
#    return answer

