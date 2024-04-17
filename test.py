from itertools import combinations

queue = [2,3, 6, 7, 10, 11, 12, 15, 16, 17, 21, 22, 30] #17개 #13개

def grouping():
    packet = []
    tmp = []
    v = queue.pop(0)
    tmp.append(v)
    while(len(queue)>0):
        vv = queue.pop(0)
        print(vv)
        if v+1 == vv:
            tmp.append(vv)
            v = vv
        else:
            packet.append(tmp)
            tmp = []
            tmp.append(vv)
            v = vv #이전껄로 대체 
        
    packet.append(tmp)
    return packet

select = []
for i in range(1, queue[-1]):
    if i not in queue:
        select.append(i)

selectCount = queue[-1]-len(queue)

for i in range(selectCount):
    aa = list(map(''.join, map(int, combinations(select, i))))
    print("aa", aa)
    a = queue + aa
    print("a", a)
    
    if i == 3:
        break
    