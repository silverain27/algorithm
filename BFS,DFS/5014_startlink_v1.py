from collections import deque
import sys

##입력 
F, S, G, U, D = map(int, sys.stdin.readline().split()) # F 총 층수 , S 현재위치 , G 목적지, U 위로 , D 아래료 
visited = [0 for i in range(F+1)]
count = [0 for i in range(F+1)]


def bfs(floor):
    queue = deque()
    queue.append(floor) #현재위치를 시작으로 ! 
    visited[floor] = 1
    while queue:
        middle = queue.popleft() 
        if middle == G: #목적지이면 
            return count[G] #그대로 리턴 
        
        ##위 
        if 0 < middle + U <= F and not visited[middle + U]:
                visited[middle + U] = 1
                count[middle + U] = count[middle] + 1
                queue.append(middle + U)
        #아래 
        if 0 < middle - D <= F and not visited[middle - D]:
                visited[middle - D] = 1
                count[middle - D] = count[middle] + 1
                queue.append(middle - D)

    if count[G] == 0:
        return "use the stairs"


print(bfs(S)) 