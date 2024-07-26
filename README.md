# SDEV140Final Requirements
Please follow the following requirements for your final project, this shows a detailed breakdown for how the points are distributed:  

The link of the GitHub repository for your final project. 10 points
A working GUI tkinter application with at least two windows.   50 points
Implementing a modular approach in your application. 10 points
Consistent clear navigation throughout the GUI application.   10 points
Use at least two images in your application(images should have alternate text).  10 points
Include at least three labels. 10 points
Include at least three buttons. 10 points
Include at least three call back function with each button, including exit button. 20 points
Implement secure coding best practices, including input validation to check if the user entered the correct data type, make sure the entry box is not empty, etc.   10 points
Validation testing - 20 points.  Develop an appropriate set of test data to fully validate the program against.

the data sets you tested against.

a brief written explanation of the results of your tests and what you had to fix.

screen shots of your good test data working.

User manual creation - 20 points.  You will write and submit a User's manual for your final project and submit it according to the instructions in the attached file.
Documentation of source code - 20 points.  You will fully document (comment) the corrected Python tkinter source code with appropriate comments including:
A brief explanation of the purpose of each module (Sub) at the beginning of each Sub. (A header's comment)
Explanation of the purpose of each variable where it is declared. (An end line comment)
Line by line, or at least section by section comments within the code, explaining what the line/section does. 
LYB Brain APP
"""
Author: Corey Lambert
Date Written:7/01/2024
Assignment: Final Project
This Program is designed as an interface to hold and operate all paperwork documnetation inside of factory.....


About The Program
This program is designed to hold and operate all key documents within a production factory. 
It starts with password validation. This opens one of two profiles. The user profile or the Supervisor profile. With these there are separate privilages.
The user profile opens up a selection of buttons to choose different sheets. 
once clicked the user is then prompted to key in information pertaining to the project they are on. This updates and saves into a visual tree as well as stores a total and average for each selection. 
The supervisor has same privalages but with access to the totals and the averages from the users profile. This allows for the supervisor to see waht is going on at any time. There will be more as i progress

7/16 Update :
So due to recent research I am revamping the program. The windows are to much each section it pops a new one. 
I am making the main a class to eliminate the global variables and clean it up a bit this will help with it down the road in final form. 
I also found a new way of going through pages I will be using the tk. Frame.  So instead of using dffernet windows navigation can be done through frames.
I also found I can import ttk from tkinter and have a tree view widget. I will be implementing this is the temp page and in the to be created tracking sheet pages. This will allow for a visual of the added data in long form.
I have ran into organizational issues and I still need to add back navigation and a exit program. I have been battling the fact of the program ending upon inputing one set of data.

7/25
The code is finally functional and runs great. I had to modify and eliminate the superviser function as it did nothing for this code and it can be added at a later date. Fot this project it was
not required. Honestly i ran out of time and greatl underestimated the time it would take to get to this part. Mulitple changes to original design were implimented to allow clearity for user to operate. 
The frames had to be organized differently and i spent alot of my time researching eays to do the tasks i wanted and what I pictured. I am happy with the result as it functions smoothly and 
the user should have no question of inputs to how to operate. I love the tree view as it almost duplicates the look of the paper version of sheets in use at this facility.

