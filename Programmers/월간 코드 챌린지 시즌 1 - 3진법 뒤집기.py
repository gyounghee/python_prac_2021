# 월간 코드 챌린지 시즌 1 - 3진법 뒤집기
# 자연수 n이 매개변수로 주어집니다. 
# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요

# * 제한사항 *
# n은 1 이상 100,000,000 이하인 자연수입니다.

# 내 답안 
def solution(n):
    answer, l = 0, 0
    three = []
    while n :   # 3진법으로 변환
        n, r = n // 3, n % 3
        three.insert(0,r)
    three.reverse()  # 앞뒤 반전 3진법
    for i in range(len(three)-1,-1,-1):  # 3진법 → 10진법
        answer += three[l] * (3**i)
        l += 1
    return answer

# TEST CASE Ⅰ
n = 45
print(solution(n))

# TEST CASE Ⅱ
n = 125
print(solution(n)



# 다른 사람 풀이
def solution(n):
    tmp = ''
    while n:                      # while문이 거짓이면 끝 즉, n = 0이 되면 반복문 종료
        tmp += str(n % 3)   # tmp에 n % 3을 하여 나온 나머지를 문자열로 추가 
        n = n // 3               # n을 3으로 나눈 몫으로 갱신

    answer = int(tmp, 3)    #  3진법 tmp를 10진법으로 변환 
    return answer
