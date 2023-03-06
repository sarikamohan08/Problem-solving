class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        right, left = n-1, 0
        while(left <= right):
            mid = left + (right - left) // 2
            if(arr[mid] - (mid + 1) < k):
                left = mid + 1
            else:
                right = mid -1
        return left + k