import sys
import json
import datetime

import Worker as w
import WorkDay as wd

MinShiftLength = 2
'''
Employees must work 15-20 hr weeks

'''


'''
Read json file
'''
with open("TestInput.json", 'r') as f:
    datastore = json.load(f)

'''
Get Work Days
'''
WorkDays = []

for day in datastore["WorkDays"]:
    WorkDays.append(wd.WorkDay(day["Day"], day["StartTime"], day["EndTime"]))


'''
Get Workers
'''
Workers = []

for worker in datastore["Workers"]:
    newWorker = w.Worker(worker["Name"], worker["Hours"])

    for day in worker["Availablity"]:
        newDay = w.AvailableDay(day["Day"], day["StartTime"], day["EndTime"])
        newWorker.AvailableDayList.append(newDay)

    Workers.append(newWorker)


'''
Assign workers to days
'''
# Add workers to TimeSlots based on availibility
for worker in Workers:

    for workDay in WorkDays:

        for timeSlot in workDay.TimeSlots:

            if worker.CanWork(timeSlot.StartTime):
                workDay.Favorability += 1
                timeSlot.AvailableWorkers.append(worker)

# Sort days by ascending favorability
WorkDays.sort(key=lambda day: day.Favorability)

# assign shifts
for workDay in WorkDays:
    # select available worker with most required work Hours
    BestWorker = workDay.BestManForTheJob(workDay.TimeSlots[i], MinShiftLength)

    if BestWorker != None:
        endIndex = len(workDay.TimeSlots)

        i = 0
        while i < endIndex and BestWorker in workDay.TimeSlots[i].AvailableWorkers:
            workDay.TimeSlots[i].AvailableWorkers.remove(BestWorker)
            workDay.TimeSlots[i].SelectedWorkers.append(BestWorker)
            BestWorker.RequiredHours -= 0.25
            i += 1
