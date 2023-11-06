#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""

import json
import os

class main():

    def __init__(self) -> None:
        with open('data.csv','r+') as file:
            data = file.read()
            if data == None:
                file.write(json.dumps('{"0":"0"}'))
                print("funny")
        self.DataStart()

    def DataStart(self):
        choice = int(input("Hello there, what would you like to do: \n1) Create Assignment    \n2) Enter in an Edit   \n3) Delete an Edit   \n4) View Assignment    \n5) Do Nothing\nselect:    "))
        if choice == 1:
            self.Create()
        if choice == 2:
            self.Edit()
        if choice == 3:
            self.Delete()
        if choice == 4:
            self.View

    def Create(self):
        Assignment = str(input("What is your Assignment Name:    ")).capitalize()
        amount = int(input("enter the amount of students:   "))
        with open('data.csv','r') as file:
            data = file.read()
        with open('data.csv','w') as file:
            sent = json.loads(data)
            sent[f"{Assignment}"] = {}
            for i in range(amount):
                name = input("What is the Students Name:   ").capitalize()
                mark = input(f"what is {name}'s mark:   ")
                sent[f"{Assignment}"][f"{name}"] = f"{mark}"
            file.write(json.dumps(sent))
            print("success")    
            
            


    def Edit(self):
        with open('data.csv','r+') as file:
            data = file.read()
            sent = json.loads(data)
            list_of_assignments = [i for i in sent if i != 0]
            print(f"which assignment do you want to change: {list_of_assignments}")
            chosen_assignment = str(input("What assignment do you want to change:   ")).capitalize()
            list_of_students = [i for i in sent[chosen_assignment]]
            student = str(input(f"Which student do you want to change the mark of: {list_of_students}:  ")).capitalize()
            new_mark = int(input(f"what is {student}'s new mark:    "))
            sent[f"{chosen_assignment}"][f"{student}"] = f"{new_mark}"
            file.write(json.dumps(sent))
            print("it works")

            
        
    def AbeKopis(self):

        pass
    def Delete(self):
        os.remove('data.csv')
        with open('data.csv','w') as file:
            file.write('{"0":"0"}')

        pass
    def View(self):
        pass
main()