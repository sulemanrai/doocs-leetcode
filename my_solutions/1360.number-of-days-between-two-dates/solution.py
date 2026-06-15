class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeapYear(year: int) -> bool:
            # TODO: implement
            pass
        def daysInMonth(year: int, month: int) -> int:
            # TODO: implement
            pass
        def calcDays(date: str) -> int:
            # TODO: implement
            pass
        return abs(calcDays(date1) - calcDays(date2))
