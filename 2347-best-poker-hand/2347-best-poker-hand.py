class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank = set(ranks)
        l = []
        suit = set(suits)
        m = []
        
        for i in rank:
            l.append(ranks.count(i))
            
        for j in suit:
            m.append(suits.count(j))
            
        if(5 in m):
            return "Flush"
        
        if(3 in l or 4 in l):
            return "Three of a Kind"
        
        if(2 in l):
            return "Pair"
        
        if(len(l)==sum(l) or len(m)==sum(m)):
            
            return "High Card"