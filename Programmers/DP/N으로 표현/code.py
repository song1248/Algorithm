def solution(N, number):
    answer = float('inf')
    num_list = [ int(str(N)*(i+1)) for i in range(8) ]
        
    def calculator(num=0,count = 0):
        nonlocal answer
        if count > 8:
            return

        if num == number:
            answer = min(answer, count)
            return 

        for i, N in enumerate(num_list):
            i = i+1
            calculator(num+N,count+i)
            calculator(num-N,count+i)
            calculator(num/N,count+i)
            calculator(num*N,count+i)

    calculator()
    return answer if answer !=  float('inf') else -1
