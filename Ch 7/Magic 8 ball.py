import random
def main():
    infile = open('8_ball_responses.txt','r')
    responses = infile.readlines()
    for i in range(len(responses)):
        responses[i] = responses[i].rstrip('\n')
    question = input("Enter a question: ")
    print(responses[random.randint(0,len(responses)-1)])
    infile.close()
main()