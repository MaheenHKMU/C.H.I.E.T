import os
from datetime import datetime

Attendance_record = "Attendance_Data.txt"

def load_record():
    record = []
    if os.path.exists(Attendance_record):
        with open(Attendance_record, "r") as file:
            for line in file:
                date, present_time, subject = line.strip().split(" | ")                                                
                #Pull the data from the data file 
                record.append({"date": date, "present_time": present_time, "subject": subject})                        
    return record

def save_record(record):
    with open(Attendance_record, "w") as file:
        for event in record:
            file.write(f"{event['date']} | {event['present_time']} | {event['subject']}\n")                           
             # save the data in a readable format

def display_attendance(record):
    if not record:
        print("No record.")
    else:
        find_subject = input('Which subject attendance do you want to check? (input "no" to check the whole record):')
        if find_subject.lower() == "no":
            print('Attendance record:')
            for i, event in enumerate(record):
                print(f"{i + 1}. Present {event['subject']} in {event['date']} {event['present_time']}")
        else:
            found = False
            print(f'Attendance record for subject: {find_subject} ')
            for i, event in enumerate(record):
                if event['subject'].lower() == find_subject.lower():                                                
                    #search function for the displaying 
                    print(f"{i + 1}. Present {event['subject']} in {event['date']} {event['present_time']}")
                    found = True
            if not found:
                print(f"No attendance records found for subject: {find_subject}")


def take_attendance(record):
    today = datetime.now().date()                                                                                   
    #Get the current date
    
    while True:
        date = input("Enter today's date (YYYY/MM/DD): ")
        try:
            entered_date = datetime.strptime(date, "%Y/%m/%d").date()                                               
            #Check to format is correct or not. If the format is not correct, it will return Value error 
            if entered_date > today:                                                                                
                #Check to see the entered date is correct or not
                print("The date cannot be in the future. Please enter a valid date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use YYYY/MM/DD.")

    while True:
        present_time = input("Enter the time (HH:MM): ")
        try:
            time_obj = datetime.strptime(present_time, "%H:%M")
            if time_obj.hour < 0 or time_obj.hour > 23 or time_obj.minute < 0 or time_obj.minute > 59:              
                #Check the time is in the vaild range
                print("Time must be in the range of 00:00 to 23:59. Please enter a valid time.")
            else:
                break
        except ValueError:
            print("Invalid time format. Please use HH:MM.")

    subject = input("Enter subject name/code: ")
    record.append({"date": date, "present_time": present_time, "subject": subject})
    save_record(record)                                                                                             
    #Save the attendance into the data file 
    print(f"Attendance recorded for lesson {subject} on {date} at {present_time}.")


def clear_record(record):
    confirm = input("Are you sure you want to clear all attendance records? (yes/no): ")
    
    if confirm.lower() == 'yes':
        with open(Attendance_record, "w") as file:
            file.write('')                                                                                         
             #Clean the record in the file  
        record.clear()                                                                                              
        #Clean the record in the Dictionary that temporary save the record 
        print("All attendance records have been cleared.")
        
    else:
        print("Clearing records aborted.")

def edit_record(record):
    if not record:
        print("No records available to edit.")
        return
    
    print("Current attendance records:")
    for i, event in enumerate(record):
        print(f"{i + 1}. {event['subject']} on {event['date']} at {event['present_time']}")    
        #for loop to display the record                    

    while True:
        try:
            record_index = int(input("Enter the record number to delete (or 0 to cancel): ")) - 1
            if record_index == -1:
                #for the user to escape from the function
                print("Deletion cancelled.")
                return
            elif 0 <= record_index < len(record):
                deleted_record = record.pop(record_index)   
                #delete the record in the chosen line                                                                         
                save_record(record)
                print(f"Record deleted: {deleted_record['subject']} on {deleted_record['date']} at {deleted_record['present_time']}")
                return
            else:
                print("Invalid record number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    record = load_record()
    print('Welcome to the class attendance tracker')
    while True:
        print('1. Take attendance')
        print('2. Check attendance')
        print('3. Clear all record')
        print('4. Edit attendance record')
        print('5. Exit')
        choice = input('Input your choice: ')
        
        if choice == '1':
            take_attendance(record)
        elif choice == '2':
            display_attendance(record)
        elif choice == '3':
            clear_record(record)
        elif choice =='4':
            edit_record(record)
        elif choice=='5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
