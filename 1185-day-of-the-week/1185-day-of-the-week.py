class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
        if (month < 3) :
            year = year - 1
          
        r =  (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7
        if r == 1:
            return 'Monday'
        elif r == 2:
            return 'Tuesday'
        elif r == 3:
            return 'Wednesday'
        elif r == 4:
            return 'Thursday'
        elif r == 5:
            return 'Friday'
        elif r == 6:
            return 'Saturday'
        return 'Sunday'