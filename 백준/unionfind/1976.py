#여행 가자 
#도시가 모두 연결되어있어야지만 가능하다가 핵심 

import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline


N = int(input()) # 도시의 수 200이하 
M = int(input()) # 여행 계획에 속한 도시의 수 M 1000이하 


# 부모
def find_parent(x):
    if parent[x] != x: # 자기자신이 아니면 
        parent[x] = find_parent(parent[x])
    return parent[x]

# 합집합 
def union(a,b):
    a = find_parent(a) # 1
    b = find_parent(b) # 4
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b

parent = [i for i in range(N+1)] #노드수 0 1 2가 있다 
for i in range(1,N+1):  
    linkinfo = list(map(int, input().split())) #여기도 N만큼 있다 
    for j in range(1,N+1): #1부터 N까지 
        if linkinfo[j-1]==1:
            union(i,j)

# 마지막 여행 계획
plan = list(map(int, input().split()))
first = parent[plan[0]] # 여행 시작 1이면 

# 계획에 포함된 도시 노드의 부모노드가 모두 같은 parent를 갖고있으면 
print('YES' if all(first == parent[i] for i in plan) else 'NO')

