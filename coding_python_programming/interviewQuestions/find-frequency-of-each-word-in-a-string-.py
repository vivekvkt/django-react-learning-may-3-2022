
#find-frequency-of-each-word-in-string
def findFrequencyWords(str1):
    str2 = str1.split()
    
    uniq_str = set(str2)
    
    for s in uniq_str:
        print(f"{s} is {str2.count(s)} times occurs")
    
str1 = "Apple Mango Orange Mango Guava Guava Mango"
findFrequencyWords(str1)

