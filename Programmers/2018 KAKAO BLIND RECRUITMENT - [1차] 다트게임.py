# 2018 KAKAO BLIND RECRUITMENT - [1차] 다트게임
# ▼ 다트 게임의 점수 계산 로직 ▼
# 1. 다트 게임은 총 3번의 기회로 구성된다.
# 2. 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 3. 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 4. 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 5. 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 6. 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 7. 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# 8. Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 9. 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.

#0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

# 입력형식 
# * 점수는 0에서 10 사이의 정수이다.
# * 보너스는 S, D, T 중 하나이다.
# * 옵선은 *이나 # 중 하나이며, 없을 수도 있다.

# 내 답안
def solution(dartResult):
    answer = []
    pre = 0
    for c in dartResult :
        if c == 'S' :
            pre = int(pre)**1
            answer.append(pre)
        elif c == 'D' :
            pre = int(pre)**2
            answer.append(pre)
        elif c == 'T' :
            pre = int(pre)**3
            answer.append(pre)
        elif len(answer) >= 1 and c == '#' :
            a1 = answer.pop()
            answer.append(a1*(-1))
        elif c == '*' :
            if len(answer) == 1 : 
                b= answer.pop()
                answer.append(b * 2)
            else: 
                b = answer.pop()
                f= answer.pop()
                answer.append(f * 2)
                answer.append(b * 2)
        else :
            if '0' in c : 
                if pre == '1' : pre = 10
                else : pre = 0
            else : pre = c
    answer = sum(answer)
    return answer

# TEST CASE Ⅰ
dartResult = '1S2D*3T*'
print(solution(dartResult))

# TEST CASE Ⅱ
dartResult = '1D#2S*3S'
print(solution(dartResult))

# TEST CASE Ⅲ
dartResult = '1D2S#10S'
print(solution(dartResult))
