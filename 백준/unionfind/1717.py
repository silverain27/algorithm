# union find 알고리즘 
# 서로소 집합 알고리즘이라고도 불리는 알고리즘으로 
# 구체적으로 여러개 노드가 존재할 떄 두개의 노드를 선택해서 
# 현재 노드가 서로 같은 그래프에 속하는지 판별하는 알고리즘 


# ❓ Disjoint-Set(서로소 집합) 이란 무엇일까요?
# 👉 서로 중복되지 않는 부분 
# 집합들로 나눠진 원소들에 대한 정보를 저장하고 
# 조작하는 자료구조입니다. 
# 즉, 공통 원소가 없는 부분 집합들로 나눠진 원소들에 대한 자료구조입니다.
#https://velog.io/@ywc8851/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Union-Find-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

# 1. 찾기 연산 함수 
def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x] 
# 자기자신이 나올때까지 return을 함 

# 2. 합집합 연산 함수 
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b]=a #작은 부모의 루트로 바꿔줌 
    else:
        parent[a]=b


# n+1개의 집합이 있다 0부터 n까지 / m은 연산갯수
n,m = map(int, input().split()) # 0~8까지가 있고 연산갯수는 총 8개이다 
test = []
parent = [i for i in range(n+1)] # 각각 번호의 노드의 parent 를 일단 자기 자신으로 초기화시킴 




for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr ==0: # 합집합 연산 
        union_parent(a,b)
    else: # 1번이면 같은집합에 포함되어있는지 찾기 
        if find_parent(a) == find_parent(b):
            print("yes")
        else:
            print("no")




#합집합은 0ab 두원소가 같은집합에 포함되어있는지는 1ab
#a,b가 같은 집합이면 Yes 아니면 No




