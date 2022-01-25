import sys
import csv
from fruit import *

if __name__ == "__main__":
    keepgoing = "y" #trigger to keep running program
    while keepgoing == "y" or keepgoing == "Y":
        #parsing file for the information to the fruit in the basket --> creates an array of the rows containing the info of each individual piece of fruit
        filename = ""
        if len(sys.argv) > 1:
            filename = sys.argv[1]
        else:
            filename = input("Enter basket file name. Please include extension in name: ")
        fruitinfo = open(filename).read().replace(" ","").split("\n")
        fruitinfo.remove(fruitinfo[0])
        fruitinfo.sort()
        
        #overall number of fruit is easy, just return the length of the array
        total_number = str(len(fruitinfo))
        
        #total types of fruit --> create a set to prevent duplicates of fruit types
        fruittypes = set()
        
        #number of each type of fruit --> create a list of tuples
        numFruits = list()
        
        #creating a dictionary for characterizing fruit based on their traits
        fruitTraits = dict()
        
        #fruit over 3 days old --> creating a dictionary to link type of fruit + number of said fruit over 3 days old
        threedays = dict()
        
        #grabbing relevant data by iterating through the overall information in the basket file
        for i in range(len(fruitinfo)):
            currFruit = list(fruitinfo[i].split(","))
            thisFruit = fruit(currFruit)
            fruittype = thisFruit.fruittype
            daysOld = thisFruit.days
            traits = thisFruit.traits()
            
            #add type of fruit to total types of fruit
            fruittypes.add(fruittype)
        
            #add type of fruit to numFruits
            fruittuplesearch = [fruit for fruit in numFruits if fruit[1] == fruittype] #search if any element in numFruits already contains the current fruittype; len(fruittuplesearch should never be >1)
            if len(fruittuplesearch) == 0:  #if fruit type is not already in the list, add it with "1" as the associated number
                numFruits.append((1, fruittype))
            else: #associated number goes up by 1 if already in the list
                numFruitIndex = numFruits.index(fruittuplesearch[0])
                numFruitTuple = list(numFruits[numFruitIndex])
                numFruitTuple[0]+=1
                numFruits[numFruitIndex] = tuple(numFruitTuple)
                
            #add traits of fruit to fruit traits, key = the type of fruit and two traits as a triple, value = number of the type of fruit sharing the traits
            traittriple = (fruittype, str(traits[0]), str(traits[1]))
            if traittriple not in fruitTraits:
                fruitTraits[traittriple] = 0
            fruitTraits[traittriple] += 1
            
            #add data of fruit over 3 days old into the threedays dictionary
            if daysOld >= 3:
                if fruittype not in threedays: #add fruittype to dictionary if not already present
                    threedays[fruittype] = 0
                threedays[fruittype] += 1
            
        #display the total number of fruit
        print("Total number of fruit: " + total_number + "\n")
        
        #print length of set to display total number of types of fruit
        print("Types of fruit: " + str(len(fruittypes)) + "\n")
        
        #display date to display number of fruit in descending order
        print("The number of each type of fruit in descending order: ")
        numFruits.sort(reverse=True)    #sort list in descending order
        for i in range(len(numFruits)):
            print(numFruits[i][1] + ": " + str(numFruits[i][0]))
        print()
        
        #display data for traits of fruit
        traitkeys = list(fruitTraits.keys())
        traitkeys.sort()
        print("The characteristics (size, color, shape, etc.) of each fruit by type:")
        for i in range(len(traitkeys)):
            number = fruitTraits[traitkeys[i]]
            fruittype = traitkeys[i][0]
            trait1 = traitkeys[i][1]
            trait2 = traitkeys[i][2]
            traitString = str(number) + " " + fruittype
            if number > 1:  #add 's' to fruit types that are >1
                traitString += "s"
            traitString += ": "
            traitString += trait1 + ", " + trait2
            print(traitString)
        print()
        
        #build the string displaying the fruit over 3 days old
        threedaystring = ""
        threedaysfruit = list(threedays.keys())
        threedaysfruit.sort()
        for i in range(len(threedaysfruit)):
            number = threedays[threedaysfruit[i]]
            currFruit = threedaysfruit[i]
            threedaystring += (str(number) + " " + currFruit)
            if number > 1: #fruit types that number > 1 need to be plural
                threedaystring += "s"
            if len(threedaysfruit) > 1: 
                if i < (len(threedaysfruit) - 1) and (len(threedaysfruit) > 2): #if there are only two fruits, there should be no comma
                    threedaystring += "," 
                if i == (len(threedaysfruit) - 2): #add 'and' before the last fruit
                    threedaystring += " and"
            threedaystring += " "
            if i == (len(threedaysfruit) - 1):
                if len(threedaysfruit) == 1 and number == 1: #if there's only one fruit, be grammatically correct
                    threedaystring += "is over 3 days old"
                else:
                    threedaystring += "are over 3 days old"
        print(threedaystring)
        print()
        
        #if there are more baskets to sort, reply "y" or "Y"
        keepgoing = input("Keep going? Reply Y/N: ")
        if keepgoing == "y" or keepgoing == "Y":
            print()