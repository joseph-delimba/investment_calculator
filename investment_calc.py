import tkinter as tk
import numpy_financial as npf

root = tk.Tk()
root.title("Investment Calculator")
root.geometry("800x600") #(widthxheight)

# String variables for the investment information and final amount label
years_to_save = tk.StringVar()
initial_investment = tk.StringVar()
rate_of_return = tk.StringVar()
contribution_amount = tk.StringVar()
final_total = tk.StringVar()
final_total.set("N/A")

# Calculates the investment fund total and sets the final label
def calculate():
    years = float(years_to_save.get())
    init_inv = float(initial_investment.get())
    rate = float(rate_of_return.get())
    cont = float(contribution_amount.get())
    final = npf.fv(rate,years,-cont*12,-init_inv)
    final_total.set(f"${final:.2f}")
    return 0

# Years to save label and entry box
years_label = tk.Label(root, text="Years to Save: ")
years_entry = tk.Entry(root, textvariable=years_to_save, width=50)

# Initial investment label and entry box
init_investment_label = tk.Label(root, text="Initial Investment: ")
init_investment_entry = tk.Entry(root, textvariable=initial_investment, width=50)

# Rate of return label and entry box (decimal not %, default value of 0.07)
rate_label = tk.Label(root, text="Rate of Return: ")
rate_entry = tk.Entry(root, textvariable=rate_of_return, width=50)
rate_entry.insert(0, "0.07")

# Monthly contribution label and entry box
contribution_label = tk.Label(root, text="Monthly Contribution: ")
contribution_entry = tk.Entry(root, textvariable=contribution_amount, width=50)

# Submit button to run the calculation
submit_btn = tk.Button(root, text="Submit", command=calculate)

# Final investment fund label
final_label = tk.Label(root, textvariable=final_total)

# Placing all the elements used the grid method
years_label.grid(row=0,column=0)
years_entry.grid(row=0,column=1)
init_investment_label.grid(row=1,column=0)
init_investment_entry.grid(row=1,column=1)
rate_label.grid(row=2,column=0)
rate_entry.grid(row=2,column=1)
contribution_label.grid(row=3,column=0)
contribution_entry.grid(row=3,column=1)
submit_btn.grid(row=4,column=1)
final_label.grid(row=3,column=2)

root.mainloop()