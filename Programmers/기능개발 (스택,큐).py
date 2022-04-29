# 기능개발 (스택/큐)
# 기능 개선 작업을 수행 중이다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있다.
# 각 기능의 개발 속도는 다르며 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기느응ㄴ 앞에 있는 기능이 배포될 때 함께 배포 된다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하라

# * 제한사항 *
# - 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# - 작업 진도는 100 미만의 자연수입니다.
# - 작업 속도는 100 이하의 자연수입니다.
# - 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# 내 답안 
def solution(progresses, speeds):
    answer = []
    box=[]
    for i in range(len(speeds)):
        if (100- progresses[i]) % speeds[i] == 0 :
            progresses[i] = (100- progresses[i]) // speeds[i]
        else : progresses[i] = ((100- progresses[i])//speeds[i])+1
    for i in range(len(speeds)):
	    if len(box) == 0 : box.append(progresses[i])
	    elif len(box) >= 1 :
		    if box[0] >= progresses[i]:
			    box.append(progresses[i])
		    elif box[0] < progresses[i]:
			    answer.append(len(box))
			    box = []
			    box.append(progresses[i])
    answer.append(len(box))   
    return answer

# TEST CASE Ⅰ
progresses, speeds = [93,30,55], [1,30,5]
print(solution(progresses,speeds))

# TEST CASE Ⅱ
progresses, speeds = [95,90,99,99,80,99], [1,1,1,1,1,1]
print(solution(progresses,speeds))

# TEST CASE Ⅲ
progresses, speeds = [96,94], [3,3]
print(solution(progresses,speeds))


# 다른 사람 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
