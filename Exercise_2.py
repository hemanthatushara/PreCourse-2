# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[low]
    i = low
    j = high
    while ( i<j):
        while (arr[i]<= pivot and i<high):
            i+= 1
        while (arr[j]>pivot):
            j-= 1
        
    
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    print(arr)
    return j

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    while(low<high):
        j = partition(arr, low, high)
        quickSort(arr, low, j)
        quickSort(arr, j+1,high)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
# pivot = 10, i =0, j = 5
# 10, 5, 8, 9, 1, 7
# 10, 5, 7, 9,1,8
#10, 5, 7, 8, 9, 1
#1, 5, 7, 8,9,10
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
