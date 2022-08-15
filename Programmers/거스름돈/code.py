def solution(n, money):
    
    answer = 0
    money.sort()
    # idx에 해당하는 money를 만들 수 있는 경우의 수를 구한다
    n_of_case = [ 0 for _ in range(n + 1)]
    n_of_case[0] = 1
    
    
    def find_case(num, money):
        n_of_case[num]

    for m in money:
        for i in range(len(n_of_case)):
            if i < m:
                continue      
            else:
                n_of_case[i] = n_of_case[i - m] + n_of_case[i]
    
    return n_of_case[-1] % 1000000007
