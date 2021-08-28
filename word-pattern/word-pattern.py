class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        default_dict = collections.defaultdict(str)
        word_list = s.split(' ')
        for c, w in zip(pattern,word_list) :
            if default_dict[c] == '' and  w not in default_dict.values():
                default_dict[c] = w

        pattern_word = ''
        for c in pattern :
            pattern_word += default_dict[c] + ' '
        if pattern_word == s + ' ' :
            return True
        else :
            return False