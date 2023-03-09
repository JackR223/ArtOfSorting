import time

#basic implmentation of binary sort:
#essentially the same as insertion sort, however a binary search is used to find the correct index for insertion

def binary_search(val, obj, start_i, end_i, default_b):

    compareSD = obj.compareSD

    # highlight current section of arr
    # can switch between stacking and non-stacking brightness change by enabling / unenabling the flag
    obj.highlight(start_i, end_i, default_b, stack=True)
    
    #for i in range(0, 10):
    #    obj.update()

    arr = obj.stripState

    i = start_i + int((end_i-start_i)/2)
    #print("start: " + str(start_i) + ", end: " + str(end_i) + ", i: " + str(i) + ", val: " + str(val) + ", into: " + str(arr[start_i:end_i])) 

    if (end_i == start_i) or (i == start_i):
    #if obj.evaluate(end_i, start_i)[1] or obj.evaluate(i, start_i)[1]:
        time.sleep(compareSD)
        if arr[i] < val:
        #if obj.evaluate(arr[i], val)[0]:
            time.sleep(compareSD)
            i += 1
        if end_i > start_i and arr[end_i] < val:
        #if obj.evaluate(end_i, start_i)[2] and obj.evaluate(arr[end_i], val)[0]:
            time.sleep(compareSD)
            i += 1
    elif val > arr[i]:
    #elif obj.evaluate(val, arr[i])[2]:
        time.sleep(compareSD)
        # recurse to right of val
        i = binary_search(val, obj, i+1, end_i, default_b)
    elif val < arr[i]:
    #elif obj.evaluate(val, arr[i])[0]:
        time.sleep(compareSD)
        # recurse to left of val
        i = binary_search(val, obj, start_i, i-1, default_b)

    return(i)



def sort(obj, audioBuff):

    swapSD = obj.swapSD

    sorted = 1

    default_b = obj.stripState[0][1]

    for i in range(1, len(obj.stripState)-1):

        val = obj.stripState[i].copy()
        audioBuff.append(val[0])

        # highlight pixel to be inserted
        obj.stripState[i][1] += 5
        obj.update()

        index = binary_search(val, obj, 0, sorted, default_b) # perform binary search to find where to insert item
        #sorted_arr = insert(sorted_arr, index, val) # insert item into sorted arr at given index (need to shift anything to the right of including the index, right by one)

        obj.highlight(0,0,default_b)

        time.sleep(swapSD*(sorted-index))

        obj.stripState[index:(sorted+1)] = [val] + obj.stripState[index:sorted]
        obj.update()

        # possible way of inserting -> keeps execution time in line with other algorithms but doesn't look the best
        #prev = obj.stripState[index]
        #obj.stripState[index] = val
        #for n in range(index+1, sorted+1):
        #    obj.stripState[n], prev = prev, obj.stripState[n]
        #    obj.update()

        sorted += 1