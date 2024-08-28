'''
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1,p2)
        if p2.startswith(p1):
            return False

def solution(phone_book):
    answer = True
    phone_book.sort() #sort함수는 list함수 자체를 sort시키는 것이기 때문에 대입할 필요가 없다 
    #print(phone_book)
    for i in range(len(phone_book)-1):
        #print(phone_book[i], phone_book[i+1], phone_book[i].startswith(phone_book[i+1]),phone_book[i+1].startswith(phone_book[i]) )
        if phone_book[i].startswith(phone_book[i+1]) or phone_book[i+1].startswith(phone_book[i]):
            return False
        
        else:
            answer = True
        
    return answer
'''
2
3
4
5
6
7
8
9
10
11
12
13
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer