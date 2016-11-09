import random

"""

Bilmuh 543 => Assigment 3 - Problem 2
----------------------------------------
The counting inversion algorithm

The difference from merge sort algorithm is that we want to do something extra:
 not only should we produce a single sorted list from A and B,
  but we should also count the number of "inverted pairs"

The SortAndCount algorithm correctly sorts the input list and counts the number of inversions;
It runs in O(n log n) time for a list with n elements

MergeAndCount algorithm takes O(n) time

Ahmet Oz
91140000121

"""


def SortAndCount(L):
    # if list L has one element
    l = len(L)
    if l <= 1 or L is None:
        return 0, L

    # Divide the list two halves A and B
    m = l // 2
    A = L[:m]
    B = L[m:]

    # Find inversions and return sorted list L
    ra, A = SortAndCount(A)
    rb, B = SortAndCount(B)
    r, L = MergeAndCount(A, B)

    return r, L


def MergeAndCount(A, B):
    count = 0
    M = []

    # while both list A and B not empty
    while A and B:
        if A[0] <= B[0]:
            M.append(A.pop(0))
        else:
            # if B[0] = current pointer is smaller than A[0]
            count += len(A)
            M.append(B.pop(0))

    # merged list M
    M += A + B

    # return inversion count and merged list
    return count, M

if __name__ == '__main__':
    n = 10
    my_randoms = random.sample(xrange(1, 101), n)

    print '\nList before: '
    print my_randoms

    inversion_count, sorted_list = SortAndCount(my_randoms)

    print '\nNumber of inversions: ', inversion_count
    print '\nSorted List: '
    print sorted_list



