def solution(brown, yellow):
    
    width_height =  int((brown - 4 ) / 2)
    for width in range(1,width_height):
        width = width
        height = width_height-width
        if width*height == yellow:
            answer = [height+2, width+2]
            break
    
    
    return answer
