#find second largest number in the list without any in-built function
#Note: List is not sorted.

numbers=[-10,-21]

largest = large = float('-inf')

if len(numbers)<2:
    print("Error!")
else:
    for i in numbers:
        if i > largest:
            large = largest
            largest = i
        elif large < i and i != largest:
            large = i
    if large != float('-inf'):
        print(large)
    else:
        print("None")
    

