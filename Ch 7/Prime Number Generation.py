def is_prime(n):
    if n < 2:
        return False
    limit = int(n ** 0.5)+1
    div = 2
    while div < limit:
        if n%div ==0:
            return False
        div += 1
    return True

def main():
    num_list = []
    num = int(input("Enter how many numbers: "))
    for i in range(num):
        if is_prime(i+1):
            num_list.append(i+1)
    print('The prime numbers are: ')
    for num in num_list:
        print(num)

main()