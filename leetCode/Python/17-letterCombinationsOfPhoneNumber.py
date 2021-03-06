# Time:  O(n * 4^n)
# Space: O(n)
#
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#

class Solution1(object): # iterative
    def __init__(self):
        self.digit_letter_dict = \
                                {
                                '0':[""],
                                '1':[""],
                                '2':['a', 'b', 'c'],
                                '3':['d', 'e', 'f'],
                                '4':['g', 'h', 'i'],
                                '5':['j', 'k', 'l'],
                                '6':['m', 'n', 'o'],
                                '7':['p', 'q', 'r', 's'],
                                '8':['t', 'u', 'v'],
                                '9':['w', 'x', 'y', 'z']
                                }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_combs = []
        for digit in digits:
            letter_combs = self.merge_letter_combs(self.digit_letter_dict[digit], letter_combs)
        return letter_combs

    def merge_letter_combs(self, letters, letter_combs):
        if not letter_combs:
            return letters
        comb_list = []
        for letter in letters:
            comb_list.extend(letter_comb + letter for letter_comb in letter_combs)
        return comb_list

class Solution(object):
    def __init__(self):
        self.digit_letter_dict = \
                                {
                                '0':[""],
                                '1':[""],
                                '2':['a', 'b', 'c'],
                                '3':['d', 'e', 'f'],
                                '4':['g', 'h', 'i'],
                                '5':['j', 'k', 'l'],
                                '6':['m', 'n', 'o'],
                                '7':['p', 'q', 'r', 's'],
                                '8':['t', 'u', 'v'],
                                '9':['w', 'x', 'y', 'z']
                                }
        self.res = []
        self.length = 0

    def letterCombinations(self, digits):
        if self.res:
            self.res = []
        self.length = len(digits)
        if self.length:
            self.letter_comb_helper(digits, 0, "")
        return self.res

    def letter_comb_helper(self, digits, start, comb):
        if len(comb) == self.length:
            self.res.append(comb)
            return
        for letter in self.digit_letter_dict[digits[start]]:
            self.letter_comb_helper(digits, start + 1, comb + letter)


if __name__ == "__main__":
    import time
    start = time.clock()
    s = Solution()
    result = s.letterCombinations("")
    print result
    print "%s sec" % (time.clock() - start)
    print "length:", len(result)
