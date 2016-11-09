import random
import time
from schedule import Interval, schedule

date_format = '%d/%m/%Y %H:%M'


def strTimeProp(start, end, prop):
    """Get a time at a proportion of a range of two formatted times."""

    stime = time.mktime(time.strptime(start, date_format))
    etime = time.mktime(time.strptime(end, date_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(date_format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, prop)


def getTimeFromStr(date_str):
    return time.strptime(date_str, date_format)


def getStrFromTime(date):
    return time.strftime(date_format, date)


def createInputFile(n):
    with open('input.txt', 'w') as input_file:
        input_file.write("Job_ID\tStart_Time\tFinish_Time\n")
        for i in range(1, n + 1):
            start = randomDate("1/9/2016 0:0", "1/11/2016 0:0", random.random())
            finish = randomDate(start, "1/11/2016 0:0", random.random())
            input_file.write("Job%s\t%s\t%s\n" % (str(i), start, finish))


def randomIntervals(n):
    createInputFile(n)
    intervals = []
    with open("input.txt", "r") as input_file:
        next(input_file)
        for line in input_file:
            job_id, start, finish = line.rstrip().split("\t")
            intervals.append(Interval(job_id, getTimeFromStr(start), getTimeFromStr(finish)))
    return intervals


if __name__ == '__main__':
    n = 10
    intervals = randomIntervals(n)
    scheduled_intervals = schedule(intervals)

    with open('output.txt', 'w+') as output_file:
        output_file.write("Job_ID\tStart_Time\tFinish_Time\n")
        for i in scheduled_intervals:
            output_file.write("%s\t%s\t%s\n" % (i.job_id, getStrFromTime(i.start_time), getStrFromTime(i.finish_time)))

