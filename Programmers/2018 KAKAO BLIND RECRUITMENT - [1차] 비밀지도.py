# 2018 KAKAO BLIND RECRUITMENT - [1차] 비밀지도

# 1. 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
# 2. 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
# 3. "지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
# 4. 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

# * 입력 형식 *
# 입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.
# - 1 ≦ n ≦ 16
# - arr1, arr2는 길이 n인 정수 배열로 주어진다.
# - 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2n - 1을 만족한다.

# * 출력 형식 *
# - 원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.


# 내 답안
def solution(n, arr1, arr2):
    bit = []
    for num in range(1,3):
        if num == 1: arr = arr1
        else : arr = arr2
        for i in range(n):
            arr[i] = bin(arr[i])
            arr[i] = arr[i].replace("0b","")
            arr[i] = arr[i].zfill(len(arr))

    bit = list(arr1.copy())

    for i in range(n):
        bit[i] = list(bit[i])
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0': bit[i][j] = ' '
            else : bit[i][j] = '#'
        bit[i] = ''.join(bit[i])
    return bit

# TEST CASE Ⅰ
n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
print(solution(n, arr1, arr2))

# TEST CASE Ⅱ
n = 6
arr1 = [46,33,33,22,31,50]
arr2 = [27,56,19,14,14,10]
print(solution(n, arr1, arr2))


# 다른 사람 풀이 ①
import re             # 정규식 사용

def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = bin(arr1[i]|arr2[i])[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer


# 다른 사람 풀이 ②
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
