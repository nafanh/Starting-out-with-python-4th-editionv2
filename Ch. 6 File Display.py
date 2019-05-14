infile = open('numbers.txt','r')
for line in infile:
    print(line.rstrip('\n'))