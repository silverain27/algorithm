from collections import deque


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split()) # 정점갯수, 간선갯수, 탐색 시작할 정점 번호 
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) #양방향 그래프 만들어주는 방법 
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)
dfs(V)
print()

# bfs
visited = [False] * (N + 1)
bfs(V)