
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer
