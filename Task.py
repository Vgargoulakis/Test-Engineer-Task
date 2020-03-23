import itertools
 
 
def myTask( list ):               # Definition of the function
 listOfStrResult = []
 oneList = []
 uniqueList = []
 uniqueNumber = 0
 totalNumber = 0
 
# Print 1
 for subList1 , subList2 in itertools.combinations( list , 2 ):
   for element1 , element2 in itertools.product( subList1 , subList2 ):
     if ( element1 == element2):
       if ( element1 not in listOfStrResult ):
         listOfStrResult.append(element1)
 print ("Strings that appear in more than one list:" , *listOfStrResult )        
 
# Print 2
 for subList in list :
   for element in subList:
     oneList.append(element)
 
 for element in oneList :
   if element not in uniqueList:
     uniqueList.append(element)
 
 for element in uniqueList:
   uniqueNumber = uniqueNumber + 1
 print ( "Number of unique strings:" , uniqueNumber )
 
# Print 3
 for element in oneList:
   totalNumber = totalNumber + 1
 print ( "Total number of strings processed:" , totalNumber )
 
# List of character strings initialization
listOfCharacterStr = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
 
myTask( listOfCharacterStr )        # Function call with a list as an argument
