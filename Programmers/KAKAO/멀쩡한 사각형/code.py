import math

def solution(w,h):
    def GCD(x,y):
        while(y):
            x,y = y,x%y
        return x
    
    gcd = GCD(w,h)

    tmp_x = w // gcd
    tmp_y = h // gcd
    
    
    values = []
    answer = 0
    
    if tmp_x >= tmp_y:
        tmp_x, tmp_y = tmp_y, tmp_x
        
    for x in range(tmp_x):
        t1 = x*tmp_y/tmp_x
        t2 = (x+1)*tmp_y/tmp_x
        answer += math.ceil(t2) - math.floor(t1)
        
    return w*h - answer*gcd
