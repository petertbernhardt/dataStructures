# Simple code/methods to practice with Maps (known as Dictionaries) in Python
class MapPractice():
    def __init__(self):
        return
    
    # Write a method contains3 that accepts a List of strings as a parameter 
    # and returns true if any single string occurs at least 3 times in the list, and false otherwise. Use a map as auxiliary storage. 
    def containsThree(self, stringList):
        dictionary = dict()
        for string in stringList:
            if string in dictionary:
                dictionary[string] = dictionary.get(string) + 1
            else:
                # String isn't in the dictionary, add it
                dictionary[string] = 1
        for string in dictionary.keys():
            if dictionary[string] >= 3:
                return True
        return False
    
    # Write a method hasOdd that takes a Set of integers as a parameter and that returns True if the set contains at least one odd
    # integer, and False otherwise. If passed an empty set, your method should return False
    def hasOdd(self, numSet):
        if not numSet:
            # stringSet is empty
            return False
        for x in numSet:
            if x % 2 == 1:
                return True
        return False
    
    # Write a method maxLength that takes a Set of strings as a parameter and that returns the length of the longest string in the set.
    # If your method is passed an empty set, it should return 0
    def maxLength(self, stringSet):
        if not stringSet:
            return 0
        maxLen = 0
        for word in stringSet:
            if len(word) > maxLen:
                maxLen = len(word)
        return maxLen
    