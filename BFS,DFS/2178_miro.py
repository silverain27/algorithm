#2178 미로탐색 

from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

def bfs(x, y):
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  queue = deque() #여기 안에서 que를 생성한다  
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 벽이므로 진행 불가
      if graph[nx][ny] == 0:
        continue
      
      # 벽이 아니므로 이동
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1 # 그 전값에다가 +1만 해줌 
        queue.append((nx, ny))
        #print(graph)
  
  # 마지막 값에서 카운트 값을 뽑는다.
  # print(graph)
  return graph[N-1][M-1]

print(bfs(0, 0)) # 0,0에서 출발 