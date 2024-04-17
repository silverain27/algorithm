#7569 토마토
from collections import deque
import sys

m, n, h = map(int, input().split()) # 가로, 세로, 높이 

graph = []
queue = deque()

for i in range(h):
    graph.append([])
    for j in range(n):
        graph[i].append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k,0)) #높이, 세로, 가로를 넣어줌     
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
    
dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz =  [0,0,0,0,-1,1]
             
def bfs():
    while queue:
        xx,yy,zz,dd = queue.popleft()
        for i in range(6):
            nx = xx + dx[i] #높이 
            ny = yy + dy[i] #세로 
            nz = zz + dz[i] #가로 
            #-----넣어준 순서대로다 ----#
            #범위 내에 있으면  
            if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                if graph[nx][ny][nz] == 0: #익지 않은 토마토이면 
                    graph[nx][ny][nz] =1#익은 토마토로 바꿔주고 
                    queue.append((nx,ny,nz,dd+1))
    return dd
 
""" ##처음에 토마토 익은 것들 다 넣어주기 
for i in range(h):
    for j in range(n): #세로 
        for k in range(m): #가로
            if graph[i][j][k] == 1: #익은 토마토
                queue.append((i,j,k,0)) #높이, 세로, 가로를 넣어줌      
                    """
answer = bfs() #bfs를 한번 돌았는데 


for i in range(h):
    for j in range(n): #세로 
        for k in range(m): #가로
            if graph[i][j][k] == 0: #익지 않은 토마토가 있으면 
                print(-1)
                exit(0)
print(answer)
            
    
                

            