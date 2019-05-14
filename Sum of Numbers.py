infile = open('numbers.txt','r')
total = 0
for line in infile:
    line = line.rstrip('\n')
    total += int(line)
print(total)