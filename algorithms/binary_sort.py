#basic implmentation of binary sort:
#essentially the same as insertion sort, however a binary search is used to find the correct index for insertion

def binary_sort(val, arr, start_i, end_i):   

    i = start_i + int((end_i-start_i)/2)
    print("start: " + str(start_i) + ", end: " + str(end_i) + ", i: " + str(i) + ", val: " + str(val) + ", into: " + str(arr[start_i:end_i]))
    

    if (end_i == start_i) or (i == start_i):
        if arr[i] < val:
            i += 1
        if end_i > start_i and arr[end_i] < val:
            i += 1 
        #if end_i != start_i and arr[i+1] < val:
        #    i += 1
    elif val > arr[i]:
        # recurse to right of val
        i = binary_sort(val, arr, i+1, end_i)
    elif val < arr[i]:
        # recurse to left of val
        i = binary_sort(val, arr, start_i, i-1)


    return(i)


    #if (end_i == start_i) or (end_i < start_i):
    #    if arr[i] < val:
    #        print("here")
    #        i += 1
    #elif val > arr[i]:
        #recurse to the right of i
    #    i = binary_sort(val, arr, i+1, end_i)
    #elif val < arr[i]:
        #recurse to the left of i
    #    i = binary_sort(val, arr, start_i, i-1)

    #return(i)

def insert(arr, insertion_index, val):
    new_arr = [0]*(len(arr)+1)
    
    
    #print(len(arr))
    print("inserting, " + str(val) + " @: " + str(insertion_index))


    #print("val: " + str(val))   
    #print("insertion_index: " + str(insertion_index))

    new_arr[0:insertion_index] = arr[0:insertion_index]
    new_arr[insertion_index] = val
    #if insertion_index != len(arr):
    new_arr[insertion_index+1:len(new_arr)] = arr[insertion_index:len(arr)]

    #print(arr[insertion_index:len(arr)])

    return(new_arr)

#arr = [1, 3, 4, 5, 6, 8, 9, 10, 11, 13]
#val = 7
#index = binary_sort(val, arr, 0, len(arr)-1)
#arr = insert(arr, index, val)
#val = 2
#index = binary_sort(val, arr, 0, len(arr)-1)
#arr = insert(arr, index, val)
#val = 12
#index = binary_sort(val, arr, 0, len(arr)-1)
#arr = insert(arr, index, val)

#print(arr)

#print(len(arr)-1)
#print(index)


def sort(obj, audioBuff):




    obj.clear()



    sorted = 1
    sorted_arr = obj.stripState[0:sorted]
    #print(sorted_arr)

    for i in range(1, len(obj.stripState)-1):
        audioBuff.append(obj.stripState[i][0])

        index = binary_sort(obj.stripState[i], obj.stripState, 0, sorted)


        print(index)

        #print("curr sorted: " + str(obj.stripState[0:sorted]))
        #print("index: " + str(index))
        sorted_arr = insert(sorted_arr, index, obj.stripState[i])
        print(sorted_arr)

        obj.stripState[0:len(sorted_arr)] = sorted_arr
    

        #temp sleep
        #import time
        #time.sleep(1)


        # JUST A LOOP TO SHOW WHEN SYSTEM ISN'T WORKING PROPERLY
        #prev = obj.stripState[0]
        #for n in range(1, sorted):
        #    if obj.stripState[n] < prev:
        #        print("")
        #        print("WARNING SORTED LIST IS NOT IN SRTICTLY DECREASING ORDER")
        #        print("")
        #    prev = obj.stripState[n]


        obj.update()


        #for n in reversed(range(0,sorted)):
        #    if obj.stripState[n] > obj.stripState[n+1]:
        #        audioBuff.append(obj.stripState[i][0])
        #
        #        mem = obj.stripState[n+1]
        #        obj.stripState[n+1] = [mem[0],255,mem[2],mem[3],mem[4]]                
        #        #obj.stripState[n+1] = [0,255,255,255,255]
        #        obj.update()
        #        obj.stripState[n+1] = obj.stripState[n]
        #        obj.stripState[n] = mem
        #        #obj.update()
        #    else:
        #        break
        #    #obj.update()
        sorted += 1
        #obj.update()