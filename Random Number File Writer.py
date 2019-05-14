import random
num = int(input("Enter how many random numbers you want: "))
outfile = open('random.txt','w')
count = 1
while count <= num:
    outfile.write(str(random.randint(1,500)) + '\n')
    count += 1
outfile.close()