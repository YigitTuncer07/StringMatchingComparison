import sys
import time

"""Kanka Python'da fonksiyon isimleri küçük harf oluyor.
Böyle bir hatayı senin gibi nizami yazan adama yakıştıramadım."""

start_time = time.time()

comparisons = 0

btable = {}

gtable = []

length = 0

with open('test.html', 'r') as file:
    lines = file.readlines()
    

def conbadtable(word):
    global btable
    global length
    length = len(word) - 1
    i = 0
    while i < length:
        btable[word[i]] = length - i
        i += 1


def congoodtable(word):
    global gtable
    global length
    try:
        i = length - btable[word[length]]
    except KeyError:
        return
    lgtable = 1
    le = lgtable
    while i >= 0:
        if word[i] == word[length-lgtable+le]:
            if not le:
                le = lgtable
            le -= 1
            i -= 1
        else:
            if not le:
                gtable.append(length-lgtable-i)
                lgtable += 1
                i = length - lgtable
            if le >= lgtable:
                i -= 1
            le = lgtable
    gtable.append(length - le - 1)
    lgtable -= 1
    for i in range(length-lgtable-1):
        gtable.append(gtable[lgtable])


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
                i += (btable[line[i + c]] + c)
            except KeyError:
                i += (length + 1)
            a = length


def boyermoore(word):
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
            c = length - a
            if c:
                try:
                    temp = max(btable[line[i]] - c, 1)
                    temp2 = gtable[c - 1]
                    i += (max(temp, temp2) + c)
                except KeyError:
                    i += length + 1
            else:
                try:
                    i += ((btable[line[i]]) + c)
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

#Constructs tables. Since brute force does not need it, we have to change for loop below
#Length which assigned in bad table, is word's length - 1.
conbadtable(word)
congoodtable(word)

method = input("Enter how the string should be found: ")
if (((method != "brute") and (method != "horspool") and (method != "Boyer"))):
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
    elif method == "Boyer":
        boyermoore(word)
    else:
        print("horsealgo")


    lines[i] = line

print("Number of comparisons: " + str(comparisons))

with open('test.html', 'w') as file:
    file.writelines(lines)
    

print(time.time() - start_time, "seconds")








