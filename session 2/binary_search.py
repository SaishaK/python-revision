lst = [2, 5, 6, 9, 11]
element = 2

low = 0
high = len(lst) - 1

while (low <= high):
    mid = (low + high)//2
    if element > lst[mid]:
        low = mid + 1
    elif element < lst[mid]:
        high = mid - 1
    else:
        print(mid)
        break