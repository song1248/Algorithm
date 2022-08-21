class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        # 가장 뒤쪽에 있는 str의 idx를 저장
        d={}
        for i in range(len(s)):
            d[s[i]]=i

        stack=[]
        stack_set = set()

        for str_idx, cur_str in enumerate (s):
            if cur_str not in stack_set:
                
                # stack이 있고
                # stack의 마지막값이 현재 str보다 크고\
                # 뒤에 남아있으면
                # pop
                while stack and stack[-1]> cur_str and d[stack[-1]]>str_idx:

                    stack_set.remove(stack.pop())

                stack.append(cur_str)
                stack_set.add(cur_str)
                
        return "".join(stack)
