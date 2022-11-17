class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l=[]
        k=celsius+ 273.15
        f= celsius*1.80+32.00
        l.append(k)
        l.append(f)
        return l