nums = [100,5,88,4,9,19,15]

                                                # [100,5,88,4,9,19,15]
                                                # [100,5,88][4,9,19,15]
                                                # [100][5,88][4,9][19,15]
                                                #       [5][88][4][9][19][15]

def merge_sort(alist):

    middle = len(alist) // 2
    # for this example, it goes from start to middle (middle no inclusive). so 7/2 =3.5 = 3. 0,1,2,3 = 100, 5, 88, 4
    # but left half only goes to 88
    left_half = alist[:middle]
    right_half = alist[middle:]
    # this constantly halves the lists

    if len(alist) > 2:
        merge_sort(left_half)
        merge_sort(right_half)

    left_point = right_point = main_point = 0

    while left_point < len(left_half) and right_point < len(right_half):
        if left_half[left_point] < right_half[right_point]:
            alist[main_point] = left_half[left_point]
            left_point += 1
        else:
            alist[main_point] = right_half[right_point]
            right_point += 1
        main_point += 1

# didn't make it to last element in left half
    while left_point < len(left_half):
        alist[main_point] = left_half[left_point]
        left_point += 1
        main_point += 1


# didn't make it to last element in right half
    while right_point < len(right_half):
        alist[main_point] = right_half[right_point]
        right_point += 1
        main_point += 1


merge_sort(nums)
print(nums)