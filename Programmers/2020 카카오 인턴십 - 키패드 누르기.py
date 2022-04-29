# [2020 카카오 인턴십] - 키패드 누르기
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며 엄지손가락을 사용하는 규칙은 다음과 같습니다.
# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
#4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# *제한사항*
#numbers 배열의 크기는 1 이상 1,000 이하입니다.
#numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
#hand는 "left" 또는 "right" 입니다.
#"left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
# 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.



def solution(numbers, hand):
    answer = ''
    L = 10
    R = 12
        
    for n in numbers:
        if n == 0 : n = 11
        if n == 1 or n == 4 or n == 7 :
            L = n
            answer += 'L'
        elif n == 3 or n == 6 or n == 9 :
            R = n
            answer += 'R'
        else :
            mL = abs(n - L)
            mR = abs(n - R)
            dL = (mL // 3) + (mL % 3)
            dR = (mR // 3) + (mR % 3)
            if dL > dR:
                R = n
                answer += 'R'
            elif dR > dL: 
                L = n
                answer += 'L'
            else : 
                if hand == 'right' : 
                    R = n
                    answer += 'R'
                else :
                    L = n
                    answer += 'L'
    return answer

# TEST CASE Ⅰ
numbers = [1,3,4,5,8,2,1,4,5,9,5]
hand = 'right'
print(solution(numbers, hand))

# TEST CASE Ⅱ
#numbers = [7,0,8,2,8,3,1,5,7,6,2]
#hand = 'left'
#print(solution(numbers, hand))

# TEST CASE Ⅲ
# numbers = [1,2,3,4,5,6,7,8,9,0]
# hand = 'rignt'
# print(solution(numbers, hand))
