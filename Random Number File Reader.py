infile = open('random.txt','r')
total = 0
count = 0
for num in infile:
    num = num.rstrip('\n')
    num = int(num)
    total += num
    count += 1

print("The total is:",total)
print("The number of random numbers in the file is:",count)
infile.close()