class MyCalendar:

    def __init__(self):
        self.calendar=[]

    def book(self, start: int, end: int) -> bool:
        for laststart,lastend in self.calendar:
            if laststart < end and start < lastend: # means there is overlapping
                print(laststart,lastend)
                return False # so we can return False
        self.calendar.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)