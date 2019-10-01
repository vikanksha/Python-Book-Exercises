# Write a program to verify if two given strings are Anagram.
def isAnagram(a,b):

    if sorted(a) == sorted(b):
      return "This is Anagram"
    else:
      return "This is Not Anagram"  
print(isAnagram("google", "apple"))