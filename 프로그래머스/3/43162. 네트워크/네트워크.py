# def DFS(i, visited, n, computers):
#         visited[i] = 1
#         for a in range(n):
#             if computers[i][a]==1 and not visited[a]:
#                 DFS(a, visited, n, computers)    
                
# def solution(n, computers):                  
#     answer = 0
#     visited = [False] * n 
#     # 뭉탱이는 시작점이 없으니까 모든 컴퓨터를 다 본다 
#     for i in range(n):
#         if not visited[i]: #
#             DFS(i, visited, n, computers)
#             answer += 1 # 뭉탱이 끝나면 count 해주기 
        
#     return answer

from collections import deque

def bfs(n, start, visited, computers):
        visited[start] = True
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for i in range(n):
                # 방문하지 않은 연결된 컴퓨터
                if computers[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    
def solution(n, computers):
    answer = 0
    visited = [False] * n

    # 방문하지 않은 컴퓨터 중 작은 번호부터 BFS 수행
    for i in range(n):
        if not visited[i]:
            bfs(n, i, visited, computers)
            answer += 1

    return answer
