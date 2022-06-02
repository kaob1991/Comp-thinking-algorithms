# Benchmarking test on 5 algorithms
# measuring the average runtime for 10 runs on various algorithms 
# As part of submission for Computational Thinking With Algorithms 
# Author: Katie O'Brien G00398250

# Credit: https://github.com/sanaynesargi/SortBenchmarker
# Credit: https://www.programiz.com/dsa/radix-sort#:~:text=In%20this%20tutorial%2C%20you%20will,to%20their%20increasing%2Fdecreasing%20order.
# Credit: https://stackabuse.com/radix-sort-in-python/
# Credit: https://www.angela1c.com/projects/cta_benchmarking/ctabenchmarkingproject
# Credit: https://runestone.academy/ns/books/published/pythonds/SortSearch/TheQuickSort.html

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Bubblesort code

def bubblesort(arr):
# While conditions are being met, the code runs
    while True:
        #index starts at 0
        i = 0
        swaps = 0
        # While i is less than the length of the array -2, continue swapping code. 
        while i < len(arr) - 2:
            # If i is greater than i + 1 , swap the elements and increase count of i by 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
            i += 1
        # If there are no swaps, break out of the while loop
        if swaps == 0:
            break
    #Return the array 
    return arr

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# MergeSort code

#If the length of the array is one, return array
def mergesort(arr):
    if len(arr) == 1:
        return arr
#Getting the midpoint of the array and creating 2 variables to take the 1st and 2nd halves of the array 
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
# Running mergesort on both sub-arrays to sort
    mergesort(left)
    mergesort(right)
# Creating 3 placeholder variables all with value 0 
    i = 0
    j = 0
    k = 0
#Copying data to temp arrays created above left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
# Checking to ensure no elements are left 
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Counting sort in Python

def countingsort(inputArray):
    # Find the maximum element in the inputArray
    maxEl = max(inputArray)

    countArrayLength = maxEl+1

    # Initialize the countArray with (max+1) zeros
    countArray = [0] * countArrayLength

    # Traverse the inputArray and increase 
    # the corresponding count for every element by 1
    for el in inputArray: 
        countArray[el] += 1

    # For each element in the countArray, 
    # sum up its value with the value of the previous 
    # element, and then store that value 
    # as the value of the current element
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    # Calculate element position
    # based on the countArray values
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Radix sort code

def countingSortForRadix(inputArray, placeValue):
    # We can assume that the number of digits used to represent
    # all numbers on the placeValue position is not greater than 10
    countArray = [0] * 10
    inputSize = len(inputArray)

    # placeElement is the value of the current place value
    # of the current element, e.g. if the current element is
    # 123, and the place value is 10, the placeElement is
    # equal to 2
    for i in range(inputSize): 
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    # Reconstructing the output array
    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1
        
    return outputArray

def radixsort(inputArray):
    # Find the maximum element in the input array
    maxEl = max(inputArray)

    # Find the number of digits in the `max` element
    D = 1
    while maxEl > 0:
        maxEl /= 10
        D += 1
    
    # Initialize the place value to the least significant place
    placeVal = 1

    
    outputArray = inputArray
    while D > 0:
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10  
        D -= 1

    return outputArray

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Quick Sort

def quicksort(array):
    # call a recursive function that takes in the array, 
    quick_Sort(array,0,len(array)-1)
    return array

# if length of list passed in is > 1, partition the array and recursively sort it
def quick_Sort(array,first,last):
    if first<last:
        splitpoint = partition(array,first,last)  # find the split point
        # recursively call the function on the two halves of the array
        quick_Sort(array,first,splitpoint-1)
        quick_Sort(array,splitpoint+1,last)

# a function to partition the array using the pivot element, 
def partition(array,first,last):
    # the pivot is the first element in the array
    pivotvalue = array[first]
    # the first pointer is the first element in the remaining unsorted part
    leftmark = first+1
    # the right pointer is the last element remaining 
    rightmark = last

    done = False
    while not done:
        # move the first pointer right until the first element > pivot is found
        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        # move the second pointer left until the first element < pivot 
        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        # stop when the second pointer is less than the first pointer (when cross over) 
        if rightmark < leftmark:
            done = True
        else:
           # using simulataneous assignment to swap the values that are out of place
            array[leftmark],array[rightmark]  = array[rightmark], array[leftmark]
    # swap with the pivot value 
    array[first],array[rightmark] = array[rightmark],array[first]

    return rightmark
