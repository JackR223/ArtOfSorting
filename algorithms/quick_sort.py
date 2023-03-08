# basic implmentation of quick sort
# could do with highlighting the pivot
# randomized pivot

import random
import time

def sort(obj):

    # fetch slowdowns:
    compareSD = obj.compareSD
    recursionSD = obj.recursionSD    

    default_b = obj.stripState[0][1]

    arr = obj.stripState
    obj.update()

    def quicksort(arr_in, start_index, end_index):

        time.sleep(recursionSD)

        obj.stripState = obj.highlight(start_index, end_index, default_b)

        if len(arr_in) > 1:

            pivot = start_index + random.randint(0, end_index - start_index)
            pivot_val = arr_in[pivot]

            l_part = start_index      # stores left partition

            # shift indexes into the right position:
            for i in range(start_index, end_index+1):
                
                #left, right = obj.comparePixel(i, pivot)
            
                #if (left != pivot) and (left != right):
                #    #insert into left partion
                #    #arr_in[i], arr_in[l_part] = arr_in[l_part], arr_in[i]
                #    obj.swapPixel(i, l_part)                    
                #    l_part += 1
                
                if arr_in[i] < pivot_val:
                    time.sleep(compareSD)
                    # insert into left partition
                    #arr_in[i], arr_in[l_part] = arr_in[l_part], arr_in[i]
                    obj.swapPixel(i, l_part)
                    l_part += 1
                
                obj.update()

            # shift pivot into the correct position:
            pivot = arr_in.index(pivot_val) # find new location of pivot
            while arr_in[pivot] < arr_in[pivot-1] and pivot != start_index:
                arr_in[pivot], arr_in[pivot-1] = arr_in[pivot-1], arr_in[pivot]
                pivot -= 1
                
                obj.update()

            # recurse:
            if pivot != start_index:
                arr_in = quicksort(arr_in, start_index, pivot-1)
            if pivot != end_index:
                arr_in = quicksort(arr_in, pivot+1, end_index)

            return(arr_in)
    
        else:

            return arr_in

    quicksort(arr, 0, len(arr)-1)