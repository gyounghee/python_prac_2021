# 완주하지 못한 선수 (해시)

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성하라

# * 제한사항 *
# - 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# - completion의 길이는 participant의 길이보다 1 작습니다.
# - 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# - 참가자 중에는 동명이인이 있을 수 있습니다.


# 내 답안  - 50점 [정확성 100, 효율성 0]  
def solution(participant, completion):
    answer = '' 
    for i in completion:
        participant.remove(i)
    answer = ','.join(participant)
    return answer

# TEST CASE Ⅰ
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))

# TEST CASE Ⅱ
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

# TEST CASE Ⅲ
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))


# 다른 사람 풀이 ①
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}                                 # dictionary 타입의 dic변수를 만듦
    for part in participant:            # part에 participant(참가자)를 차례로 넣는다
        dic[hash(part)] = part         # 참가자의 해쉬값을 key 값, 참가자의 이름을 value 값으로 하여 dic에 집어넣는다 
        temp += hash(part)           # temp 변수에 참가자의 해쉬값을 더한다
    for com in completion:          # com에 completion(완주자)를 차례로 넣는다
        temp -= hash(com)           # temp에서 완주자에 완주자의 해쉬값을 뺀다.
    answer = dic[temp]               # answer에 해당 해쉬값의 value 즉, 완주하지 못한 선수의 이름을 넣는다.
                                               # hash값은 key가 다르면 모두 다르며 temp값에는 완주하지 못한 선수의 해쉬값만 남게 되기 때문에 가능

    return answer


# 다른 사람 풀이 ②
import collections                        # collections 모듈의 Counter 클래스 사용

def solution(participant, completion):    
    answer = collections.Counter(participant) - collections.Counter(completion)
                                     	         # Counter의 함수는 컨테이너등에 동일한 자료가 몇 개인지 확인하는 데 사용하는 객체
                                   	         # Counter 함수를 통해 dictionary 타입을 만들고 참가자 - 완주자를 하여 미완주자에 대한 key, value값을 answer에 넣는다.
    return list(answer.keys())[0]         # answer에는 하나의 키와 값을 가지게 되기 때문에 이를 리스트로 변환 후 슬라이싱하여 그 값을 리턴한다 


# 다른 사람 풀이 ③
def solution(participant, completion):
    participant.sort()                                # 참가자 정렬
    completion.sort()                               # 완주자 정렬
    for i in range(len(completion)):            # 완주자 수 만큼 for문을 돌림
        if participant[i] != completion[i]:      # 만약 i번째 참가자와 i번째 완주자가 같지 않다면
            return participant[i]                    # 그 참가자는 완주를 하지 못한 것이기 때문에 i번째 참가자 리턴
    return participant[len(participant)-1]     # 만약 찾지 못하면 제일 마지막 참가자 리턴
