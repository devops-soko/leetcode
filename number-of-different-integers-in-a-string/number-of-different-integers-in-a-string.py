class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        flag = False
        nums =[]
        num=''
        for i,c in enumerate(word):
            if flag == False and c.isdigit():
                flag = True
                num += c
            elif flag == True and c.isdigit():
                num += c
            elif flag == True and c.isalpha() :
                nums.append(int(num))
                num=''
                flag = False

            if flag == True and len(word)-1 ==i :
                nums.append(int(num))

        return len(set(nums))