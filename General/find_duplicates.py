from time import process_time

# Function to print duplicates
import numpy as np

def printRepeating(arr, size):
    print("The repeating elements are: ")
    temp = {}
    dup = {}
    for item in arr:
        if item in temp:
            #print(item)
            dup[item] = item
            #pass
        else:
            temp[item] = item
    return dup


# Driver code
arr = np.random.randint(10, size=1000000)
arr_size = len(arr)

# Start the stopwatch / counter
t1_start = process_time()

#arr = [1, 2, 3, 1, 3, 6, 6]

res = printRepeating(arr, arr_size)
print(len(res))
# Stop the stopwatch / counter
t1_stop = process_time()

elapsed_time = round((t1_stop - t1_start) * 1000,2)
print("time : " + str(elapsed_time) + " ms")
