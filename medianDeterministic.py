import random

'''
def kthSmallest(self, arr, l, r, k):  
        
        # If k is smaller than number of  
        # elements in array  
        if (k > 0 and k <= r - l + 1):  
            
            # Number of elements in arr[l..r]  
            n = r - l + 1
    
            # Divide arr[] in groups of size 5,  
            # calculate median of every group 
            # and store it in median[] array.  
            median = [] 
    
            i = 0
            while (i < n // 5): 
                median.append(self.findMedian(arr, l + i * 5, 5)) 
                i += 1
    
            # For last group with less than 5 elements  
            if (i * 5 < n): 
                median.append(self.findMedian(arr, l + i * 5,  
                                                n % 5)) 
                i += 1
    
            # Find median of all medians using recursive call.  
            # If median[] has only one element, then no need  
            # of recursive call 
            if i == 1: 
                medOfMed = median[i - 1] 
            else: 
                medOfMed = self.kthSmallest(median, 0,  
                                    i - 1, i // 2) 
    
            # Partition the array around a medOfMed 
            # element and get position of pivot  
            # element in sorted array  
            pos = self.partition(arr, l, r, medOfMed) 
    
            # If position is same as k  
            if (pos - l == k - 1):  
                return arr[pos]  
            if (pos - l > k - 1): # If position is more,  
                                # recur for left subarray  
                return self.kthSmallest(arr, l, pos - 1, k)  
    
            # Else recur for right subarray  
            return self.kthSmallest(arr, pos + 1, r, k - pos + l - 1)  
    
        # If k is more than the number of  
        # elements in the array
        return 9999999
    
    def swap(self, arr, a, b):  
        temp = arr[a]  
        arr[a] = arr[b]  
        arr[b] = temp  
    
    # It searches for x in arr[l..r],   
    # and partitions the array around x.  
    def partition(self, arr, l, r, x): 
        for i in range(l, r): 
            if arr[i] == x: 
                self.swap(arr, r, i) 
                break
    
        x = arr[r]  
        i = l  
        for j in range(l, r):  
            if (arr[j] <= x):  
                self.swap(arr, i, j)  
                i += 1
        self.swap(arr, i, r)  
        return i  
    
    # A simple function to find  
    # median of arr[] from index l to l+n 
    def findMedian(self, arr, l, n): 
        lis = [] 
        for i in range(l, l + n): 
            lis.append(arr[i]) 
            
        # Sort the array  
        lis.sort() 
    
        # Return the middle element 
        return lis[n // 2]

'''

class DeterministicMedian:
    def quickselect_median(self, l, pivot_fn=random.choice):
        if len(l) % 2 == 1:
            return self.quickselect(l, len(l) // 2, pivot_fn)
        else:
            return 0.5 * (self.quickselect(l, len(l) // 2 - 1, pivot_fn) +
                        self.quickselect(l, len(l) // 2, pivot_fn))


    def quickselect(self, l, k, pivot_fn):
        
        if len(l) == 1:
            assert k == 0
            return l[0]

        pivot = pivot_fn(l)

        lows = [el for el in l if el < pivot]
        highs = [el for el in l if el > pivot]
        pivots = [el for el in l if el == pivot]

        if k < len(lows):
            return self.quickselect(lows, k, pivot_fn)
        elif k < len(lows) + len(pivots):
            # We got lucky and guessed the median
            return pivots[0]
        else:
            return self.quickselect(highs, k - len(lows) - len(pivots), pivot_fn)
        
        
