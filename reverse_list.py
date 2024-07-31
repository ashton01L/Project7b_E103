# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/30/2024
# Description: Define a function named 'reverse_list' that takes as a parameter
# a list and reverses the order of the elements in that list.

def reverse_list(numlist):
    """
    Defines a function called 'reverse_list' that takes in a parameter of a list of
    numbers called 'numlist'.
    :param numlist: list of numbers to be take as a parameter and then reversed
    by the function.
    :return: No return prompted based on instructions.
    """

    # Assigns variables to the left-most and right-most elements of the list
    left = 0
    right = len(numlist) - 1

    # A while loop to flip the left and right elements of the list and then
    # move them each towards center.
    while left < right:
        numlist[left], numlist[right] = numlist[right], numlist[left]
        left += 1
        right -= 1

# numlist = [7, -3, 12, 9] # list of numbers to reverse.
# reverse_list(numlist) # reverses the list of numbers given.
# print(numlist)  # this will print [9, 12, -3, 7].
