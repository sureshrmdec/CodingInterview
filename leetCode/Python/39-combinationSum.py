#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution1(object):
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    # 一個自己在寫的時候也會犯的錯誤，到底何謂 back tracking ? 為什麼這算是 back tracking 呢？這提供了很好的解釋！
    # 您好！这道题目我在用递归的时候，如果将这句代码：self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
    # 改为：valuelist.append(candidates[i]); self.DFS(candidates, target - candidates[i], i, valuelist) 
    # 就会出现了timeout 的error。不知道原因是什么？在用append的时候消耗的时间会更大吗？谢谢！
    # 不是的。如果使用append的话，valuelist的值就改变了，而dfs是要回溯的，所以不能改变valuelist的值，
    # 但要传递的参数是valuelist+[candidates[i]]，相当于a += 1和a+1的区别，
    # 一个a的值改变了，一个没有改变。

    def __init__(self):
        self.res    = []
        self.length = 0

    def combinationSum(self, candidates, target):
        self.length = len(candidates)
        candidates.sort()
        self.DFS(target, candidates, [], 0)
        return self.res

    def DFS(self, diff, candidates, comb, start):
        if not diff: # diff == 0
           self.res.append(list(comb)) # version 2: since we use the address(generator) of list directly, change it to list now
           return self.res
        else:
           for i in xrange(start, self.length):
               if candidates[i] > diff:
                  break # or you can write 'return', both end the function and ship to next recursion
               else:
                  comb.append(candidates[i]) # version 2: use append to record the list, but it change the list directly, need to pop out the thing later, after close the recursion
                  self.DFS(diff - candidates[i], candidates, comb, i)
                  comb.pop() # version 2: recover the value of comb now, backtracking

# P.S. version 1 & 2 速度差不多，推測是因為 version 2 雖然用了 append ，但在結束之後還是得用上 pop 來恢復
class Solution(object):
    def __init__(self):
        self.res = []
        self.target = 0
        self.length = 0

    def combinationSum(self, candidates, target):
        self.res = []
        if candidates:
            self.target = target
            self.length = len(candidates)
            # notice! must be sorted, otherwise hard to see the replicate
            candidates.sort()
            self.comb_sum_helper(candidates, [], 0, 0)
        return self.res

    def comb_sum_helper(self, candidates, comb, curr_sum, start):
        if curr_sum == self.target:
            self.res.append(comb)
            return
        for i in xrange(start, self.length):
            if self.target - curr_sum < candidates[i]:
            # this condition must exist, we use it to
            # escape the infinite looping condition
                break
            self.comb_sum_helper(candidates, comb + [candidates[i]], curr_sum + candidates[i], i)

if __name__ == '__main__':
   s = Solution()
   candidates = [3,6,7,2]
   target     = 7
   print s.combinationSum(candidates, target)