name = input("Enter the name of the file: ")
infile = open(name,'r')
count = 1
for i in infile:
    print(count,':',infile.readline().rstrip('\n'))
    count += 1
infile.close()