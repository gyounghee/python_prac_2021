# 문제
# 민우 동생이 로또에 낙서함 → 안보이는 부분은 0으로 표기
# 당첨 가능한 최고 순위와 최저 순위 구하기
# 1등 - 6개  /  2등 - 5개  / 3등 - 4개  / 4등 - 3개  /  5등 - 2개  /  6등(낙첨) - 그 외

#  * 제한사항 *
# lottos는 길이 6인 정수 배열입니다.
# lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
# 0은 알아볼 수 없는 숫자를 의미합니다.
# 0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
# lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
# win_nums은 길이 6인 정수 배열입니다.
# win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
# win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
# win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다.

# 나의 답
def solution(lottos, win_nums):
    answer = []
    high, low, zero = 0, 0, 0
    for l in lottos:
        for w in win_nums :
            if l == w : low += 1
        if l == 0 : zero += 1
    answer.append(low + zero)
    answer.append(low)

    for i in range(0,2):
        if answer[i] == 6 : answer[i] = 1
        elif answer[i] == 5 : answer[i] = 2
        elif answer[i] == 4 : answer[i] = 3
        elif answer[i] == 3 : answer[i] = 4
        elif answer[i] == 2 : answer[i] = 5
        else : answer[i] = 6
            
    return answer

## 다른 사람 풀이
#def solution(lottos, win_nums):
#
#    rank=[6,6,5,4,3,2,1]
#
#    cnt_0 = lottos.count(0)
#    ans = 0
#    for x in win_nums:
#        if x in lottos:
#            ans += 1
#    return rank[cnt_0 + ans],rank[ans]

# TEST CASE Ⅰ
lottos = [44,1,0,0,31,25]
win_nums = [31,10,45,1,6,19]
print(solution(lottos, win_nums))

# TEST CASE Ⅱ
lottos = [0,0,0,0,0,0]
win_nums = [38,19,20,40,15,25]
print(solution(lottos, win_nums))

# TEST CASE Ⅲ
lottos = [45,4,35,20,3,9]
win_nums = [20,9,3,45,4,35]
print(solution(lottos, win_nums))
