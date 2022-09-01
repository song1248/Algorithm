# from functools import lru_cache
from collections import defaultdict
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def calc(num1, num2, operator):
            num1 = int(num1)
            num2 = int(num2)
            match operator:
                case '+':
                    return num1 + num2
                case '-':
                    return num1 - num2
                case '*':
                    return num1 * num2
                
        operators = ("+", "-", "*", "/")
        
        def explore(expression = expression):
            
            # if len(expression) == 1:
            #     return [expression[0]]
            
            answer = []
            
            # return_point = True
            for i, value in enumerate(expression):
                if value in operators:
                    # return_point = True
                    # 왼쪽에서 나올 수 있는 값들
                    left = explore(expression[:i])
                    # 오른쪽에서 나올 수 있는 값들
                    right = explore(expression[i+1:])
                    
                    for l in left:
                        for r in right:
                            answer.append(calc(l, r, value))
                        
            # oprerator가 없다면 input을 그대로 내보냄
            
            return answer if answer else [int(expression)]
        
    
        return explore()
