import sys
import time

"""Kanka Python'da fonksiyon isimleri küçük harf oluyor.
Böyle bir hatayı senin gibi nizami yazan adama yakıştıramadım."""

start_time = time.time()

comparisons = 0

table = {}

with open('test.html', 'r') as file:
    lines = file.readlines()
    

def getlookuptable(word):
    global table
    le = len(word) - 1
    i = 0
    while i < le:
        table[word[i]] = le - i
        i += 1
    return le


def horspoolsearch(word):
    global length
    global comparisons
    global line
    size = len(line)
    i = length
    a = length
    while i < size:
        comparisons += 1
        if line[i] == word[a]:
            if a:
                i -= 1
                a -= 1
            #There is a match
            else:
                a = length
                line = line[:i] + '<mark>' + word + '</mark>' + line[i + length + 1:]
                i += (length + 14)
        else:
            try:
                c = length - a
                i += (table[line[i + c]] + c)
            except KeyError:
                i += (length + 1)
            a = length




def bruteSearch(sentence,word): 
    global comparisons
    sentenceLength = len(sentence)
    wordLength = len(word)
    for i in range(sentenceLength):
        j = 0
        while j < wordLength and sentence[i + j] == word[j]:
            j = j + 1
        comparisons = comparisons + j + 1 #This increments count with the number of comparisons
        #The +1 is because we count the failed comparisons aswell
        if (j == wordLength):
            return i
    return -1




word = input("Enter the word: ").strip()

#Constructs table. Since brute force does not need it, we have to change for loop below
#Length is word's length - 1.
length = getlookuptable(word)

method = input("Enter how the string should be found: ")
if (((method != "brute") and (method != "horspool") and (method != "boyar"))):
    print("false input")
    sys.exit(1)


for i in range(len(lines)):
    line = lines[i]

    # For optimization all search functions must know length of word.
    # Also method does not change in loop
    if (method == "brute"):
        index = bruteSearch(line,word)
        if (index != -1):
            line = line[:index] + '<mark>' + word + '</mark>' + line[index+len(word):]
            found = True            
    elif (method == "horspool"):
        horspoolsearch(word)
           
    else:
        print("horsealgo")


    lines[i] = line

print("Number of comparisons: " + str(comparisons))

with open('test.html', 'w') as file:
    file.writelines(lines)
    

print(time.time() - start_time, "seconds")








