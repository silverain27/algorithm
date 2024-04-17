import sys 

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find_parent(x):
    if x!= parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a,b):
    a = find_parent(a) #1
    b = find_parent(b) #4 
    if a!=b:
        parent[b] = a
        number[a] += number[b]
    print(number[a]) # 여기에서 답을 print해서 제출해야함 

TestN = int(input()) # 전체 테스트 숫자 

for _ in range(TestN):
    num = int(input())
    parent, number = {}, {}
    #parent는 원래처럼 부모를 나타내는 것 
    #nubmer는 
    for i in range(num):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] =b
            number[b] = 1
        union(a, b)
        # print("~! number :", number)
        # print("@@ parent :", parent)

# for _ in range(TestN):
#     F = int(input()) #친구관계 숫자 
#     parent = []
#     n = 0
#     for i in range(F): 
#         parent
#         a, b = map(str, input().split())
#         if relation[a] == 'None':
#             relation[a] = n
#             n +=1
#         print(relation)
#         # relation[a] = # 숫자  
#         # find = union(a,b)
