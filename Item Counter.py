infile = open('names.txt','r')
count = 0
for name in infile:
    count += 1
print(count)