import sys
import time


start_time = time.time()

comparisons = 0

# Bad symbol table as dictionary
btable = {}

# Good suffix table as list
gtable = []

# Pattern's length-1. It will be assigned later
length = 0

with open('test.html', 'r') as file:
    lines = file.readlines()
    

# Construction of bad symbol table
def conbadtable():
    global word
    global btable
    global length
    length = len(word) - 1
    i = 0
    while i < length:
        btable[word[i]] = length - i
        i += 1


#Construction of good suffix table
def congoodtable():
    global word
    global gtable
    global length
    # Since we construct the bad symbol table, we know previous occurrence of pattern's last letter
    try:
        i = length - btable[word[length]]
    # If there is a KeyError, pattern's last letter is not in pattern
    # So all values must be length of pattern
    except KeyError:
        return
    # lgtable is length of good suffix table + 1
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
    # If index (i) of pattern becomes 0 and if length of good suffix table is less than pattern's length,
    # Add last value of good suffix table to rest of table's empty values.
    for i in range(length-lgtable-1):
        gtable.append(gtable[lgtable])


def horspoolsearch():
    global word
    global length
    global comparisons
    global line
    size = len(line)
    i = length
    a = length
    while i < size:
        comparisons += 1
        # Character match
        if line[i] == word[a]:
            if a:
                i -= 1
                a -= 1
            #Pattern match
            else:
                a = length
                line = line[:i] + '<mark>' + word + '</mark>' + line[i + length + 1:]
                i += (length + 14)
        else:
            c = length - a
            # If pattern's last letter's comparison is in bad symbol table,
            # Increases index by it. Otherwise, increases it by pattern's length
            try:
                i += (btable[line[i + c]] + c)
            except KeyError:
                i += (length + 1)
            a = length


def boyermoore():
    global word
    global length
    global comparisons
    global line
    size = len(line)
    i = length
    a = length
    while i < size:
        comparisons += 1
        #Character match
        if line[i] == word[a]:
            if a:
                i -= 1
                a -= 1
            #Pattern match
            else:
                a = length
                line = line[:i] + '<mark>' + word + '</mark>' + line[i + length + 1:]
                i += (length + 14)
        else:
            c = length - a
            if c:
                # If last comparison is in bad symbol table and good suffix table, applies formula
                # Otherwise, increases it by pattern's length
                try:
                    temp = max(btable[line[i]] - c, 1)
                    temp2 = gtable[c - 1]
                    i += (max(temp, temp2) + c)
                except KeyError:
                    i += length + 1
            else:
                # If pattern's last letter's comparison is in bad symbol table,
                # Increases index by it. Otherwise, increases it by pattern's length
                try:
                    i += btable[line[i]]
                except KeyError:
                    i += (length + 1)
            a = length


def brutesearch():
    global word
    global comparisons
    global length
    global line
    sentenceLength = len(line)
    wordLength = length + 1
    for i in range(sentenceLength):
        j = 0
        while j < wordLength and line[i + j] == word[j]:
            j = j + 1
        comparisons = comparisons + j + 1  #This increments count with the number of comparisons
        #The +1 is because we count the failed comparisons aswell
        if j == wordLength:
            line = line[:i] + '<mark>' + word + '</mark>' + line[i + len(word):]
            i += (wordLength + 13)


#.strip() for if input has space in begining or ending
word = input("Enter the word: ").strip()


method = input("Enter how the string should be found: ")


if method == "brute":
    for i in range(len(lines)):
        line = lines[i]
        brutesearch()
        lines[i] = line
elif method == "horspool":
    conbadtable()
    for i in range(len(lines)):
        line = lines[i]
        horspoolsearch()
        lines[i] = line
elif method == "Boyer":
    conbadtable()
    congoodtable()
    for i in range(len(lines)):
        line = lines[i]
        boyermoore()
        lines[i] = line
else:
    print("Unknown algorithm")
    sys.exit(1)

print("Number of comparisons: " + str(comparisons))

with open('test.html', 'w') as file:
    file.writelines(lines)
    

print(time.time() - start_time, "seconds")