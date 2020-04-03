Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


# DFS

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keypad = {'2':['a','b','c'],'3':['d','e','f'],
                   '4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
                   '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans = []
        temp = ""
        self.dfs(keypad, digits, ans, temp, 0, 0)
        return ans
        
        
    def dfs(self, keypad, digits, ans, temp,l, index):
        
        if l == len(digits):
            ans.append(temp)
            return
    
        for item in keypad[digits[index]]:
            self.dfs(keypad, digits, ans, temp + item, l + 1, index + 1)
            
 #Only for loop
 
 class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keypad = {'2':['a','b','c'],'3':['d','e','f'],
                   '4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
                   '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans = [""]
        
        for item in digits:
            temp = []
            
            for ch in keypad[item]:
                for item in ans:
                    temp.append(item + ch)
            ans = temp
        
        return ans

