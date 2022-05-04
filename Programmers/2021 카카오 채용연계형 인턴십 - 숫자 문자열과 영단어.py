# 2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어
# 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.
# ex)  1478 → "one4seveneight"
# ex)  234567 → "23four5six7"
# 문자열 s가 매개변수로 주어집니다. 
s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# * 제한사항 *
# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.


# 내 답안
def solution(s):
    answer = ''
    box = ''
    number = {0:'zero',1:'one',2:'two',3:'three',4:'four',
          5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    for c in s:
        if c.isdigit(): answer += c
        else :
            box += c
            for i in range(0,10):
                if number[i] == box :
                    answer += str(i)
                    box = ''
    answer = int(answer)
    return answer


# TEST CASE Ⅰ
s = "one4seveneight"
print(solution(s))

# TEST CASE Ⅱ
s = "23four5six7"
print(solution(s))

# TEST CASE Ⅲ
s = "2three45sixseven"
print(solution(s))

# TEST CASE Ⅳ
s = "123"
print(solution(s))

# -------------------------------------------------------------------
# 두 번째 답안
def solution(s):
    answer = ''
    number_dict = { 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
                    'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9 }
    tmp = ''
    for c in s:
        if c.isalpha() :
            tmp += c
            try :
                answer += str(number_dict[tmp])
                tmp = ''
            except KeyError : pass
        else :
            answer += c 
    return int(answer)


# 세 번째 답안
def solution(s):
    number_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
                   'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for key,value in number_dict.items() :
        s = s.replace(key, str(value))
    return int(s)




## 다른 사람 풀이
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
