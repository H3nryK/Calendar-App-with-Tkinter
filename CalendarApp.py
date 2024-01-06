import calendar
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        
        self.selected_date = tk.StringVar()
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        
        self.create_widgets()
        
    def create_widgets(self):
        #Frame for calendar
        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack(pady=10)
        
        #Header frame
        header_frame = ttk.Frame(self.calendar_frame)
        header_frame.grid(row=0, column=0, columnspan=7)
        
        #Month and year labels
        self.month_label = ttk.Label(header_frame, text="", font=("Helvetica", 16))
        self.month_label.grid(row=0, column=1, padx=10)
        
        #Previous and next buttons
        ttk.Button(header_frame, text="Prev", command=self.prev_month).grid(row=0, column=0, padx=10)
        ttk.Button(header_frame, text="Next", command=self.next_month).grid(row=0, column=2, padx=10)
        
        #calendar
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.populate_calendar()
    
    def populate_calendar(self):
        year, month = self.get_current_date()
        month_calendar = self.cal.monthdayscalendar(year, month)
        
        # Update month label
        month_name = calendar.month_name[month]
        self.month_label.config(text=f"{month_name} {year}")
        
        # Clear existing widgets in the calendar frame
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
            
        # Month Label
        ttk.Label(self.calendar_frame, text=f"{month_name} {year}", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=7)
            
        # Weekly labels
        for day_num, day in enumerate(calendar.day_name):
            ttk.Label(self.calendar_frame, text=day[:3], font=("Helvetica", 10)).grid(row=1, column=day_num)
            
        # Calendar days
        for week_num, week in enumerate(month_calendar, start=2):
            for day_num, day in enumerate(week):
                if day != 0:
                    day_button = ttk.Button(self.calendar_frame, text=str(day), command=lambda d=day: self.select_date(d))
                    day_button.grid(row=week_num, column=day_num)
    
    def prev_month(self):
        year, month = self.get_current_date()
        new_month = month - 1 if month > 1 else 12
        new_year = year - 1 if month == 1 else year
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.populate_calendar() 
    
    def next_month(self):
        year, month = self.get_current_date()
        new_month = month + 1 if month < 12 else 1
        new_year = year + 1 if month == 12 else year
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.populate_calendar()
        
    def get_current_date(self):
        now = datetime.now()
        return now.year, now.month
    
    def select_date(self, day):
        year, month = self.get_current_date()
        selected_date = f"{year}-{month:02d}-{day:02d}"
        self.selected_date.set(selected_date)
        print(f"Selected Date: {selected_date}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()