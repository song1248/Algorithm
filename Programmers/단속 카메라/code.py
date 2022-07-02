def solution(routes):
    routes = sorted(routes)
#     print(routes)
    answer = 0
    camera = -30001
    for start, end in routes:
#         print(camera,235324)
        if start > camera:
            answer += 1
            camera = end
        else:
            camera = min(end,camera)
        
            
    return answer
