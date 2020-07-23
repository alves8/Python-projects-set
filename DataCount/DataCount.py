import re
# Open the file and save it in a variable (wordCount) to obtain the string.
with open('text.txt', 'r') as file1:
    wordCount = file1.read()

print(type(wordCount))

print(wordCount)
# index each element by a value.
y = []
# separate letters by space
x = re.sub('[:,.!@#$]', '', wordCount)

x = wordCount.split()
print(type(x))
size = len(x)


print("Number of times the word is repeated")
for i in range(0, size):
    k=1
    for j in range(0, size):
        
        
        if (x[i] != " " and x[j] != " " and x[i] == x[j]):
           k += 1    
        
    print(x[i], ":", k, "x", ((k/size)*100),"%")

