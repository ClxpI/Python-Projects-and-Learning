# Portfolio Task - Gerrymandering
# Author:
# Date:

from drawingPanel import * 

def main():
    initialise()
    mainBody()
    terminate()

def initialise():
    pass


'''
  Function to display introductory message
'''

def displayIntroduction():
    print("This program allows you to search through")
    print("data about congressional voting")    
    print("and determine")
    print("gerrymandered")
    print()


'''
  Function to read state details from the district text file
  create a list containing the name of the state and
  each individual district and its votes as a separate block
'''

def readStateDetails(state):
    # initialise state details list
    stateDetails = []
    
    # initialise lineNum to process no of lines in the text file
    lineNum = 0

    # convert identified state to lowercase
    requiredState = state.lower()

    # open district text file foe reading from
    with open ("districts.txt", "r") as myFile:
        # read each line from the text file 
        for line in myFile:
            # increment lineNum
            lineNum = lineNum + 1
            # test to see if required state is in this line
            if line.lower().find(requiredState) != -1:
               # remove hidden end of line character code (/n)
               line.rstrip("/n")

               # initialise inner list
               innerList = []
               
               # Convert text line into a list innerList
               innerList = [elt.strip() for elt in line.split(',')]
 
               # Calculate noOfRistricts in the state
               noOfDistricts = (len(innerList) - 1) // 3

               # Initialise list state details
               stateDetails = []
               # Append name of the state to the state details list
               stateDetails.append(innerList[0])
               # For each district determine its district number, votes for each party
               # and append that as a new item list to the state details list
               for districts in range(1, noOfDistricts):
                   districtDetails = innerList[(districts * 3) - 2 : (districts * 3) + 1]
                   stateDetails.append(districtDetails)
 
    print(stateDetails)


    # Return state details list
    return stateDetails

 
        

    
def mainBody():
    
    # Introduction section
    displayIntroduction()

    # Prompt user for the name of the state
    state = input("Please enter the name of the state: ")
    print()

    # Read state details from the district file
    stateDetails = readStateDetails(state)

    # If the state is found then
    if state == True:
        with open ("eligible_voters.txt", "r") as myFile2:
        # print the total wasted votes of democrats
        
        print()

        # print the total wasted votes of republicans

        # print the total voters in the state

        # calculate which party won

        # print who has gained an advantage from gerrymandering the state

        # print if it is gerrymandered

        # display information about the state graphically
    else:
        print(state+" not found.")
    

def terminate():
    pass

main()


    
