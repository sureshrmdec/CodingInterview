class Solution:
    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        strobogram_dict = {'6':'9', '9':'6', '1':'1', '8':'8', '0':'0'}
        left = 0; right = len(num) - 1
        while left <= right:
            # strobogram_dict.get(num[left]) is None means that
            # we dont have any strobogrammatic number like above
            # and the second condition contains the checking for strobogram_dict.get(num[right]) is None
            if strobogram_dict.get(num[left]) is None or strobogram_dict[num[left]] != num[right]:
                return False
            left  += 1
            right -= 1
        return True

if __name__ == "__main__":
    s = Solution()
    print s.isStrobogrammatic("69")
    print s.isStrobogrammatic("96")
    print s.isStrobogrammatic("196")
    print s.isStrobogrammatic("222")
    print s.isStrobogrammatic("818")
    print s.isStrobogrammatic("88")




