import matplotlib.pyplot as plt
infile = open('1994averages.txt','r')
avg_1994 = infile.readlines()
weeks = []
for i in range(len(avg_1994)):
    avg_1994[i] = avg_1994[i].rstrip('\n')
    avg_1994[i] = float(avg_1994[i])

for i in range(1,53):
    weeks.append(i)
plt.plot(weeks,avg_1994)
plt.title('Weekly Gas Averages in 1994')
plt.xlabel('Week number')
plt.ylabel('Price in Dollars')
plt.xlim(left = 1, right =52)
plt.ylim(bottom = 0.5, top = 1.5)
plt.grid(True)
plt.show()

infile.close()