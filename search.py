import sys
import time

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
    l1 = length
    #lgtable is length of good suffix table+1
    lgtable = 1
    le = lgtable
    # shortcut is if pattern does not have same pre letter with any k value (EX: ...323...323 while k = 2)
    # used for terminating function
    shortcut = True
    while lgtable < (length+1):
        if word[i] == word[l1]:
            if not le:
                # false condition
                shortcut = False
                le = lgtable
                l1 = length
            else:
                le -= 1
                l1 -= 1
                i -= 1
        else:
            if not le:
                # true condiition
                gtable.append(l1 - i)
                lgtable += 1
                i = length - btable[word[length]]
            elif le == lgtable:
                i -= 1
            l1 = length
            le = lgtable
        if i == -1:
            gtable.append(l1 + 1)
            lgtable += 1
            if shortcut:
                return
            le = lgtable
            l1 = length
            i = length - btable[word[length]]

def horspoolsearch():
    global word
    global length
    global comparisons
    global line
    global btable
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
    global btable
    global gtable
    size = len(line)
    sizegtable = len(gtable) - 1
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
                    try:
                        temp2 = gtable[c - 1]
                    except IndexError:
                        temp2 = gtable[sizegtable]
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
    size = len(line)
    j = 0
    i = 0
    while i < size:
        comparisons += 1
        if line[i] == word[j]:
            j += 1
            if j == (length + 1):
                temp = '<mark>' + word + '</mark>'
                temp = temp + line[(i + 1):]
                line = line[:(i - length)] + temp
                i += 13
                size += 13
                j = 0
        else:
            i -= j
            j = 0
        i += 1

#.strip() for if input has space in begining or ending
word = input("Enter the word: ").strip()

method = input("Enter how the string should be found: (brute, horspool, boyer)")

start_time = time.time()

if method == "brute":
    length = len(word) - 1
    for i in range(len(lines)):
        line = lines[i]
        brutesearch()
        lines[i] = line
    print("bad table not generated for brute force")
    print("good table not generated for brute force")
elif method == "horspool":
    conbadtable()
    for i in range(len(lines)):
        line = lines[i]
        horspoolsearch()
        lines[i] = line
    print(btable)
    print("good table not generated for horspool's")
elif method == "boyer":
    conbadtable()
    congoodtable()
    for i in range(len(lines)):
        line = lines[i]
        boyermoore()
        lines[i] = line
    print(btable)
    print(gtable)
else:
    print("Unknown algorithm")
    sys.exit(1)


print("Number of comparisons: " + str(comparisons))

with open('textSample1.html', 'w') as file:
    file.writelines(lines)
    
finalTime = time.time() - start_time
finalTime = finalTime * 1000
print(finalTime, "milli seconds")