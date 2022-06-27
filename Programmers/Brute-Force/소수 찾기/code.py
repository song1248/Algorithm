from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num_set = set()
    for i in range(len(numbers)):
        permu = permutations(numbers, i+1)
        for p in permu:
            num_set.add(int("".join(p)))
            
    for num in num_set:
        prime_num = True
        for j in range(2,num):
            if num % j == 0:
                prime_num = False
                break
        if prime_num == True and num != 1 and num != 0:
            answer+=1
        
    return answer
  
 # from itertools import permutations 을 이용
