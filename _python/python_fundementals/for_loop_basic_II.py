#Biggest Size - Given a list, write a function that changes all positive numbers in the list to "big".

def biggie_size(x):
    for i in range(len(x)):
        if(x[i]>0):
            x[i]="big"
    return x

#Count Positives
#Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).

def count_positives(x):
    counter = 0
    for i in range (len(x)):
        if(x[i]>0):
            counter +=1

    x[len(x)-1]=counter
    return x

#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.

def sum_total(x):
    sum =0
    for i in range (len(x)):
        sum +=x[i]

    return sum

#Average - Create a function that takes a list and returns the average of all the values

def average(x):
    sum =0
    for i in range (len(x)):
        sum +=x[i]

    return sum/len(x)

#Length - Create a function that takes a list and returns the length of the list.

def length(x):
    counter =0
    while counter < len(x):
        counter +=1

    return counter
# or return len(x)

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.

def minimum(x):
    min=0
    if(x):
        for i in range(len(x)):
            if(x[i]<min):
                min=x[i]
        return min
    else:
        return False
    
#Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.

def maximum(x):
    max=0
    if(x):
        for i in range(len(x)):
            if(x[i]>max):
                max=x[i]
        return max
    else:
        return False
    
#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def ultimate_analysis(x):
    sumTotal = 0
    min = 0
    max = 0
    length = 0
    
    if(x):
        for i in range(len(x)):
            length+=1
            if(x[i]>max):
                max=x[i]
            if(x[i]<min):
                min=x[i]
            sumTotal+=x[i]
        return {'sumTotal': sumTotal, 'average': sumTotal/length, 'minimum': min, 'maximum': max, 'length': length }
    else:
        return False
    
#Reverse List - Create a function that takes a list and return that list with values reversed. 
#Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)

def reverse_list(x):
    x.reverse()
    return x

def reverse_list2(arr):
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp
    return arr

#testing print statement    
print(reverse_list2([37,2,1,-9]))