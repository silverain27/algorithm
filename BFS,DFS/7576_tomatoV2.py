#토마토 
from collections import deque

M, N = map(int, input().split()) #가로M,세로 N
box = []
for i in range(N):
    box.append(list(map(int, input().split())))
# 0: 안익은 토마토 1: 익은 토마토 , -1 :토마토가 없음 
   
queue = deque()  # 이문제는 여기서 큐를 생성하는게 다르다는 포인트 ! !            
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))
#1인 애들을 일단 쭉 다 넣어준다 



def BFS():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        a,b = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<M and box[nx][ny] == 0:
                queue.append((nx,ny))
                box[nx][ny] = box[a][b] +1 ##최단 거리를 구하는 것 처럼 그 전 위치에다가 값을 더해준다 
        #print(box)

BFS()

res = 0
for tomatoes in box:
    if 0 in tomatoes:
        print(-1)
        exit(0)
    res = max(res, max(tomatoes))

print(res-1)



        
        
                   