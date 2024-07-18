"""
Author: Corey Lambert
Date Written:7/01/2024
Assignment: Final Project
This Program is designed as an interface to hold and operate all paperwork documnetation inside of factory. It starts with password validation.
Upon entering password it opens one of teo profiles user or supervisor. The user profile then opens to clickable buttons to select waht worksheets
the user wants to enter data into.... 
"""

import tkinter as tk

from tkinter import simpledialog, messagebox
# password lists and variable identification
user_passwords = ["user1","user2"]
supervisor_passwords = ["super1", "super2"]
temp_record = []

# validate password
def password_access():
    password = password_entry.get()
    #opens in either user profile or supervisor profile
    if password in user_passwords:
        messagebox.showinfo("Let's Work", "User Acces Granted.")
        LYB_OperationBrain("User")
    elif password in supervisor_passwords:
        messagebox.showinfo("Let's Work", "Supervisor Controls Granted")
        LYB_OperationBrain("Supervisor")
        #error if password incorrect
    else:
        messagebox.showerror("Error", "Invalid Password")

# main app 
def LYB_OperationBrain(role):
    main_app = tk.Toplevel(root)
    main_app.title(f" {role} Version")
    main_app.geometry("600x600")
    # identify which profile is being used
    label = tk.Label(main_app, text= f"Welcome - {role} Version")
    label.pack(pady=35)
# button declaration for main page
    daily_trackingButton = tk.Button(main_app, text="Daily Tracking Sheet",
                                command= tracking_sheet)
    daily_trackingButton.pack(pady= 4)

    run_trackingButton = tk.Button(main_app, text= "Run Time Sheet",
                                   command=lambda: run_sheet(main_app))
    run_trackingButton.pack(pady= 4)
  #define function of buttons  
def tracking_sheet():
    messagebox.showinfo("You selected Daily Tracking Sheets")

def run_sheet(parent):
    messagebox.showinfo("You Selected Run Time Tracking Sheets")
    temp_page(parent)
# different page for sheets
def temp_page(parent):
    temp_page = tk.Toplevel(parent)
    temp_page.title("Temperture Page")
    temp_page.geometry("600x600")

    label= tk.Label(temp_page, text= "Time and Temperture Page")
    label.pack(pady= 30)


   #buttons for data entry

    temp_recordButton =tk.Button(temp_page, text= "Temperature", 
                                 command=lambda: temp_check(temp_page))
    temp_recordButton.pack(pady= 6)
# open text box for user inputed data
def temp_check(parent):
    time= simpledialog.askstring("Input", "Enter Current Time:", parent= parent)
    
    temparature= simpledialog.askstring("Input","Enter the Current Temperature:",
                                        parent= parent)
# save data to list for use later
    if time and temparature:

        temp_record.append((time, temparature)) 
        # show it was inputed
        messagebox.showinfo("Data Entered")
        # error if entry is not complete
    else:
        messagebox.showwarning("Input Error, Enter Both Time And Temperature")



    
 
   
# Main app loop

root = tk.Tk()
root.title("LYB Operation Brain - Validate Creditials")
root.geometry("600x600")
# password entry box that blocks the characters entered
password_label = tk.Label(root, text= "Enter Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show= "*")
password_entry.pack(pady=10)

validate_button = tk.Button(root, text= "Validate", command= password_access)
validate_button.pack(pady=15)

root.mainloop()
