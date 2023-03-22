class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pairs = []
        ll = len(arr)
        for i in range(ll):
            for j in range(ll):
                if(i==j):
                    continue
                pairs.append([arr[i],arr[j]])
        
        return sorted(pairs, key=lambda x: x[0]/x[1])[k-1]