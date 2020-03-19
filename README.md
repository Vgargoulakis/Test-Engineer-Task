# Test-Engineer-Task
## Description :
 
This function accepts a single list as a parameter. This list could consist of any number of lists (1..n) and each of these lists contain character strings (eg. ['a' , 'b' , 'bc' ...]). The function prints out the following:
- Strings that appear in more than one list                                 
- The total number of unique strings across all lists
- The total number of strings that were processed


For the first print, by using two loops (for loop inside for loop), I have added the functions 'itertools.combinations(iterable,r)' and 'itertools.product()' in order to create all the unique combinations of r between the sub-lists. For every single combination, I have made the comparison between the elements in order to check if they are equal. I have also used a selection structure for avoiding duplicates.

For the second print, I have added all the elements from the initial sub-lists in one list. This helped me to isolate later in another list all the unique strings.
 
For the third print, just counted the number of all the elements on the one list.

## Dependencies :
Python 3 version
