outfile = open('golf.txt','w')

cont = 'y'
while cont == 'y' or cont == 'Y':
    name = input("Enter golfer's name: ")
    score = int(input("Score: "))
    cont = input("Are there are more golfers? Enter y or Y for yes, anything else for no")
outfile.close()