file_name = input("Enter the name of the file: ")
infile = open(file_name,'r')
count = 1
while count <= 5:
    print(infile.readline())
    count +=1
infile.close()