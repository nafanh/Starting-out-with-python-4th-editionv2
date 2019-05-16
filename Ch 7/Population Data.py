def main():
    infile = open('USPopulation.txt','r')
    pop = infile.readlines()
    total = 0
    for i in range(len(pop)):
        pop[i] = pop[i].rstrip('\n')
        pop[i] = int(pop[i])
        total += pop[i]
    min_pop = min(pop)
    max_pop = max(pop)
    print('The Average population change over {} years is: {:.0f}'.format(len(pop),total/len(pop)))
    print('The year with the smallest population change is {}'.format(1950 + pop.index(min_pop)+1))
    print('The year with the largest populaiton change is {}'.format(1950 + pop.index(max_pop)+1))

main()