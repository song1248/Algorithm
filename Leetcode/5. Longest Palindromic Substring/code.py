class Solution(object):
    def longestPalindrome(self, s):
        answer = s[0]
        def case_a(i, n, palindrome):
            if i+n == len(s) or i+1-n == -1:
                return palindrome
            if ord(s[i+1-n]) - ord(s[i+n]) == 0:
                palindrome = s[i+1-n] + palindrome + s[i+n]
                return case_a(i, n+1, palindrome)
            return palindrome
        
        def case_b(i, n, palindrome):
            if i+n == len(s) or i-n == -1:
                return palindrome
            if ord(s[i-n]) - ord(s[i+n]) == 0:
                palindrome = s[i-n] + palindrome + s[i+n]
                return case_b(i, n+1, palindrome)
            return palindrome            
        
        
        # "aa" 혹은 "aba"형태가 나오면 검사
        # -> 마지막 전 인덱스 까지 검사
        
        for i in range(len(s)-1):
            n = 1

            palindrome_a = case_a(i, n, "")
            palindrome_b = case_b(i, n, s[i])
        
            if len(answer) != max(len(answer), len(palindrome_a)):
                answer = palindrome_a
            if len(answer) != max(len(answer), len(palindrome_b)):
                answer = palindrome_b
                
        return answer
