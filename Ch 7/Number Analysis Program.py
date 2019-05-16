def main():
    print("You will enter a series of 20 numbers")
    count = 1
    num_list = []
    while count <= 20:
        num = int(input("Enter number {}: ".format(count)))
        num_list.append(num)
        count += 1
    lowest = min(num_list)
    highest = max(num_list)
    total = sum(num_list)
    average = total/20
    print("The lowest number is:",lowest)
    print("The highest number is:",highest)
    print("The sum of the number is:",total)
    print("The average of the numbers is:",average)


main()