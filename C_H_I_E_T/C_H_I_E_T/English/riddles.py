#Ridlle

#function for random
import random
import json
import sys





# The main page of riddles

def riddles_page():
    # welcome the guest

    print("\nWelcome to the riddle Game\n")
    print("Riddle is a fun way to workout your brain.\nIt can improve creativity as well as strengthen your logic and critical thinking skills.\n")
        
    while True:
        #Give options to play the game or leave

        print("\npress 1 to play the game")
        print("press 2 to Exit the game\n")

        # Promt the guest the choice

        start = input("Enter: ").replace(" ","")
        if start == "1":

            CHANCES = 3 #they will start from 3 lives

            print("\n\nYou have 3 chances chance so Answer carefully.\n""Please use One word to describe your answer.\n")
    
            print("press 2 to go exit the riddle game\n")
              
              # open json
            with open ('English\\riddle.json') as f:
                riddle = json.load(f)

                # random json question
                random.shuffle(riddle['riddles'])

                # time for the question
            for question in riddle['riddles']:
                print(question['question'])
                answer = input("Answer: ").lower().replace(" ","")



                    # give them option to break out
                if answer == '2':
                    print('Thanks for playing Riddle\n')
                    sys.exit()

                while  answer != question['answer']:
                    CHANCES -= 1
                    if CHANCES == 0:
                        print(f"The answer was {question["answer"]}\n")
                        sys.exit()

                    print(f"\nYou have {CHANCES} try left\n")
                    
                    answer = input("Enter your answer: " ).lower().replace(' ','')
                    
                    if answer == question['answer']:
                        break

                    elif answer == "2":
                        sys.exit()


                if answer == question["answer"]:
                    print('welldone\n')

  


         # exist the riddle
        elif start == "2":
            print("Thanks for your stay\n")
            break
        else:
            print("\nInvalid, please press 1 or 2\n")


riddles_page()

        
