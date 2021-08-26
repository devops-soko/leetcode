class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_list = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        output =[]
        for i in range(len(words)):
            row = None
            if words[i][0].lower() in keyboard_list[0]:
                row = 0
            elif words[i][0].lower() in keyboard_list[1]:
                row = 1
            else :
                row = 2


            for j in range(len(words[i])) :
                if words[i][j].lower() not in keyboard_list[row] :
                    break
                if j == len(words[i])-1 :
                    output.append(words[i])

        return output