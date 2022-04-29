# 2021 KAKAO BLIND RECRUITMENT - 신규 아이디 추천

# 신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때,
# "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성하라

# * 규칙 *
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# * 제한사항 *
# new_id는 길이 1 이상 1,000 이하인 문자열입니다.
# new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
# new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.


# 내 답안
import re

def dot(answer) :                                                           #  # 4단계 : 아이디의 처음 or 마지막에 위치한 마침표(.) 제거
    if answer[0] == '.' : answer = answer[1:]  
    if answer[-1] =='.' : answer = answer[:-1]
    return answer

def solution(new_id):
    answer = new_id.lower()                                                  # 1단계 : new_id의 모든 대문자를 소문자로 치환
    answer = re.sub(r'[^a-z-0-9_.]',"",answer)                           # 2단계 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    while '..' in answer : answer = answer.replace('..','.')              # 3단계 : 마침표(.)가 2번 이상 연속 된 부분을 하나의 마침표(.)로 치환
    if len(answer) == 0 or answer == '.' : answer = 'aaa'           # 필요에 의해 추가한 코드
    answer = dot(answer)                                                       # 4단계 
    answer = answer.replace(" ","a")                                        # 5단계 : 아이디가 빈 문자열이라면, 빈 문자열에 "a" 대입
    if len(answer) >= 16 : answer = answer[:15]                         # 6단계 : 아이디의 길이가 16자 이상이면, 처음 15자를 제외한 나머지 문자 제거
    answer = dot(answer)                                                       # 4단계 한번 더 
    for i in range(3):                                                               # 7단계 : 아이디의 길이가 2자 이하라면, 마지막 문자를 아이디 길이가 3이 될 때까지 반복해서 끝에 붙인다.
        if len(answer) <= 2 : answer += answer[-1]
        if len(answer) == 3 : break
    return answer

# TEST CASE Ⅰ
new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))

# TEST CASE Ⅱ
new_id = "z-+.^."
print(solution(new_id))

# TEST CASE Ⅲ
new_id = "=.="
print(solution(new_id))

# TEST CASE Ⅳ
new_id = "123_.def"
print(solution(new_id))

# TEST CASE Ⅴ
new_id = "abcdefghijklmn.p"
print(solution(new_id))



# 다른 사람 풀이
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
