from itertools import permutations

def solution(expression):
    
    operater_set = set(['-','*','+'])
    
    split_expression = []
    start = 0
    for i in range(len(expression)):
        if expression[i] in operater_set:
            split_expression.append(expression[start:i])
            split_expression.append(expression[i])
            start = i + 1
    split_expression.append(expression[start:])
    
    order = ['-','*','+']
    def explore(split_expression, order):
        for operator in order:
            i = 0
            while i < len(split_expression) :
                if split_expression[i] == operator:
                    num1 = int(split_expression[i-1])
                    num2 = int(split_expression[i+1])
                    new_num = 0
                    if operator == "+":
                        new_num = num1 + num2
                    elif operator == "-":
                        new_num = num1 - num2
                    else:
                        new_num = num1 * num2
                        
                    split_expression = split_expression[:i-1] + [new_num] + split_expression[i+2:]
                
                    i -= 1
                i += 1
        return int(abs(split_expression[0]))

    max_val = 0    
    for tmp_order in permutations(order, 3):
        max_val = max(explore(split_expression, tmp_order), max_val)           


    return max_val
