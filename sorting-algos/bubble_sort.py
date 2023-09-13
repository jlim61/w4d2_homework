# [100,5,88,4,9,19,15]
# start at beginning of list, then compare ONLY two numbers. that's the bubble.
# [100,5,88,4,9,19,15]
# [100, 5] -> [5, 100]
# [5, 100, 88] -> [5, 88, 100] 
# [5, 88, 100, 4] -> [5,88,4,100] -> it checks one number all the way through to the end

# [100,5,88,4,9,19,15] -> start
# [5,88,4,9,19,15,100] -> first run through
# [5,4,9,19,15,88,100] -> second run through
# [4,5,9,15,19,88,100] -> third run through




nums = [100,5,88,4,9,19,15]

def bubble_sort(alist):
    unsorted = True
    passes = 1
    while unsorted:
        unsorted = False
        for i in range(len(alist) - passes):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                unsorted = True
        passes += 1
        print(alist)

bubble_sort(nums)
print(nums)