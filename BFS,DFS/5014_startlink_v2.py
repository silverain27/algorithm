from collections import deque


f, s, g, u, d = map(int, input().split())# F 총 층수 , S 현재위치 , G 목적지, U 위로 , D 아래료 
visited = [-1] * (f + 1)

def bfs(goal):
    while queue:
        x = queue.popleft()

        if x == goal:
            return visited[x]

        for nx in (x + u, x - d): #위, 아래 두번 반복 
            if 0 < nx <= f and visited[nx] == -1: #방문 안한거 
                queue.append(nx)
                visited[nx] = visited[x] + 1
            print(queue)
            print(visited)
    return "use the stairs"

queue = deque()
queue.append(s)
visited[s] = 0
print("===initial que : ", queue)
print(bfs(g)) 