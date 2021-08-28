class Solution:
    def reformat(self, s: str) -> str:
        digit_list, char_list = [], []
        for c in s :
            if c.isdigit() :
                digit_list.append(c)
            else:
                char_list.append(c)

        if (len(digit_list) ==0 and len(char_list) !=1) or (len(digit_list) !=1 and len(char_list) ==0):
            return ""

        output = ""

        for k in range(min([len(digit_list), len(char_list)])):
            output += char_list.pop() + digit_list.pop()

        if len(digit_list)> len(char_list) : 
            return digit_list.pop() + output 
        elif len(digit_list) < len(char_list) :
            return output + char_list.pop()
        else: 
            return output
