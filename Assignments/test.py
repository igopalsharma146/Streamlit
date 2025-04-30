import tkinter as tk
from tkcalendar import Calendar

def get_date():
    selected_date = cal.get_date()
    print("User selected date:", selected_date)

# Main window
root = tk.Tk()
root.title("Select a Date")

# Calendar widget
cal = Calendar(root, selectmode="day", year=2025, month=4, day=30)
cal.pack(pady=20)

# Button to confirm selection
btn = tk.Button(root, text="Confirm Date", command=get_date)
btn.pack()

root.mainloop()