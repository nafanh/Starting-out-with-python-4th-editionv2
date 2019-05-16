import random
def generate_randoms():
    random_list = []
    for i in range(7):
        random_list.append(random.randint(0,9))
    return random_list

def main():
    random_num_list = generate_randoms()
    for rand in random_num_list:
        print(rand)
main()
#test