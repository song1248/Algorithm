# 양의 정수 n 을 k 진수로 바꾸었을때
# 옆에 p 가이쓰면 안됨
import math
def solution(n, k):
    
    
    def transform(num, k):
        tf = ''
        while num > 0:
            mok , namuge = divmod(num, k)          
            tf = str(namuge) + tf
            num = mok
        
        return tf

#     def is_prime(num):
#         if num == 1:
#             return False
        
#         for i in range(2,num):
#             if num % i == 0:
#                 return False
#         return True

    def is_prime(n):
        if n <= 1 :
            return 0 #1은 소수가 아님.
         
	# // 짝수는 소수에서 제외
	# // 단, 2는 유일하게 짝수 중에서 소수
        if n % 2 == 0 :
            return 1 if n==2 else 0
         
        # // n이 홀수인 경우 sqrt(n)까지 나눠서 나눠떨어지는지 여부 체크
        i = 3
        while i <= math.sqrt(n) :
            # // 나눠 떨어진다면 약수에 해당하므로 소수가 아님.
            if n % i == 0 :
                return 0
            
            i += 2
        # // 위에서 걸러지지 않은 나머지 경우는 소수에 해당됨
        return 1
    
    answer_set = set()
    transform_num = transform(n, k)
    
    num_list = transform_num.split('0')
    
    answer = 0
    for num in num_list:
        if not num:
            continue
        if is_prime(int(num)):
            answer += 1
    
    
    return answer
