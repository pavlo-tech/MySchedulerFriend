import datetime as dt

class TimeSlot():
    def __init__(self, StartTime):
        self.AvailableWorkers = []
        self.SelectedWorkers = []
        self.StartTime = StartTime
        self.EndTime = StartTime + dt.timedelta(0,0,0,0,15)

# must have > 7 timeslots
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

        # compensate if there is not enough time to meet MinShiftLength
        if (endIndex - startIndex) < (MinShiftLength * 4 - 1):
            startIndex = endIndex - MinShiftLength * 4 - 1
            TimeSlot = self.TimeSlots[startIndex]

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
