                                         *****   *   *   ***   *****   *****
                                         *       *   *    *    *         *
                                         *       *****    *    *****     *
                                         *       *   *    *    *         *
                                         *****   *   *   ***   *****     *

###Don't use macos###
-------------------------------------------------------------------------------------------------------------------
Make sure you run the program in Python 3.12.7 64-bit(Microsoft store) and open whole folder in VS code
-------------------------------------------------------------------------------------------------------------------
Follow the example in the code
-------------------------------------------------------------------------------------------------------------------
Start using C.H.I.E.T by opening the main.py
-------------------------------------------------------------------------------------------------------------------
Make sure you trust all the author in the folder
-------------------------------------------------------------------------------------------------------------------
Please enjoy using C.H.I.E.T !!!!!
-------------------------------------------------------------------------------------------------------------------
Here are some test case:

Attendance tracker
1. take attendance

valid input:
Enter today's date (YYYY/MM/DD):2024/11/28
Enter the time (HH:MM):18:00
Enter subject name/code:Eng

invalid input:
Enter today's date (YYYY/MM/DD):202/11/28 or 2024/16/28 or 2024/11/36
Enter the time (HH:MM):25:00 or 20:80
Enter subject name/code: Eng

2. display attendance

valid input:
Which subject attendance do you want to check? (input "no" to check the whole record):no or (subjecy name or code you have save in the record)

invalid input:
Which subject attendance do you want to check? (input "no" to check the whole record):30

3. clear attendance

valid input:
Are you sure you want to clear all attendance records? (yes/no):yes or no

invalid input:
Are you sure you want to clear all attendance records? (yes/no): hello world



Assignment tracker 

•	Press the run button, you will be greeted with a Menu of 5 options.

•	Type either 1/2/3/4/5 into the CLI then press enter to access add assignments, view assignments, remove assignments, mark assignments as complete, exit 

•	If you press options 1,2,3 or 4 type your answer into the CLI respectively then hit Enter. After you finish typing out all the information in whatever option you pick from 1-4. The program will go back to the main menu. 
 


assignment tracking menu - normal:
    when 3’s chosen from main menu you should see assignment menu
assignment tracking menu -abnormal:
   If 3’s chosen from the main menu and it doesn’t open or run properly this is abnormal.

1.    add assignment – normal:
Program will ask user for title, due date and description then will return to menu

1.     add assignment – abnormal:
The Program ask’s user for information but isn’t stored in txt file when function is completed.

2.     view assignment – normal: 
The code will List out all the assignments in the text file numbered, but last line should only have number and there should be nothing else

2.    view assignments – abnormal:
User has added an assignment, but the list is empty except for the first line with number.

3.   remove assignments – normal:
The Program asks user what line they want to remove. If there is data on the line, it will remove the line and type what line was removed. If there is no data on the line, it will say “line/assignment not found” and if they don’t enter a number 
“please enter a valid number. It should bring them back to the assignment menu if no data is found or wrong input.

3.   remove assignment – abnormal:
The program will tell the user there is no line found even if there is data on the line. Or it doesn’t remove the line.

4.    mark assignments as completed – normal:
The program asks the user the line they would like to mark, and it will say [completed] on the very right side of the assignment. If there is no assignment found on the line, or they type non integers it will tell them line not found or please type a number.

4.    mark assignments as complete – abnormal:
there is data on the line that the user chooses, but it still says line not found or it doesn’t say completed on the far-right side of the assignment or it is written somewhere else. 

5.    exit – normal:
It should break out of the while loop and return to the main menu of CHIET.

5.    exit – abnormal:
It doesn’t exit the program, and it says error in the CLI.




Math Quiz
Here are a few test cases you may consider while running the quiz:
1.	Basic Functionality: 
     o	   Run the quiz and answer all questions correctly.
     o	   Check if the score updates correctly.
2.	Incorrect Answers: 
     o	   Intentionally answer some questions incorrect.
     o	   Check if the program correctly identifies wrong answers and provides the correct answer.
3.	Testing exit: 
     o	   At any point in the quiz, type exit, and check if tthe program exits properly,providing the correct score.
4.	Score Improvement: 
     o	   Run the quiz twice. For the first time, answer some questions correctly to set a baseline score, then try to answer a few more correctly the next time to test the "You Are Improving" feedback.
     o	   After achieving a score, attempt to answer the same questions incorrectly for all answer and ensure the program states “No Improvement”
 



Eng
1)Main page of Educational English 

Input: Enter: 5
output: Invalid Input

Input: Enter: 1
output: welcome to grammar....

Input: Enter: 5
output: see you..(exit that page)

Input: Enter: 1
output: welcome to grammar....(goes to grammar page)


2) Grammar page

Input: Enter: 1
output : In this page...(goes to tense page) 
       Input: Enter 4
       output: press...(exit tense page) 


Input:  Enter: 6
output: Invalid 

Input: Enter: 5
output: see you..(exit that grammar page)


Input: Enter: 2
output: welcome...(Enter Vocabulary page)

3)Vocabulary page
Input: Enter: 2
output: The meaning....

Input: Enter:4
Output: Thanks....(exit Vocabulary page)
    

Input: Enter: -1
output: Invalid Input, press the following option


Input: Enter: 3
output: welcome...(goes to riddle page)

4) Riddle page
Input : Enter: uevzusbsj
output: Invalid, please press 1 or 2

Input:  Enter: 1
Output: You have...(the riddle game starts)
     Input: Answer: 2
     output: Thanks...(exit the riddle page)



Input: Enter: 4
output: Thanks for your stay...(exit Educational English page)

Timetable 
valid
For days : Monday
Subject description: Maths 
Time: 12:00
