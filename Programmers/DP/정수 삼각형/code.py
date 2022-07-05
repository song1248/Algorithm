# 정수 삼각형

시간초과 코드

```python
def solution(triangle):
    
    answer = 0
    def explore(i=0,layer=0,sum=0):
        nonlocal answer
        if layer >= len(triangle):
            answer = max(answer, sum)
            return
            
        sum += triangle[layer][i]
        
        explore(i+1, layer+1,sum)
        explore(i, layer+1,sum)
        
    explore()
    return answer
```

위에서부터 탐색

- 중복되는 연산을 계속하여 시간복잡도 증가
- → 중복되는 연산을 줄이기 위해 dp 사용

```python
def solution(triangle):

    # 아래쪽부터 탐색
    def explore(layer=-1):
        nonlocal triangle
        
        if abs(layer) == len(triangle):
            return 
        
        for i in range(len(triangle[layer-1])):
            triangle[layer-1][i] += max(triangle[layer][i],triangle[layer][i+1])
    
        explore(layer-1)
        
    explore()
    
    return triangle[0][0]
```

triangle을 memorize로 이용하여 중복계산을 줄임
