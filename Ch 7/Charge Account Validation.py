def main():
    infile = open('charge_accounts.txt','r')
    accounts = infile.readlines()
    for i in range(len(accounts)):
        accounts[i] = accounts[i].rstrip('\n')
    num = input("Enter a charge number: ")
    if num in accounts:
        print("The charge number is valid")
    else:
        print("The charge number is invalid")
main()