import tkinter as tk
from tkinter import ttk

# create a ticker input
# create an api to grab data of the ticker
# create text box for prc_pur, shares, prc_sold
# -google what tkinter text boxes should take input
# create button to calculate
# create box to display result for profit
# -google what tkinter text boxes should display text
# create box to display result for profit


# create tkinter frame to hold everything

# prc_pur = float(input("Enter current trading price of the stock: "))
# shares = float(input("Enter the amount of shares you're buying: "))
# prc_sold = float(input("Enter the trading price of the stock at sale: "))


# def calculate():
#     value = prc_sold*shares
#     cost = prc_pur*shares

#     profit = value - cost

#     gain = (prc_sold - prc_pur/prc_pur) * 100  # for percentage gain
#     # profit =

#     return profit

# result = calculate()
# print(result)

window = tk.Tk()
window.title("Stock Gain Calculator")
window.resizable(width=False, height=False)
# hi
# window.geometry('{}x{}'.format(width, height))

# frame = tk.Frame(window, height=225, width=300, bg='black')
# frame.pack()

textbox = tk.Text(window, x=150, y=10)
textbox.place()

# button = tk.Frame(frame)
# button.pack()


window.mainloop()
