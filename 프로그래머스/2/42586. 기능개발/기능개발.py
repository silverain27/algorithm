import math

def solution(progresses, speeds):
    answer = []

    # 작업완료까지 걸리는 작업일을 먼저 전부 계산해서 리스트에 담아둔다.
    days = [math.ceil((100-p) / s) for p, s in zip(progresses, speeds)]

    index = 0 # 현재인덱스
    process = 0
    for i in range(len(days)) :
        process +=1
        if days[index] < days[i] :      # 현재 인덱스의 작업일보다 큰 작업일이 나오면
            process +=1
            answer.append(i - index)    # 둘의 차이(배포 개수)를 추가 
            index = i                   # 현재 인덱스를 갱신
            
    answer.append(len(days) - index)    # 갱신된 인덱스부터 마지막 인덱스까지의 개수

    return answer


# def solution(progresses, speeds):
#     days = []
#     for i in range(0, len(progresses)):
#         a = (100-progresses[i]) / speeds[i]
#         b =  (100-progresses[i]) % speeds[i] 
#         if b >0 :
#             days.append(int(a)+1)
#         else:   
#             days.append(int(a))
#     answer = [1]
#     for i in range(0,len(days)-1):
#         if days[i] >= days[i+1]:
#             answer[-1]+=1
#         else:
#             answer.append(1)
#     return answer
    