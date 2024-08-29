
def solution(clothes):
    answer = 1
    category = {}
    cloth_ctg = []
    for cloth in clothes:
        if(cloth[1] not in category):
            category[cloth[1]] = 1 
        else:
            category[cloth[1]] +=1
    for a in category.values():
        answer *= a+1
    return answer-1

#입지않는 다는 선택지를 추가 


