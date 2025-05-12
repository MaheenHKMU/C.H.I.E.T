#Main page

from subprocess import call

def main():
    while True:
        print('*****   *   *   *   *****   *****')
        print('*       *   *   *   *         *  ')
        print('*       *****   *   *****     *  ')
        print('*       *   *   *   *         *  ')
        print('*****   *   *   *   *****     *  ')
        print("\npress 1 to get info on C.H.I.E.T")
        print("press 2 to explore Classroom Attendance Tracker")
        print("press 3 to explore Homework Assignment Tracker")
        print("press 4 to explore Interactive Quiz(math edition)")
        print("press 5 to explore Educational English ")
        print("press 6 to explore Timetable Scheduler")
        print("press 7 to Budget plan")
        print("press 8 to exit\n")
        user = input("Enter: ").replace(" ","")

        if user == "1":
            print("\nC.H.I.E.T stands for;")
            print("  Classroom Attendance Tracker")
            print("  Homework Assignment Tracker")
            print("  Interactive Quiz")
            print("  Educational Learning")
            print("  Timetable scheduler")
            print("\nThe main page serves as the central hub, with six child pages / modules connected to it:")
            print("This modular design allows students to access and utilize various educational tools to manage academic tasks, quizzes, schedules, and budgets within a single application.")
            print("This comprehensive system seems well suited to address the challenges faced by students in organizing their studies and learning experience.\n")
            print("At C.H.I.E.T, We are a group of passionate studens who have come together to develop an innovative application to transform the educational experience.")
            print(" Our team, comprising individuals with diverse backgrounds and skills, recognized the need for acomprehensive tool to help students better manage their academic responsibilities and foster engaged learning\n")
            print("\nBy:")
            print("  Thomas")
            print("  Yunchho")
            print("  Rohan")
            print("  Maheen")
            print("  Albin\n")
        elif user == "2":
            call (["python","class_atten\\class_attendance.py"])
        elif user == "3":
            call (["python","Homework\\final.py"])
        elif user == "4":
            call (["python","math\\Math_quiz.py"])
        elif user == "5":
            call (["python","English\\Interactive Education(English edition).py"])
        elif user == "6":
            call (["python","Timetable\\TimeTableSchedules.py"])
        elif user == "7":
            call(["python", "Budgeting\\Budgetplanner.py"])
        elif user =="8":
            print("Bye Bye\n")
            break
        else:
            print("\nInvalid Input\n")


if __name__== "__main__":
    main()
