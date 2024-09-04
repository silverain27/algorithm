
# def solution(priorities, location):
#     answer = 0
#     from collections import deque
#     from string import ascii_uppercase

#     index_labels = ascii_uppercase[:len(priorities)]
#     d = deque([(v, i, index_labels[i]) for i, v in enumerate(priorities)])
#     print(d)
#     while len(d):
#         item = d.popleft()
#         if d and max(d)[0] > item[0]: # pop했을떄 d확인해줘야함 아무것도 없을수도 있어서
#             d.append(item)
#             print(d)
#         else:
#             answer += 1
#             if item[1] == location:
#                 break
#     print("answer :", answer)
#     return answer

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer