class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count,full,empty=numBottles,numBottles,numBottles
        while full:
            full=empty//numExchange
            count+=full
            empty=empty//numExchange+empty%numExchange
            
        return count