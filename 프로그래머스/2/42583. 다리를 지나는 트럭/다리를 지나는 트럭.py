# def solution(bridge_length, weight, truck_weights):
#     bridge = ["" for i in range(bridge_length)] # 다리를 코드화한 리스트. string형 list이다.
#     waiting = list(map(int,list(truck_weights))) # 아직 건너지 않은 대기열. waiting은 int형 list이다.
#     fin = list() # 이미 건넌 트럭. int형 list이다.
#     trucknum = len(truck_weights) # 총 트럭의 수

#     sec = 0
#     bridge_weight = 0 # 지금 다리 위에 있는 무게의 합계

#     while(1):
#         if len(fin) == trucknum: # 다 건넜으면 반복문 종료
#             return sec
#         else:                    # 다 안 건넜으면 한 칸씩 옮겨준다.
#             sec += 1

#             if bridge[0] != "":
#                 fin.append(bridge[0])
#                 bridge_weight -= int(bridge[0])
#             del bridge[0]

#             if len(waiting) == 0:
#                 bridge.append("")
#             else:           
#                 if (weight >= bridge_weight + waiting[0]): # 다음 트럭이 올라가도 버틸 수 있다면
#                     bridge.append(str(waiting[0]))
#                     bridge_weight += waiting[0]
#                     del waiting[0]
#                 else: # 다음 트럭이 못올라가면 추가로 안 올리고 지금 다리에 있는애들만 한칸씩 옮겨준다.
#                     bridge.append("")

#     return sec
from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length)  # [0]*bridge_length 을 덱으로 변환
    truck_weights = deque(truck_weights) # 리스트를 덱으로 변환
    
    currentWeight = 0
    while len(truck_weights) > 0:
        time = time + 1

        currentWeight = currentWeight - bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight = currentWeight + truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    time = time + bridge_length
    
    return time