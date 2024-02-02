import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import pandas as pd

def calculate_wage():
    try:
        hours_worked = float(hours_entry.get())
        hourly_rate = float(rate_entry.get())
        week_number = int(week_entry.get())
        week_start = start_date_var.get()
        week_end = end_date_var.get()
        invoice_number = invoice_entry.get()

        wage = hours_worked * hourly_rate

        # Calculate amounts based on percentages
        expenditure = wage * 0.5
        savings = wage * 0.2
        investment = wage * 0.1
        tax = wage * 0.1

        # You can customize the file path and format as needed
        file_path = "wage_data.csv"

        # Read existing data from file, or create a new DataFrame if the file doesn't exist
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['WeekNumber', 'StartDate', 'EndDate', 'InvoiceNumber', 
                                       'HoursWorked', 'HourlyRate', 'Wage', 'Expenditure', 'Savings', 'Investment', 'Tax'])

        # Append new data to DataFrame
        new_entry = {'WeekNumber': week_number, 'StartDate': week_start, 'EndDate': week_end,
                     'InvoiceNumber': invoice_number, 'HoursWorked': hours_worked,
                     'HourlyRate': hourly_rate, 'Wage': wage,
                     'Expenditure': expenditure, 'Savings': savings, 'Investment': investment, 'Tax': tax}
        df = df.append(new_entry, ignore_index=True)

        # Save DataFrame to file
        df.to_csv(file_path, index=False)

        result_label.config(text=f'Wage calculated and stored for Week {week_number}!\n'
                                 f'Expenditure: ${expenditure:.2f}\n'
                                 f'Savings: ${savings:.2f}\n'
                                 f'Investment: ${investment:.2f}\n'
                                 f'Tax: ${tax:.2f}\n'
                                 f'Total Wage: ${wage:.2f}')
    except ValueError:
        tk.messagebox.showerror("Error", "Invalid input. Please enter valid numerical values.")

# GUI setup
root = tk.Tk()
root.title("Wage Calculator")

# Labels
tk.Label(root, text="Hours Worked:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
tk.Label(root, text="Hourly Rate:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
tk.Label(root, text="Week Number:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
tk.Label(root, text="Week Start Date:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
tk.Label(root, text="Week End Date:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
tk.Label(root, text="Invoice Number:").grid(row=5, column=0, padx=5, pady=5, sticky='e')

# Entry Widgets
hours_entry = tk.Entry(root)
rate_entry = tk.Entry(root)
week_entry = tk.Entry(root)

# Using DateEntry widget for date selection
start_date_var = tk.StringVar()
start_date_entry = DateEntry(root, textvariable=start_date_var, date_pattern='yyyy-mm-dd')
end_date_var = tk.StringVar()
end_date_entry = DateEntry(root, textvariable=end_date_var, date_pattern='yyyy-mm-dd')

invoice_entry = tk.Entry(root)

# Placing Entry Widgets
hours_entry.grid(row=0, column=1, padx=5, pady=5)
rate_entry.grid(row=1, column=1, padx=5, pady=5)
week_entry.grid(row=2, column=1, padx=5, pady=5)
start_date_entry.grid(row=3, column=1, padx=5, pady=5)
end_date_entry.grid(row=4, column=1, padx=5, pady=5)
invoice_entry.grid(row=5, column=1, padx=5, pady=5)

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate Wage", command=calculate_wage)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()
