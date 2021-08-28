class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        default_dict = collections.defaultdict(str)
        word_list = s.split(' ')
        if len(set(pattern)) != len(set(word_list)) or len(pattern) != len(word_list):
            return False

        for i in range(len(pattern)) :
            if default_dict[pattern[i]] == '' and  word_list[i]:
                default_dict[pattern[i]] = word_list[i]

            if default_dict[pattern[i]] != word_list[i] : 
                return False

        return True
