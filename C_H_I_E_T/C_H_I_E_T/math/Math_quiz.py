# math_quiz

import random


# 12 question in total
# list of math question and answer
math_Q_and_A = [
    {
    "question":"What is the formulae of Quadratic equation",
    "answer": "ax^2+bx+c",
    },
        {
    "question":"If 1=3,2=3,4=4 and 5=4 what is 6 equal to",
    "answer": "3",
    },
    {
    "question":"Solve  - 15+ (-5x) =0",
    "answer": "-3",
    },
    {
    "question":"Look at this series: 53, 53, 40, 40, 27, 27, … What number should come next?",
    "answer": "14",
    },
    {
    "question":"If 13 x 12 = 651 & 41 x 23 = 448, then, 24 x 22 =?",
    "answer": "924",
    },
    {
    "question":"How many feet are in a mile?",
    "answer": "5280",
    },
    {
    "question":"How to get a number 100 by using four sevens (7’s) and a one (1)??",
    "answer": "100",
    },
    {
    "question":"There is a three-digit number. The second digit is four times as big as the third digit, while the first digit is three less than the second digit. What is the number?",
    "answer": "141",
    },
    {
    "question":"If the side of a square is of length (x + 5), what is its area?",
    "answer": "x^2+10x+25",
    },
    {
    "question":"What is the graph of y = 7x - 1?",
    "answer": "circle",
    },
    {
    "question":"How much interest is earned if $2500 is invested for 25 years at 8% simple interest?",
    "answer": "5000",
    },
    {
    "question":"What value of y makes y/(-10) = 100 a true statement?",
    "answer": "1000",
    },
    {
    "question":"What is the x-intercept of 4x + 2y = -8?",
    "answer": "-2",
    },
    {"question":" Find the missing terms in multiple of 3: 3, 6, 9, __, 15",
     "answer":"12",
     },
     {"question":" The largest 4 digit number is:",
     "answer":"9999",
     }


]

print("\nWelcome to my Maths Quiz\n")
print("enter 'exit' to go back\n")

random.shuffle(math_Q_and_A) #making the question randomly



score = 0

# using for-loop to go through the question and answer
for question in math_Q_and_A:
    print(question["question"])

     # promt the users the input
    answer = input("Enter your answer: " ).lower().replace(' ','')

    # using if statement
    if answer == question["answer"]:
        print("CORRECT!!!""\n")
        score = score +1
    elif answer == 'exit' :
        print(f"YOU GOT {score} out of {len(math_Q_and_A)} questions correct.")
        break
    else:
        print(f"\nWORNG!\nThe answer was {question["answer"]}.\n")

#scoring tracking part

with open ('math\\math_score.txt', 'r') as f:
    prev_score = int(f.read())
if prev_score == score:
    print(f"YOU GOT {score} out of {len(math_Q_and_A)} questions correct!!!.\nThanks for practicing.\n")
elif prev_score < score:
    print(f"You got {score}, you are improving\n")
else:
    print(f"YOU GOT {score} out of {len(math_Q_and_A)} questions correct.\n")
    print("No improvement\n")

with open('math\\math_score.txt', 'w') as f:
    f.seek(0)
    f.write(str(score))
