def get_gnames():
    infile = open('GirlNames.txt','r')
    gnames = infile.readlines()
    for i in range(len(gnames)):
        gnames[i] = gnames[i].rstrip('\n')
    infile.close()
    return gnames

def get_bnames():
    infile = open('BoyNames.txt','r')
    bnames = infile.readlines()
    for i in range(len(bnames)):
        bnames[i] = bnames[i].rstrip('\n')
    infile.close()
    return bnames

def main():
    girl_names = get_gnames()
    boy_names = get_bnames()
    name = input("Enter a name: ")
    if name in boy_names:
        print("Popular Boy name")
    elif name in girl_names:
        print("Popular Girl name")
    elif name in boy_names and  girl_names:
        print("It's a popular boy and girl name")
    else:
        print("Not a popular boy or girl name")

main()

