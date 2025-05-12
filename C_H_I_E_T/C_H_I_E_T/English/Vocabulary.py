# project 1
# Quiz_ Game

#for random
import random
import json

#library of MCQ 
practice = [
    {
        "prompt": "which one of the following spelling is correct?",
        "options" :["A. Electronic", "B. Electornic", "C. Eleactronic", "D. Electronick"],
        "answer" : "A"
    },
    {
        "prompt": "Which of the following spelling is correct?",
        "options":["A. Investigate", "B. Investygate", "C. Inviestygate", "D.Investtigate"],
        "answer" : "A"
    },
    {
        "prompt": "which of the follwing spelling is correct?",
        "options": ["A. Concillate ","B. Concilatt","C. Conciliate","D. all of then above"],
        "answer": "C"
    },
    {
        "prompt": "what is the synonym of allow?",
        "options": ["A. disallow","B. permit","C. follow","D. all of them above"],
        "answer" : "B"
    },
    {
        "prompt": "what is the synonym of flee ?",
        "options": ["A. flee ","B. stop","C. forbid","D. escape"],
        "answer" : "D"
    },
    {
        "prompt": "what is the synonym of disable ? ",
        "options": ["A. strong","B. brave","C. furious","D. handicapped"],
        "answer" : "D"
    },
    {
        "prompt": "what is the opposite word of changeable ?",
        "options": ["A. likeable ","B. constant","C. eveloution","D. all of them above"],
        "answer" : "B"
    },
    {
        "prompt": "what is the opposite word of aruge?",
        "options": ["A. aruge","B. not aruge","C. agree","D. arugement"],
        "answer" : "C"
    },
    {
        "prompt": "what is the ooposite words of near ?",
        "options": ["A. futher","B. distained","C. far","D. all of them above"],
        "answer" : "C"
    },
    
]

# def function for practice

def quick_pract(practice):
    # make the practice question randomize
    random.shuffle(practice)

    #give them instruction 
    print("\nThere are 9 question in this practice.\n")

    #give them option to quit the practice
    print("\npress 3 to quit the practice\n")
    score = 0#start with zero ofc

    #using for loop to loop throuh the question
    for pract in practice:
        print(pract["prompt"])
        for option in pract["options"]:
            print(option)

        #user to input
        answer = input("Enter your answer: " ).upper().replace(" ","")
        if answer == pract["answer"]:
            print("CORRECT!!!""\n")
            score = score +1
        elif answer == '3':
            
            break
        else:
            print(f"\nWORNG!\nThe answer was {pract["answer"]}.\n")

    #using I/O function to store score of the practice
    with open ('English\\vocab_quiz.txt', 'r') as f:
        prev_score = int(f.read())

    if prev_score == score:
        print(f"YOU GOT {score} out of {len(practice)} questions correct.\nThanks for practicing.\n")
    elif prev_score < score:
        print(f"You got {score}, you are improving\n")
    else:
        print("No improvement\n")

    with open('English\\vocab_quiz.txt', 'w') as f:
        f.seek(0)
        f.write(str(score))

#The main page for Vocabulary
def vocabulary():
    print("\nWelcome to Vocabulary\n")
    print("In Vocabulary, you will find new word to add it to your vocabulary and improve your spelling, synonyms.\n")
    
    while True:
        print("press 1 for Vocabulary List")
        print("press 2 to learn oppsite word and synonyms")
        print("press 3 for quick practice")
        print("press 4 to go back\n")

        guest = input('Enter: ')

        if guest == "1":
            #show the list of vocab
            #with open json file to show the list of vocab
            with open ('English\\vocab.json') as v:
                vocab = json.load(v)
                for vo in vocab['vocab_list']:
                    print(f"\n{vo['word']}: {vo['define']}\n")

        elif guest == "2":
            # show the oppo and syno
            with open('English\\vocab.json') as v:
                vocab = json.load(v)
                for opp in vocab['opposite']:
                    print(f"\n{opp['define']}\n")
                    for syn in vocab['synonym']:
                        print(f"{syn['define']}\n\n")

        elif guest == '3':
            # make a game
            quick_pract(practice)

        elif guest == '4':
            #break the page
            print("Thanks for your stay\n")
            break

        else:
            print("Invaild input, press the follwing option\n")


vocabulary()