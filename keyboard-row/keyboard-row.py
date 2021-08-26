class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_dic = {}
        for c in 'qwertyuiop' :
            keyboard_dic[c] = 1

        for c in 'asdfghjkl' :
            keyboard_dic[c] = 2

        for c in 'zxcvbnm' :
            keyboard_dic[c] = 3

        l = []
        for word in words:
            for i in range(len(word)-1):
                if keyboard_dic[word[i].lower()] != keyboard_dic[word[i+1].lower()] :
                    l.append(word)
                    break

        for word in l :
            words.remove(word)

        return words