class Solution:
    def reformat(self, s: str) -> str:
        digit_list, char_list = [], []
        for c in s :

            if c.isdigit() :
                digit_list.append(c)
            else:
                char_list.append(c)

        if (len(digit_list) ==0 and len(char_list) !=1) or (len(digit_list) !=1 and len(char_list) ==0) or abs(len(digit_list)-len(char_list)) > 1 :
            return ""

        output = ""
        i,j =0,0
        if len(digit_list) <= len(char_list) :
            for k in range(len(s)):
                if(k%2 ==0) :
                    output += char_list[j]
                    j+=1
                else :
                    output += digit_list[i]
                    i+=1


        else :
            for k in range(len(s)):
                if(k%2 ==0) :
                    output += digit_list[i]
                    i+=1
                else :
                    output += char_list[j]
                    j+=1

        return output