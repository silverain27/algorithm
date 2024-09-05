from itertools import product, chain


def solution(word):
    basic = ["A", "E", 'I', "O", "U"]
    word_set = basic[:] # 일단 하나씩 다있는거 추가한다 
    #print(word_set) 
    for i in range(2, 6): # 두번 반복되는 것 부터니까 
        word_set += list(map(list, product(basic, repeat=i)))
    print(word_set)
    result = sorted(list(map(lambda x: ''.join(x), word_set)))
    #print(result)
    return result.index(word) + 1