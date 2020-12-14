"""
@class:  CSC382
@author: Francesco Pecora
@date:   12/13/2020
"""

import random

class DeterministicMedian:

    def kthSmallest(self, arr, l, r, k): 
        '''
        main function that finds the kth smallest value
        list arr: list holding our values
        int l: integer holding left pointer (start of list)
        int r: integer holding right pointer (end of list)
        int k: integer holding kth position required
        '''
        if (k > 0 and k <= r - l + 1): # k less than num of elements in array
            pos = self.randomPartition(arr, l, r) 
            if (pos - l == k - 1): 
                return arr[pos] 
            if (pos - l > k - 1):
                return self.kthSmallest(arr, l, pos - 1, k) 
            return self.kthSmallest(arr, pos + 1, r, k - pos + l - 1) 
        return 99999999
    

    def swap(self, arr, a, b):
        '''
        function that swaps two elements of an array
        list arr: list of elements
        int a: first index to be swapped
        int b: second index to be swapped
        '''
        arr[a], arr[b] = arr[b], arr[a]
    

    def partition(self, arr, l, r):
        '''
        function that creates the partition of the array
        list arr: list holding our values
        int l: integer holding left pointer (start of partition)
        int r: integer holding right pointer (end of partition)
        '''
        x = arr[r] 
        i = l 
        for j in range(l, r): 
            if (arr[j] <= x): 
                self.swap(arr, i, j) 
                i += 1
        self.swap(arr, i, r) 
        return i
 

    def randomPartition(self, arr, l, r): 
        '''
        function finding random partition of array
        list arr: list holding our values
        int l: integer holding left pointer (start of list)
        int r: integer holding right pointer (end of list)
        '''
        n = r - l + 1
        pivot = int(random.random() % n) 
        self.swap(arr, l + pivot, r) 
        return self.partition(arr, l, r) 
        
