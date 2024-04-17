from itertools import deque

N = 4 #int(input()) #사람 수 
people = ['A','B','C','D']

length = 4 #회의록 길이 
meeting = ['C', '?', 'D', '?']

def bfs(depth, value):
    queue = deque()
    queue.append(depth,value)
    while queue():
        for i in range(length):
            if meeting[i] != '?': # 사람이면 
                
            
            elif meeting[i] == '?': # ? 이면  
        
