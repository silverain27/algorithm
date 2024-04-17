import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque()
 
for i in range(h):
    graph.append([])
    for j in range(n):
        graph[i].append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k)) #높이, 세로, 가로를 넣어줌  
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

print("==initial que : ", queue)

while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append((a,b,c))
            graph[a][b][c] = graph[x][y][z]+1
    for mm in range(h):
        print(graph[mm])
    print("que : ", queue)
    print()
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)
 