class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        operator = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            if char in "+-*/" or i == len(s) - 1:
                if char == ' ' and i != len(s) - 1:
                    continue
                
                if operator == '+':
                    stack.append(curr_num)
                elif operator == '-':
                    stack.append(-curr_num)
                elif operator == '*':
                    stack.append(stack.pop() * curr_num)
                elif operator == '/':
                    stack.append(int(stack.pop() / curr_num))
                
                operator = char
                curr_num = 0
                
        return sum(stack)