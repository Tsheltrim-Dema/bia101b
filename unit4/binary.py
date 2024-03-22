# input array
arr = [3,4,5,6,7,8,9]
target = 9

low = 0
high = len(arr)-1

# loop
result = False
while low <= high:
    # divide
    mid = (low + high) // 2 # this is the middel index(not the value of the index)

    #print('mid:', mid)
   # print('low:', low)
   # print('high:', high)
    #print('-----')

    # compare the middle with the4 target
    if arr[mid] == target:
        print('found')
        result = True
        break

    # compare and discard the half
    if target > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1

if result == True:
    print('found')
else:
    print("not found")
    

