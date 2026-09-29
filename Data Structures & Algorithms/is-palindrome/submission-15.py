class Solution:
    def isPalindrome(self, s: str) -> bool:
        lR = 0
        rR = len(s) - 1

        while lR < rR:
            while lR < len(s) and not s[lR].isalnum():
                lR += 1
            while rR >= 0 and not s[rR].isalnum():
                rR -= 1

            if lR >= rR:
                break
                  
            if s[lR].lower() != s[rR].lower():
                return False

            lR += 1
            rR -= 1
            
        return True