#subint
#Create a function that takes a number and a list of numbers as a 
#parameter and returns the indeces of the numbers of the list which 
#contain the given number or returns an empty list (if the number is not part 
#of any of the numbers in the list)

#Example

#print(find_matching_indexes(1, [1, 11, 34, 52, 61])) 
#should print: [0, 1, 4] print(find_matching_indexes (9, [1, 11, 34, 52, 61])) 
#should print: '[]'

def find_matching_indexes(number, listOfNumbers):
    arrayOfindexes = []
    for i in range(0, len(listOfNumbers)):
        for j in str(listOfNumbers[i]):
            print (j)
            if (str(number)==j):
                arrayOfindexes.append(i)
                break
    print(arrayOfindexes)

find_matching_indexes(5, [123, 23, 54, 724, 5])