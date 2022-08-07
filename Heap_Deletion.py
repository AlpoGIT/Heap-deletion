def sift_down(arr : list, i : int) -> list:
    '''
    input: list arr, index i of element to be sifted down the heap
    output: the list where arr[i] is removed and sifted down 
    preversing heap invariant. O(log n) operation
    '''
    # generate list of children of key[i]
    # children are at 2**i+1 and 2**i+2
    child_index_1 = 2*i+1
    child_index_2 = 2*i+2

    while child_index_1 < len(arr):
        # swap with min child key
        if child_index_2 < len(arr):
            # they are 2 children
            if arr[child_index_1] < arr[child_index_2]:
                mind_child_index = child_index_1
            else:
                mind_child_index = child_index_2
        else:
            # if 1 child
            mind_child_index = child_index_1
        
        if arr[i] > arr[mind_child_index]:
            # swap min child and parent
            tmp = arr[mind_child_index]
            arr[mind_child_index] = arr[i]
            arr[i] = tmp

            # update indices of children
            i = mind_child_index
            child_index_1 = 2*i+1
            child_index_2 = 2*i+2
        else:
            break

    return arr

def heap_delete(arr : list, i : int) -> list:
    '''
    input: a heap and an index such that arr[i] is deleted
    output: the list without arr[i] where the heap invariant is preserved.
    Done in O(log n) time.
    '''
    # put last element in place of arr[i], and sift down to retrieve heap invariant
    last_index = len(arr)-1
    arr[i] = arr[last_index]
    arr = sift_down(arr,i)

    # pop last element of list is O(1)
    arr.pop(-1)

    return arr


if __name__ == '__main__':
    # below an example
    import heapq
    import time
    import numpy as np

    L = list(np.random.randint(0,100,size=17))
    heapq.heapify(L)
    M = L.copy()

    start_time = time.time()
    output = L[0]
    L= heap_delete(L,0)

    print("--- %.20f seconds ---" % (time.time() - start_time))
    print(L)

    start_time = time.time()
    heapq.heappop(M)

    print("--- %.20f seconds ---" % (time.time() - start_time))
    print(M)

#    The thread 'MainThread' (0x1) has exited with code 0 (0x0).
#--- 0.06480026245117187500 seconds ---
#--- 0.00735378265380859375 seconds ---
#The program 'python.exe' has exited with code 0 (0x0).
