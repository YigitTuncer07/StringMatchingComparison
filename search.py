import sys
import time

start_time = time.time()

comparisons = 0

with open('test.html', 'r') as file:
    lines = file.readlines()
    
    
    
    
def getLookupTable(word):
    print()

    
    
    
    
def horspoolSearch(sentence,word):
    print("hi")



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




word = input("Enter the word: ")
method = input("Enter how the string should be found: ")
if (((method != "brute") and (method != "horsepool") and (method != "boyar"))):
    print("false input")
    sys.exit(1)


for i in range(len(lines)):
    line = lines[i]
    
    if (method == "brute"):
        index = bruteSearch(line,word)
        if (index != -1):
            line = line[:index] + '<mark>' + word + '</mark>' + line[index+len(word):]
            found = True            
    elif (method == "horsepool"):
        print("horsealgo")
           
    else:
        print("horsealgo")


    lines[i] = line

print("Number of comparisons: " + str(comparisons))

with open('test.html', 'w') as file:
    file.writelines(lines)
    

print(time.time() - start_time, "seconds")








