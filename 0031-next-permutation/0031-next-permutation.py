class Solution:
    def nextPermutation(self,  arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bPoint, n = -1, len(arr)
        for i in range(n-2,-1,-1):
            if arr[i] >= arr[i+1]: continue                   # Skip the non-increasing sequence
            bPoint = i                                        # Got our breakpoint
            for j in range(n-1,i,-1):                         # again traverse from end
                if arr[j] > arr[bPoint]:                      # Search an element greater the element present at the breakPoint.
                    arr[j], arr[bPoint] = arr[bPoint], arr[j] # Swap it
                    break                                     # We just need to swap once
            break                                             # Break this loop too
        arr[bPoint+1:] = reversed(arr[bPoint+1:])        