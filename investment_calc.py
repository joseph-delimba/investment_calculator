import tkinter as tk
import numpy_financial as npf
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import mplcursors

root = tk.Tk()
root.title("Investment Calculator")
root.geometry("750x550") #(widthxheight)

# Default values to populate the initial total and graph
DEFAULT_YEARS = '10'
DEFAULT_INIT_INV = '10000'
DEFAULT_RATE = '0.07'
DEFAULT_CONT_AMNT = '2000'
DEFAULT_FINAL = npf.fv(float(DEFAULT_RATE),int(DEFAULT_YEARS),-(int(DEFAULT_CONT_AMNT)*12),-int(DEFAULT_INIT_INV))

# String variables for the investment information and final amount label
years_to_save = tk.StringVar()
initial_investment = tk.StringVar()
rate_of_return = tk.StringVar()
contribution_amount = tk.StringVar()
final_total = tk.StringVar()
final_total.set(f'${DEFAULT_FINAL:,.2f}')

labels = [] #years
data = [] #dollar amount

# Calculates the investment fund total and sets the final label
def calculate():
    labels.clear()
    data.clear()
    try:
        years = float(years_to_save.get())
        init_inv = float(initial_investment.get())
        rate = float(rate_of_return.get())
        cont = float(contribution_amount.get())
        final = npf.fv(rate,years,-cont*12,-init_inv)
        final_total.set(f"${final:,.2f}")
        for x in range(int(years)):
            labels.append(x+1)
            data.append(npf.fv(rate,x+1,-cont*12,-init_inv))
        update_graph(data,labels)
    except:
        final_total.set("Error! Please check your input.")
    return 0

# Top and bottom frames for the design of the GUI
top_frame = tk.Frame(root, height=100)
top_frame.pack(side=tk.TOP, fill=tk.X)

bottom_frame = tk.Frame(root, height=500)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Years to save label and entry box
years_label = tk.Label(top_frame, text="Years to Save: ")
years_entry = tk.Entry(top_frame, textvariable=years_to_save, width=50)
years_entry.insert(0, DEFAULT_YEARS)

# Initial investment label and entry box
init_investment_label = tk.Label(top_frame, text="Initial Investment: ")
init_investment_entry = tk.Entry(top_frame, textvariable=initial_investment, width=50)
init_investment_entry.insert(0, DEFAULT_INIT_INV)

# Rate of return label and entry box (decimal not %, default value of 0.07)
rate_label = tk.Label(top_frame, text="Rate of Return: ")
rate_entry = tk.Entry(top_frame, textvariable=rate_of_return, width=50)
rate_entry.insert(0, DEFAULT_RATE)

# Monthly contribution label and entry box
contribution_label = tk.Label(top_frame, text="Monthly Contribution: ")
contribution_entry = tk.Entry(top_frame, textvariable=contribution_amount, width=50)
contribution_entry.insert(0,DEFAULT_CONT_AMNT)

# Submit button to run the calculation
submit_btn = tk.Button(top_frame, text="Submit", command=calculate)

# Final investment fund label
final_label = tk.Label(top_frame, textvariable=final_total)

# Create figure and subplot for bar graph
fig = Figure()
ax = fig.add_subplot(111)

# Create canvas and place in GUI
canvas = FigureCanvasTkAgg(fig, master=bottom_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Function to update the bar graph using given data and labels lists
def update_graph(data, labels):
    ax.clear()
    ax.bar(labels, data)
    ax.set_ylabel('Total Value ($)')
    ax.set_xlabel('Year')
    ax.set_title('Investment Growth')
    ax.set_xticks(labels)
    cursor = mplcursors.cursor(ax, hover=mplcursors.HoverMode.Transient)
    cursor.connect(
        "add", lambda sel: sel.annotation.set_text(f'${data[sel.index]:,.2f}'))
    canvas.draw()

# Create the graph to populate the intial frame using default values
for x in range(int(DEFAULT_YEARS)):
    labels.append(x+1)
    data.append(npf.fv(float(DEFAULT_RATE),x+1,-(int(DEFAULT_CONT_AMNT)*12),-int(DEFAULT_INIT_INV)))

update_graph(data,labels)

# Placing all the elements used the grid method
years_label.grid(row=0,column=0)
years_entry.grid(row=0,column=1)
init_investment_label.grid(row=1,column=0)
init_investment_entry.grid(row=1,column=1)
rate_label.grid(row=2,column=0)
rate_entry.grid(row=2,column=1)
contribution_label.grid(row=3,column=0)
contribution_entry.grid(row=3,column=1)
submit_btn.grid(row=4,column=0)
final_label.grid(row=4,column=1)

root.mainloop()