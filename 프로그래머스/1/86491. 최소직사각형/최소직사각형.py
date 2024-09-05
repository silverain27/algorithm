def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        sizes[i].sort()
    
    garo = []
    sero = []
    
    for size in sizes:
        garo.append(size[0])
        sero.append(size[1])
    answer = max(garo) * max(sero)
    
    
    return answer