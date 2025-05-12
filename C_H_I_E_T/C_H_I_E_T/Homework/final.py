import fileinput

if __name__ == "__main__":

    while True:
        print("\nAssignment Tracker Menu:")
        print("1. Add Assignment")
        print("2. view Assignment")
        print("3. remove assignments")
        print("4. mark assignments as completed")
        print("5. exit app")

        choice = input("Enter your choice: ") #asks the user to make a choice
        
        if choice == "1": #if user choses 1 they get asked about the assignment details
            title = input("Enter assignment title: ")
            due_date = input("Enter due date (e.g., YYYY-MM-DD): ")
            description  = input("Enter the description of the assignment: ")
            with open("assignments.txt", "a") as f:
              f.write(title)   #write the assignment details into the tex file
              f.write(" ")
              f.write(description)
              f.write(" ")
              f.write(due_date)
              f.write("\n")
              f.close()
        
        elif choice == "2":
          with open("assignments.txt", "r") as f:
             content = f.read()    #labelling read the file as content
             contentList = content.split("\n")   #splits the string into a list for each new line
             count = 0
             for content in contentList:
              count += 1
              print(f"[{count}]: {content}") #labels each line with numbers 1,2,3 ect
         
        elif choice == "3":
            line_number = input("Enter the line number you want to remove: ")
            try: #this makes it so that the code will not break if unidentifiable answers are entered
                line_number = int(line_number)  
                with open("assignments.txt", "r") as f:
                    lines = f.readlines()    #labeling the reading lines in the text file action as lines
                if 1 <= line_number <= len(lines):  
                    del lines[line_number - 1]
                    
                    with open("assignments.txt", "w") as f:
                        f.writelines(lines)
                    print(f"Line {line_number} removed.") #tells the user what line was removed
                else:
                    print("line/assignment not found.")
            except ValueError:
                print("Please enter a valid number.")   #if the user doesn't input a valid line number
        
        elif choice == "4":
            L = input("Enter the line number you would like to mark: ")
            try:
                L = int(L)
                with open("assignments.txt", "r") as f:
                    lines = f.readlines() #labeling the reading lines in the text file action as lines

                if 1 <= L <= len(lines):
                    lines[L - 1] = lines[L - 1].rstrip() + "  [Completed]\n" #this writes completed on the line

                    with open("assignments.txt", "w") as f:
                        f.writelines(lines)
                    print(f"Line {L} marked as completed.") #tells the user which line was marked as completed
                else:
                    print("line/assignment not found.")  #if line not found in the file
            except ValueError:     
                print("Please enter a line number with an assignment.") #asks the user to try typing another line number
             

        elif choice == "5": 
            print("Exiting App. Have a great day!")
            break #break will exit out of the while loop
        else:
            print("Invalid choice. Please select a valid option.")