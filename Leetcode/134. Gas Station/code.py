class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost): 
            return -1
        
        answer = 0
        cur_gas = 0
        
        gas.append(0)
        cost.append(cost[0])
        
        for i in range(len(gas)-1):
            
            # gas 얻기
            cur_gas += gas[i] - cost[i]
            
            if cur_gas < 0:
                cur_gas = 0
                answer = i + 1
 
        return answer
            
