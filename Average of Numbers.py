infile = open('numbers.txt','r')
count = 0
total = 0
for line in infile:
    line = line.rstrip('\n')
    line = int(line)
    total += line
    count += 1
print(total/count)