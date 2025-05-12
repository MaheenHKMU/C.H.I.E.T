#_main_flie_
 


from subprocess import call



def main():
    while True:
        print('\n      Hello world    \n')
        print(' Welcome to Interactive Education(English edidtion)\n')
        print ('press 1 to explore grammar')
        print ('press 2 to explore vocabulary')
        print ('press 3 to play riddles')
        print ('press 4 to leave this page')
        # give guest to input
        user = input ('Enter: ').replace(' ','')
        if user == '1':
            call (["python","English\\Grammar.py"])
        elif user == '2':
            call (["python","English\\Vocabulary.py"])
        elif user == '3':
            call (["python","English\\riddles.py"])
        elif user == '4':
            print('\nBye Bye\n')
            break
        else:
            print("\n Invalid Input")






if __name__ == "__main__":
    main()