#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time:  O(n)
# Space: O(1)
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
#

class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    # 下面这种算法据说是STL中的经典算法。在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
    # 然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，然后将partition后的元素（不包括partition指向的元素）
    # 逆序排列。比如14532，那么升序对为45，partition指向4，由于partition之后除了5没有比4大的数，所以45交换为54，即15432，
    # 然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。确实很巧妙。
    def nextPermutation(self, num):
        length = len(num); end = length - 1; partition = -1
        # find the biggest number which is bigger the partition number
        for i in xrange(end, 0, -1):
            if num[i] > num[i - 1]:
               partition = i - 1
               break
        # if there is no such thing, which mean the biggest number is already
        # in the front, no next biggest number, we reverse the list directly
        # as the question wisj
        if partition == -1:
           self.reverse(num, 0, end)
           return
        # from the end of the list, try to find the bigger number than partition & swap with it.
        # which can make sure the number we are going to build is the next 'biggest' number
        for i in xrange(end, partition, -1):
            if num[i] > num[partition]:
               self.swap_in_list(num, i, partition)
               break
        # finally, reverse the partition after part index, make sure the part can be the smallest
        self.reverse(num, partition + 1, end)

    def reverse(self, lst, start, end):
        while end >= start:
              self.swap_in_list(lst, start, end)
              end   -= 1
              start += 1

    def swap_in_list(self, lst, idx1, idx2):
        tmp       = lst[idx1]
        lst[idx1] = lst[idx2]
        lst[idx2] = tmp


if __name__ == '__main__':
   s = Solution()
   test_lst = [3,2,1]
   # test_lst = [1, 4, 5, 3, 2]
   # print s.reverse(test_lst, 2, 4)
   s.nextPermutation(test_lst)
   print test_lst