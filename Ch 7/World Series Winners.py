def main():
    infile = open('WorldSeriesWinners.txt','r')
    win = infile.readlines()
    for i in range(len(win)):
        win[i] = win[i].rstrip('\n')
    user_win = input("Enter a team: ")
    count = 0
    for name in win:
        if user_win == name:
            count += 1
    print("The {} have won the world series {} time(s).".format(user_win,count))




main()