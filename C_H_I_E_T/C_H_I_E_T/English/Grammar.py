# project 1
# Quiz_ Game
# List of past,present, future tense
#source esl grammer

#improting random and json
import random
import json

#making a library for question and answer for grammer quiz
gramm_quiz = [
    {
        "prompt": "The past tense of Teach?",
        "options":["A. Teach", "B. Taught", "C. Teached", "D. Teaches"],
        "answer" : "B"
    },
    {
        "prompt": "The young woman smiled __ John and John smiled back.",
        "options": ["A. at", "B. to", "C. in", "D. of"],
        "answer" : "A"
    },
    {
        "prompt": "if he ____ on talking like that, we will throw her out.",
        "options": ["A. went ", "B. going", "C. goes", "D. gone"],
        "answer" : "C"
    },
    {
        "prompt": "Tom ______ us to school every morning",
        "options" :["A. drive", "B. driven", "C. drived", "D. deives"],
        "answer" : "D"
    }
]
      
# this def function is for all the tenses
def tenses():
    print("\nIn this page you will learn Past, Present perfect and Future tense")
    
    #using While loop and boolean
    while True:
        print("1. learn Past tense")
        print("2. learn Present tense")
        print("3. learn Future tense")
        print("4. go back")

         #promting guest the input
        guest = input("I want to ").lower().replace(' ','')
         #using if statement
        if guest == '1'or guest == 'learnpasttense':
            #past_tenses 
            #used json file to store all the past tenses
            with open('English\\grammer.json') as g:
                gram = json.load(g)
                for pas in gram['past_tenses']:
                    print(f"\n{pas['topic']}\n{pas['define']}\n")
        elif guest == '2' or guest == 'learnpresentperfecttense':
            #pre_per
            #used json file file to store all the present past tense
            with open('English\\grammer.json') as g:
                gram = json.load(g)
                for pre in gram['present_tense']:
                    print(f"\n{pre['topic']}\n{pre['define']}\n")
        elif guest == '3' or guest == 'learnfuturetense':
            #fu_tenses()
            #used json file to store all the future tense
            with open('English\\grammer.json') as g:
                gram = json.load(g)
                for fut in gram['future_tense']:
                    print(f"\n{fut['topic']}\n{fut['define']}\n")
        #give user to exit the program
        elif guest =='4' or guest == 'goback':
            break
        else:
            print("\nInvaild Input\n")

#this def function is for grammer practice 
def gram_prac():
    #they will start from zero
    score = 0
    print('\n welcome to grammar practice')
    print('press 2 to exit the practice\n')
    
    #using random module to randomize the question
    random.shuffle(gramm_quiz)

    #using for-loop to loop through the question
    for question in gramm_quiz:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
         #give user the promt 
        answer = input("Enter your answer: " ).upper().replace(' ','')
        if answer == question["answer"]:
            print("CORRECT!!!""\n")
            score = score +1

        #give user the way to break out of the loop
        elif answer == '2':
            
            break
        else:
            print(f"\nWORNG!\nThe answer was {question["answer"]}.\n")

    #using I/O function to store the score of the practice.
    with open ('English\\gram_quiz_score.txt', 'r') as f:
        prev_score = int(f.read())
    if prev_score == score:
        print(f"YOU GOT {score} out of {len(gramm_quiz)} questions correct.\nThanks for practicing.\n")
    elif prev_score < score:
        print(f"You got {score}, you are improving\n")
    else:
        print(f"YOU GOT {score} out of {len(gramm_quiz)} questions correct.\n")
        print("No improvement\n")

    with open('English\\gram_quiz_score.txt', 'w') as f:
        f.seek(0)
        f.write(str(score))


def grammer_page():
    # greet the guest and tell them the propose of the page
    print("\nWelcome to grammar page\nIn this you will lern Tenses, proposition, if-clause, active & passive voice.\n")
    print("you might ask what's the use of learing this?\nWell, learning grammer has benifits such as improving your sentences structure and enhances clarity and more.\n")

    while True:
        #give them options
        print("press 1 for Tenses")
        print("press 2 for Preposition")
        print("press 3 for if-clause")
        print("press 4 for grammar practice")
        print("press 5 to go back\n")

        guest = input("Enter: ").replace(' ','')

        if guest == '1':
            tenses()
        elif guest =='2':
            #preposition()
            with open ('English\\grammer.json') as g:
                gram = json.load(g)
                for pre in gram['prepositions']:
                    print(f"\n{pre['topic']}\n{pre['define']}\n\n")
        elif guest == '3':
            #if_clause()
            with open ('English\\grammer.json') as g:
                gram = json.load(g)
                for cla in gram['If_clauses']:
                    print(f"\n{cla['topic']}\n{cla['define']}\n\n")
        elif guest == '4':
            gram_prac()
        elif guest == '5':
            print("\nSee you\n")
            break
        else:
            print("\nInvalid input\n")


grammer_page()