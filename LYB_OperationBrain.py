"""
Author: Corey Lambert
Date Written:7/01/2024
Assignment: Final Project
This Program is designed as an interface to hold and operate all paperwork documnetation inside of factory.....
"""
import tkinter as tk

from tkinter import messagebox
# password lists
user_passwords = ["user1","user2"]
supervisor_passwords = ["super1", "super2"]

# validate password
def password_access():
    password = password_entry.get()
    if password in user_passwords:
        messagebox.showinfo("Let's Work", "User Acces Granted.")
        LYB_OperationBrain("User")
    elif password in supervisor_passwords:
        messagebox.showinfo("Let's Work", "Supervisor Controls Granted")
        LYB_OperationBrain("Supervisor")
    else:
        messagebox.showerror("Error", "Invalid Password")


def LYB_OperationBrain(role):
    main_app = tk.Toplevel(root)
    main_app.title(f" {role} Version")
    main_app.geometry("300x200")
    
    label = tk.Label(main_app, text= f"Welcome - {role} Version")
    label.pack(pady=35)

    daily_trackingButton = tk.Button(main_app, text="Daily Tracking Sheet",
                                command= tracking_sheet)
    daily_trackingButton.pack(pady= 4)

    run_trackingButton = tk.Button(main_app, text= "Run Time Sheet",
                                   command= run_sheet)
    
    run_trackingButton.pack(pady= 4)
    
def tracking_sheet():
    messagebox.showinfo("You selected Tracking Sheets")

def run_sheet():
    messagebox.showinfo("You Selected Run TIme Tracking Sheets")



root = tk.Tk()
root.title("LYB Operation Brain - Validate Creditials")
root.geometry("300x200")

password_label = tk.Label(root, text= "Enter Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show= "*")
password_entry.pack(pady=10)

validate_button = tk.Button(root, text= "Validate", command= password_access)
validate_button.pack(pady=15)

root.mainloop()
