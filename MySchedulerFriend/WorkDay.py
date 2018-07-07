import datetime as dt

class TimeSlot():
    def __init__(self, StartTime):
        self.AvailableWorkers = []
        self.SelectedWorkers = []
        self.StartTime = StartTime
        self.EndTime = StartTime + dt.timedelta(0,0,0,0,15)


class WorkDay():
    def __init__(self, Day, StartTime, EndTime):
        self.Day = Day
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.TimeSlots = []
        self.Favorability = 0

    def BestManForTheJob(TimeSlot, MinShiftLength):

        startIndex = self.TimeSlots.index(TimeSlot)
        endIndex = len(self.TimeSlots)

        TimeSlot.AvailableWorkers.sort(key=lambda worker: worker.RequiredHours, reverse = true)

        for worker in TimeSlot.AvailableWorkers:
            ShiftLen = 0

            index = startIndex
            while index < endIndex:

                if worker in self.TimeSlots[index].AvailableWorkers:
                    index +=1
                    ShiftLen += 0.25

                    if ShiftLen == MinShiftLength:
                        return worker
                else
                    index = endIndex
            return None
