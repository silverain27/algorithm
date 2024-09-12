def DFS(i, visited, n, computers):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a, visited, n, computers)    
                
def solution(n, computers):            
    
           
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i, visited, n, computers)
            answer += 1
        
    return answer