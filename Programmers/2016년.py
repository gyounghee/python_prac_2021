# 2016년 1월 1일은 금요일이다. 2016년 a월 b일은 무슨 요일일까?
# 두 수 a, b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수 solution을 완성하라
# 요일의 이름은 일요일부터 토요일까지 SUN,MON,TUE,WED,THU,FRI,SAT 이다.

# * 제한사항 *
# 2016년은 윤년입니다. (2월이 29일인 날)
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)


# 내 답안
def solution(a, b):
    answer = ''
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    c = (sum(month[:a-1]) + b)%7
    answer = str(day[c])
    return answer

# TEST CASE Ⅰ
a, b = 5, 24
print(solution(a,b))  #"TUE"


# 다른 사람 풀이
def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    now = 5
    for i in range(0, a - 1) :
        now += dayLen[i]

    answer = (now + b - 1) % 7

    return days[answer]

## 연도가 바뀌면 days를 고칠 필요가 없이 now하나만 바꾸면 되기 때문에 좋은 코드라고 생각함.
