#2667 단지 번호 붙이기

from collections import deque

n = int(input())
graph = []
#visited = []
result= []

for i in range(n):
    graph.append(list(map(int, input())))
    #visited.append([False]*n) --> 맞는 예시 1
    
#visited = [[False] * N] * N  --> 틀린 예시 
visited = [[False]*n for _ in range(n)] ## 맞는 예시 2

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#print(graph)
#print("---visited", visited)

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    count = 0 
    while queue:
        a,b = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0<=nx<n and 0<=ny<n: # 조건이 조금 더 직관적임 
                if visited[nx][ny] == False and graph[nx][ny] == 1: # 여기서 한번더 확인해줘야함 
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    count +=1    
    return count
                
for i in range(n):
    for j in range(n):
        if(graph[i][j]==1 and visited[i][j]==False):
            count = BFS(i,j)
            result.append(count)
            
          
print(len(result))
result.sort()
for res in result:
    print(res+1)