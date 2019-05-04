tuition = 8000
percent_increase = 1.03
for year in range(1,6):
    tuition *= percent_increase
    print("In {} year(s) the tuition will be #{:.2f} dollars".format(year,tuition))