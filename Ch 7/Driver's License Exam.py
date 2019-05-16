def main():
    #Create variable for number correct answers
    correct = 0
    #List stores the question numbers that are incorrect
    incorrect_answers_list= []
    #Opens the answer key and puts the correct answers into a list
    answers = open('answers.txt','r')
    answer_list = answers.readlines()
    #Remove the new line character from answer keys
    for i in range(len(answer_list)):
        answer_list[i] = answer_list[i].rstrip('\n')
    #opens the student answers and stores them into a list
    student_answers = open('student_answers.txt','r')
    student_answers_list = student_answers.readlines()

    #parses the student answers and compares them to the answer key
    for i in range(len(student_answers_list)):
        student_answers_list[i] = student_answers_list[i].rstrip('\n')
        if student_answers_list[i] == answer_list[i]:
            correct += 1
        else:
            incorrect_answers_list.append(i+1)

    #prints the data
    total_incorrect = len(answer_list) - correct
    print("The total number of questions correct is:",correct)
    print("The total number of incorrect is:",total_incorrect)
    if len(incorrect_answers_list) == 0:
        print("You didn't get any questions wrong")

    print("The question numbers wrong are:",end = ' ')
    for num in incorrect_answers_list:
        print(num,end=' ')
    print()
    if correct >= 15:
        print("You passed")
    else:
        print("You failed")

    answers.close()
    student_answers.close()

main()
