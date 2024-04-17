#섬의갯수 

import sys
from collections import deque

sys.setrecursionlimit(10000)


dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,1,-1,-1]


####### BFS ######

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while queue:
        a,b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0<=nx<h and 0<=ny<w:
                
                if visited[nx][ny] == False and graph[nx][ny] ==1:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

def DFS(x, y):
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  visited[x][y] = True
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and visited[nx][ny] == False:
      DFS(nx, ny)
      
while 1:
    graph = []
    visited = []
    w,h = map(int, input().split()) #지도 너비 w, 높이 h
    
    if(w ==0 and h ==0): break

    for i in range(h):
        graph.append(list(map(int, input().split())))
        visited.append([False] * w)
    #print(visited)
    #print(graph)
    # 1개의 테스트 케이스에 대해서 함수 실행 s
    count = 0
    for i in range(h): #여기를 거꾸로 해야하구나 ! ! 
        for j in range(w): 
            if graph[i][j] == 1 and visited[i][j] == False:
                BFS(i,j) 
                count +=1
    
    print(count)
    

####### DFS ######


