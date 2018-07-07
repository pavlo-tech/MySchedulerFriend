
class AvailableShift():
    def __init__(self, Day, StartTime, EndTime):
        self.Day = Day
        self.StartTime = StartTime
        self.EndTime = EndTime


class Worker():
    def __init__(self, Name, RequiredHours):
        self.Name = Name
        self.RequiredHours = RequiredHours
        self.AvailableShiftList = []

    def CanWork(startTime):
        for availableShift in self.AvailableShiftList:
            if availableShift.StartTime == startTime:
                return True
        return False
