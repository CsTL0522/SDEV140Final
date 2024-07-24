"""
Author: Corey Lambert
Date Written:7/01/2024
Assignment: Final Project
This Program is designed as an interface to hold and operate all paperwork documnetation inside of factory. It starts with password validation.
Upon entering password it opens one of teo profiles user or supervisor. The user profile then opens to clickable buttons to select waht worksheets
the user wants to enter data into.... 
"""

import tkinter as tk
from tkinter import messagebox, ttk

class LYBOperationBrainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LYB Operation Brain")
        self.root.geometry("500x500")

        self.user_passwords = ["user1", "user2"]
        self.entry_widgets = {}
        self.current_frame = None

        self.times = [f"{hour if hour != 0 else 12}:00 AM" for hour in range(12)] + \
                     [f"{hour - 12 if hour > 12 else 12}:00 PM" for hour in range(12, 24)]
        self.box_numbers = [str(i) for i in range(1, 101)]

        self.create_main_frame()
        self.create_machine_info_frame()
        self.create_main_app_frame()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        password_label = tk.Label(self.main_frame, text="Enter Password:")
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=10)

        validate_button = tk.Button(self.main_frame, text="Validate", command=self.password_access)
        validate_button.pack(pady=15)

        exit_button_main = tk.Button(self.main_frame, text="Exit", command=self.root.quit)
        exit_button_main.pack(pady=10)

        password_image = tk.PhotoImage(file="C:/Users/CTSL0/OneDrive/Documents/SDEV140/LYB_logo.png")
        password_image_label = tk.Label(self.main_frame, image=password_image)
        password_image_label.pack(pady=10)
        self.main_frame.password_image = password_image  # Keep a reference to prevent garbage collection

    def create_machine_info_frame(self):
        self.machine_info_frame = tk.Frame(self.root)

        machine_number_label = tk.Label(self.machine_info_frame, text="Enter Machine Number:")
        machine_number_label.pack(pady=10)
        self.machine_number_entry = tk.Entry(self.machine_info_frame)
        self.machine_number_entry.pack(pady=10)

        date_label = tk.Label(self.machine_info_frame, text="Enter Date: (MM/DD/YYYY)")
        date_label.pack(pady=10)
        self.date_entry = tk.Entry(self.machine_info_frame)
        self.date_entry.pack(pady=10)

        submit_button = tk.Button(self.machine_info_frame, text="Submit", command=self.submit_machine_info)
        submit_button.pack(pady=15)

        back_button_machine_info = tk.Button(self.machine_info_frame, text="Back", command=lambda: self.switch_frame(self.main_frame))
        back_button_machine_info.pack(pady=10)

        exit_button_machine_info = tk.Button(self.machine_info_frame, text="Exit", command=self.root.quit)
        exit_button_machine_info.pack(pady=10)

    def create_main_app_frame(self):
        self.main_app_frame = tk.Frame(self.root)

    def password_access(self):
        password = self.password_entry.get()
        if password in self.user_passwords:
            messagebox.showinfo("Let's Work", "User Access Granted.")
            self.show_machine_info_page("User")
        else:
            messagebox.showerror("Error", "Invalid Password")

    def show_machine_info_page(self, role):
        self.switch_frame(self.machine_info_frame)
        self.machine_info_frame.role = role

    def LYB_OperationBrain(self, role, machine_number, date):
        self.switch_frame(self.main_app_frame)
        self.root.geometry("1450x750")

        self.main_app_frame.title = f"{role} Version"

        label = tk.Label(self.main_app_frame, text=f"Welcome - {role} Version")
        label.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

        header_label = tk.Label(self.main_app_frame, text=f"Machine Number: {machine_number}, Date: {date}")
        header_label.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

        self.create_label_entry(self.main_app_frame, "Time:", 2, ttk.Combobox, values=self.times)
        self.create_label_entry(self.main_app_frame, "Box Number:", 3, ttk.Combobox, values=self.box_numbers)
        self.create_label_entry(self.main_app_frame, "Box Weight (LBS):", 4, ttk.Spinbox, from_=0, to=2000)
        self.create_label_entry(self.main_app_frame, "Temperature (°F):", 5, ttk.Spinbox, from_=0, to=800)
        self.create_label_entry(self.main_app_frame, "RPM:", 6, ttk.Spinbox, from_=0, to=10000)
        self.create_label_entry(self.main_app_frame, "Rate:", 7, ttk.Spinbox, from_=0, to=16000)
        self.create_label_entry(self.main_app_frame, "Run Comment:", 8, tk.Text, height=4, width=30)

        tree_image = tk.PhotoImage(file="C:/Users/CTSL0/OneDrive/Documents/SDEV140/Extruder.png")
        tree_image_label = tk.Label(self.main_app_frame, image=tree_image)
        tree_image_label.grid(row=2, column=3, rowspan=7, padx=10, pady=5, sticky="nsew")
        self.main_app_frame.tree_image = tree_image  # Keep a reference to prevent garbage collection

        submit_button = tk.Button(self.main_app_frame, text="Submit", command=self.submit_all_data)
        submit_button.grid(row=9, column=1, pady=10, sticky="nsew")

        tree = ttk.Treeview(self.main_app_frame, columns=("Time", "Box Number", "Box Weight", "Temperature", "RPM", "Rate", "Run Comment"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        tree.grid(row=10, column=0, columnspan=3, pady=10, sticky="nsew")
        self.treeview = tree

        self.current_machine_number = machine_number
        self.current_date = date

        back_button = tk.Button(self.main_app_frame, text="Back", command=lambda: self.switch_frame(self.machine_info_frame))
        back_button.grid(row=11, column=0, pady=10, sticky="nsew")

        exit_button = tk.Button(self.main_app_frame, text="Exit", command=self.root.quit)
        exit_button.grid(row=11, column=2, pady=10, sticky="nsew")

        for i in range(13):
            self.main_app_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.main_app_frame.grid_columnconfigure(i, weight=1)

    def create_label_entry(self, parent, text, row, widget_class, **options):
        label = ttk.Label(parent, text=text)
        label.grid(row=row, column=0, padx=5, pady=5, sticky=tk.W)
        
        if widget_class == ttk.Spinbox:
            validate_cmd = parent.register(self.validate_spinbox_input)
            options.update({'validate': 'key', 'validatecommand': (validate_cmd, '%P')})
        
        entry = widget_class(parent, **options)
        entry.grid(row=row, column=1, padx=5, pady=5, sticky=tk.W)
        
        key = text.replace(" ", "").replace("(", "").replace(")", "").replace(":", "").lower()
        self.entry_widgets[key] = entry
        print(f"Added entry widget for key: {key}")

    def validate_spinbox_input(self, value_if_allowed):
        return value_if_allowed.isdigit() or value_if_allowed == ""

    def submit_all_data(self):
        try:
            print(f"Current keys in entry_widgets: {self.entry_widgets.keys()}")
            time = self.entry_widgets["time"].get()
            box_number = self.entry_widgets["boxnumber"].get()
            box_weight = self.entry_widgets["boxweightlbs"].get()
            temperature = self.entry_widgets["temperature°f"].get()
            rpm = self.entry_widgets["rpm"].get()
            rate = self.entry_widgets["rate"].get()
            run_comment = self.entry_widgets["runcomment"].get("1.0", tk.END).strip()

            if all([time, box_number, box_weight, temperature, rpm, rate, run_comment]):
                self.treeview.insert("", "end", values=(time, box_number, box_weight, temperature, rpm, rate, run_comment))
                messagebox.showinfo("Data Entered", "All data has been entered successfully.")
                self.clear_entries()
            else:
                messagebox.showwarning("Input Error", "Please fill in all fields.")
        except KeyError as e:
            messagebox.showerror("Error", f"KeyError: {e}")

    def clear_entries(self):
        for key, entry in self.entry_widgets.items():
            if isinstance(entry, tk.Text):
                entry.delete("1.0", tk.END)
            else:
                entry.delete(0, tk.END)

    def switch_frame(self, new_frame):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    def submit_machine_info(self):
        machine_number = self.machine_number_entry.get()
        date = self.date_entry.get()
        if machine_number and date:
            self.LYB_OperationBrain(self.machine_info_frame.role, machine_number, date)
        else:
            messagebox.showwarning("Input Error", "Please enter both machine number and date.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LYBOperationBrainApp(root)
    root.mainloop()