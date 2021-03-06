# Time:  O(n)
# Space: O(1)
#
# Given a sorted integer array where the range of elements are [lower, upper] inclusive,
# return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# return ["2", "4->49", "51->74", "76->99"].
#


class Solution1:
    # @param {integer[]} nums
    # @param {integer} lower
    # @param {integer} upper
    # @return {string[]}
    def findMissingRanges(self, nums, lower, upper):
        ranges = []
        # check if nums exists or not
        if nums:
           # make lower range
           if nums[0] > lower:
              nums.insert(0, lower - 1)
           # make upper range
           if nums[-1] < upper:
              nums.append(upper + 1)
        else:
           nums = [lower - 1, upper + 1]
        # check for the nums
        for i in xrange(1, len(nums)):
            # difference is just two, then can only insert one elem
            if nums[i] - nums[i - 1] == 2:
                 ranges.append(str(nums[i - 1] + 1))
            # more than two, then we need to use '... -> ...' to indicate the range
            elif nums[i] - nums[i - 1] > 2:
                 ranges.append('->'.join([str(nums[i - 1] + 1), str(nums[i] - 1)]))
        return ranges

class Solution: # simpler olution
    def findMissingRanges(self, A, lower, upper):
        ranges = []
        pre = lower - 1

        for i in xrange(len(A) + 1):
            if i == len(A):
                cur = upper + 1
            else:
                cur = A[i]

            if cur - pre >= 2:
                ranges.append(self.getRange(pre + 1, cur - 1))

            pre = cur

        return ranges

    def getRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)
if __name__ == '__main__':
   s = Solution()
   print s.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
   print s.findMissingRanges([1, 4, 75], 0, 99)
   print s.findMissingRanges([7, 9, 10, 23, 45, 78, 102], 1, 190)
   print s.findMissingRanges([-1000000000,-9999,0,1,2,10,100,1000,999999999,1000000000], -1000000000, 1000000000)
   print s.findMissingRanges([], 1, 1)



        