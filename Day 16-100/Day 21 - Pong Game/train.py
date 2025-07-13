#Check to see if a string has the same amount of 'x's and 'o's.
#The method must return a boolean and be case insensitive. The string can contain any char.

numbers = [1,2,3,4,5]
def remove_smallest(numbers):
    smallest = min(numbers)
    amended = []
    for item in numbers:
        if item != smallest:
            amended.append(item)
    return amended

print(remove_smallest(numbers))