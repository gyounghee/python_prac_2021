# 소수 만들기
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성하라.

# * 제한사항 *
# - nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# - nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

# 내 답안
def solution(nums):
    answer,s = 0, 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                count = 0
                s = nums[i] + nums[j] + nums[k]
                for n in range(1,s+1):
                    if s % n == 0 :
                        count+=1
                if count == 2 : answer += 1
    return answer

# TEST CASEⅠ
nums = [1,2,3,4]
print(solution(nums))

# TEST CASE Ⅱ
nums = [1,2,7,6,4]
print(solution(nums))

# 다른 사람 풀이
def solution(nums):
    from itertools import combinations as cb  
    answer = 0
    for a in cb(nums, 3):             # nums에 있는 수 중 3개씩 묶은 값들을 순서대로 a에 넣음   
        cand = sum(a)                  # 3개 씩 묶여져 저장되어 있는 a의 3가지 숫자의 합을 구하여 cand에 넣음
        for j in range(2, cand):       # 2부터 cand-1 까지 순서대로 j에 넣음
            if cand%j==0:                # 만약 cand를 j로 나눴을 때 나머지가 0이라면  즉, 나눠진다면
                break                         # for문에서 나와서 맨위의 for문을 이어서 실행한다. 
        else:                                   # 만약 cand를 j로 나눴을 때 나눠지지 않는다면 즉, 소수라면
            answer += 1                   # answer값을 1 올린다.
    return answer

# ** 새로 알게 된 내용 **
# itertools (python의 내장 라이브러리)
from itertools import combinations as cb 
ex) cb ('ABCD' , 2)  → AB AC AD BC BD CD
ex)  cb ('ABCD' , 3) → ABC ABD ACD BCD 

* combinations( ) → 정렬된 순서, 반복 X
