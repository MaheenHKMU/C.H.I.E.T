#timetable

import json # allows structured storage of timetable information.

# Brief Description:
# This program manages a weekly timetable, allowing users to add, edit, display and delete classes/events
# Data is stored in a JSON file, making it easy to read and write structured information.

FILENAME = 'timetable.json'  # File to store the timetable data


def load_timetable():
    """Load the timetable from a JSON file."""
#File I/O - this function attempts to read timetable data from a file (Lecture 8)

    try:
        with open(FILENAME, 'r') as file:
            return json.load(file) # json.load() reads the JSON data from the file and converts it into a Python dictionary.
    except (FileNotFoundError, json.JSONDecodeError):
        return {} # Returns an empty dictionary if the file doesn't exist or is invalid.


def save_timetable(timetable):
    """Save the timetable to a JSON file."""
    # File I/O - this function writes the timetable data to a JSON file

    with open(FILENAME, 'w') as file:
        json.dump(timetable, file) # converts dictionary into JSON format and then writes it into the file.


def add_class(timetable):
    """Add a new class/event to the timetable."""
    # Functions - handles the addition of new class/event (Lecture 7)

    day = input("Enter the day of the week: ")
    subject = input("Enter the subject/event name: ")
    time = input("Enter the time: ")

    # Decision structure - checks if the day already exists in the timetable (Lecture 4)
    if day not in timetable:
        timetable[day] = [] # if not, creates a new list for that day
    timetable[day].append({'subject': subject, 'time': time}) # Data collection - Append a new dictionary containing subject and time to the list for the given day.
    save_timetable(timetable)
    print("Class/Event added successfully!")


def display_classes(timetable):
    """Display all classes/events in the timetable."""
    # Decision Structure - Checks if there are any classes/events to display

    if not timetable:
        print("No classes/events found.") 
        return # Exit the function if there are no classes/events
    
    # Loop through the timetable to display each day's classes/events
    for day, classes in timetable.items(): # data collection - iterating over the dictionary
        print(f"\n{day}:")
        for idx, cls in enumerate(classes, start=1):           # Enumerate creates an index for each class and tracks the index of items within the class list. 
                                                               # This helps perform actions that require the item and its position in the list.
                                                               # The start=1 argument specifies that the enumeration should start at 1 instead of the default 0.
            print(f"{idx}. {cls['subject']} at {cls['time']}")


def edit_class(timetable):
    """Edit an existing class/event in the timetable."""
    # Functions- allows users to modify an existing class/event 

    display_classes(timetable)
    day = input("Enter the day of the class/event you want to edit: ")
    
    if day in timetable:                                                          # Check if the specified day exists in the timetable
        try:
            display_classes({day: timetable[day]})                                    # displays classes/events for that specific day 
            index = int(input("Enter the index of the class/event to edit: ")) - 1    # get index to edit
        
            # Validate the index input
            if 0 <= index < len(timetable[day]):
                new_subject = input("Enter the new subject/event name: ")
                new_time = input("Enter the new time: ")
                timetable[day][index] = {'subject': new_subject, 'time': new_time}
                save_timetable(timetable)
                print("Class/Event updated successfully!")
            else:
                print("Invalid index.") 
        except ValueError:
            print("No classes/events found for that day.")


def delete_class(timetable):
    """Delete a class/event from the timetable."""
    # Functions

    display_classes(timetable)
    day = input("Enter the day of the class/event you want to delete: ")
    
    if day in timetable:
        try:
            display_classes({day: timetable[day]})
            index = int(input("Enter the index of the class/event to delete: ")) - 1  # Get index to delete the specific class/event
        
            if 0 <= index < len(timetable[day]):
                timetable[day].pop(index) # Remove the specified class/event
                if not timetable[day]:  # Remove the day if no classes left
                    del timetable[day]
                save_timetable(timetable)
                print("Class/Event deleted successfully!")
            else:
                print("Invalid index.")
        except ValueError:
            print("No classes/events found for that day.")


def menu():
    """Display the menu and handle user choices."""


    timetable = load_timetable() # Load existing timetable data from the file

    while True: # Repetition Structure (Lecture 5)- This loop continues to display the menu until the user exits
        print("\nTimetable Menu:")
        print("1. Add Class/Event")
        print("2. Display Classes/Events")
        print("3. Edit Class/Event")
        print("4. Delete Class/Event")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_class(timetable)  # Call function to add a class/event
        elif choice == '2':
            display_classes(timetable) 
        elif choice == '3':
            edit_class(timetable)  
        elif choice == '4':
            delete_class(timetable) 
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()