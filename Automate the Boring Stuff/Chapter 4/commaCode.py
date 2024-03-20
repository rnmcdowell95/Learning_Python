# Practicing working with lists.
# This will copy the values of a list into a string, adding a comma after each value and an "and" before the last value.



def extractList(extractionList):

    #Creating a string variable to hold the extracted list.
    tempString = ''

    #Checks to see if extractionList
    if len(extractionList) == 0:

        #Lets the user know that no input was received.
        tempString = "This list is empty!"
        
        return tempString

    #Checks to see if extractionList has only one value.
    if len(extractionList) == 1:
        
        #Sets tempString equal to extractionList since there is only the one value.
        tempString = extractionList[0]

        return tempString

    #Iterates through the length of the list besides the last value.
    for i in range(len(extractionList) - 1):
        
        #Adds the current index value to tempString and adds in a comma.
        tempString = tempString + extractionList[i] + ', '

    #Adds an 'and' before adding the last value of extractionList to tempString.
    tempString = tempString + 'and ' + extractionList[-1]

    return tempString

#A list to use as a practice validation
practiceList = ['pie']

practiceString = extractList(practiceList)

print(practiceString)