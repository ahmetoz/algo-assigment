"""

Bilmuh 543 => Assigment 3 - Problem 1
----------------------------------------
Interval scheduling algorithm implementation. (unweighted version)
sorting is O(n log n) , selection is linear O(n)
whole operation is dominated by O(n log n)
Runtime complexity:  O(n log n)

Note: Datetime format (tr-TR) dd//MM/yyyy aka "%d/%m/%Y" ex: 01/01/2016

Ahmet Oz
91140000121

"""


class Interval(object):
    def __init__(self, job_id, start_time, finish_time):
        self.job_id = job_id
        self.start_time = start_time
        self.finish_time = finish_time


def schedule(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x.finish_time)
    scheduled_intervals = []
    tmp_finish_time = 0

    for interval in sorted_intervals:
        if tmp_finish_time <= interval.start_time:
            tmp_finish_time = interval.finish_time
            scheduled_intervals.append(interval)

    return scheduled_intervals