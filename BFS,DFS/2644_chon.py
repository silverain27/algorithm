from collections import deque

N = int(input())#전체 사람 수 
a, b = map(int, input().split()) #계산해야하는 서로 다른 사람의 번호 

M = int(input()) #부모 자식 관계 수 
graph = [[] for _ in range(N+1)] 
visited = [False] * (N+1)
for i in range(M):
    mom,son = map(int, input().split())
    graph[mom].append(son)
    graph[son].append(mom)
    
def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if visited[n] == False:
                visited[n] = visited[node]+1
                queue.append(n)
                
bfs(a)
print(visited[b] if visited[b] > 0 else -1)