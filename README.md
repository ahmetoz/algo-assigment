# Problem 1 :
Interval scheduling algorithm implementation. (unweighted version)
sorting is O(n log n) , selection is linear O(n)
whole operation is dominated by O(n log n)
Runtime complexity:  O(n log n)

run command with command line or python console: 

cd problem1
python analyze.py


sample input size is 10 you could change n from test code.*:
 
n = 100
intervals = randomIntervals(n)
...


#### Sample Input from problem1:
Job_ID	Start_Time	Finish_Time
Job1	28/10/2016 13:11	31/10/2016 22:07
Job2	09/10/2016 12:03	29/10/2016 19:24
Job3	13/10/2016 08:14	30/10/2016 05:34
Job4	16/10/2016 00:34	29/10/2016 13:59
Job5	02/10/2016 03:02	28/10/2016 02:48
Job6	03/09/2016 02:12	06/10/2016 01:33
Job7	25/09/2016 05:30	04/10/2016 19:34
Job8	28/10/2016 10:41	29/10/2016 06:00
Job9	13/10/2016 08:33	14/10/2016 12:07
Job10	23/09/2016 19:01	14/10/2016 08:29


#### Sample Output from problem2: (optimised schedule)
Job_ID	Start_Time	Finish_Time
Job7	25/09/2016 05:30	04/10/2016 19:34
Job9	13/10/2016 08:33	14/10/2016 12:07
Job8	28/10/2016 10:41	29/10/2016 06:00

------------------------------------------------------------------------
#Problem 2:

###The counting inversion algorithm

The difference from merge sort algorithm is that we want to do something extra:
 not only should we produce a single sorted list from A and B,
  but we should also count the number of "inverted pairs"

The SortAndCount algorithm correctly sorts the input list and counts the number of inversions;
It runs in O(n log n) time for a list with n elements

MergeAndCount algorithm takes O(n) time


------------------------------------------------------------------------
run command with command line or python console: 

cd problem2
python inversion.py


sample input size is 10 default you could change n from test code.*:
 

List before: 
[83, 6, 93, 72, 25, 71, 54, 49, 4, 17]

Number of inversions:  18

Sorted List: 
[4, 6, 17, 25, 49, 54, 71, 72, 83, 93]
