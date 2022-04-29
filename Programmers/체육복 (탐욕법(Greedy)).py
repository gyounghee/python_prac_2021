# 체육복 - 탐욕법(Greedy)
# 도둑이 들어, 일부 학생이 체육복을 도난당했다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성하라.

# * 제한사항 *
# - 전체 학생의 수는 2명 이상 30명 이하입니다.
# - 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# - 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# - 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# - 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

# 내 답안 
from collections import Counter
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    student = [s for s in range(1,n+1)]
    lost_n = list((Counter(lost) - Counter(reserve)).keys())
    reserve_n = list((Counter(reserve) - Counter(lost)).keys())
    for ln in range(len(lost_n)):
        for rn in range(len(reserve_n)):
            if lost_n[ln] == reserve_n[rn] :
                reserve_n[rn], lost_n[ln] = 0, 0 
            if lost_n[ln]+1 == reserve_n[rn] or lost_n[ln]-1 == reserve_n[rn] :
                reserve_n[rn], lost_n[ln] = 0, 0 
    answer = len(Counter(student) - Counter(lost_n))
    return answer

# TEST CASE Ⅰ
n, lost, reserve = 5, [2,4], [1,3,5]
print(solution(n,lost,reserve))

# TEST CASE Ⅱ
n, lost, reserve = 6, [1,3,5], [2,4,6]
print(solution(n,lost,reserve))

# TEST CASE Ⅲ
n, lost, reserve = 5, [2,4], [3,1]
print(solution(n,lost,reserve)) 

# TEST CASE Ⅳ
n, lost, reserve = 3, [1,2], [2,3]
print(solution(n,lost,reserve))



# 다른 사람 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
