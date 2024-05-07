class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0
        for c in s:
            if c=="[":
                stack.append(current_string)
                stack.append(current_num)
                current_string = ""
                current_num = 0
            elif c=="]":
                num = stack.pop()
                stacked_str = stack.pop()
                current_string = stacked_str + num*current_string
            elif c.isdigit():
                current_num = current_num*10 + int(c)
            else:
                current_string+=c
        return current_string