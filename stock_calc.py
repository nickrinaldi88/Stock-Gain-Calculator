import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
from bs4 import BeautifulSoup


height = 160
width = 500

window = tk.Tk()
window.title("Stock Gain Calculator")
window.resizable(width=False, height=False)

window.geometry(f'{width}x{height}')

# labels and string variables

pp_sv = tk.StringVar()
pp_sv.set('Purchase Price')
pp_label = tk.Label(window, textvariable=pp_sv)
pp_label.place(x=20, y=10)


share_sv = tk.StringVar()
share_sv.set("# of Shares")
share_label = tk.Label(window, textvariable=share_sv)
share_label.place(x=170, y=10)


sp_sv = tk.StringVar()
sp_sv.set("Sale Price")
sp_label = tk.Label(window, textvariable=sp_sv)
sp_label.place(x=20, y=60)


but_sv = tk.StringVar()
but_sv.set("Calculate")
but_label = tk.Label(window, textvariable=but_sv)
but_label.place(x=20, y=110)

res_sv = tk.StringVar()
res_sv.set("Total Profit: ")
result_label = tk.Label(window, textvariable=res_sv)
result_label.place(x=170, y=60)

result = tk.Label(window)
result.place(x=270, y=60)

clr_sv = tk.StringVar()
clr_sv.set("Clear")
clear_label = tk.Label(window, textvariable=clr_sv)
clear_label.place(x=170, y=110)

tick_sv = tk.StringVar()
tick_sv.set('Ticker')
tick_label = tk.Label(window, textvariable=tick_sv)
tick_label.place(x=320, y=10)


# input boxes

pp_box = tk.Text(window, height=2, width=4)
pp_box.place(x=120, y=10)

sp_box = tk.Text(window, height=2, width=4)
sp_box.place(x=120, y=60)

share_box = tk.Text(window, height=2, width=4)
share_box.place(x=270, y=10)

tick_box = tk.Text(window, height=2, width=4)
tick_box.place()


def calculate():
    # grab text values of all three boxes

    try:
        prc_pur = int(pp_box.get(1.0, "end-1c"))
        shares = int(share_box.get(1.0, "end-1c"))
        prc_sold = int(sp_box.get(1.0, "end-1c"))
    except ValueError:
        pass

    value = prc_sold*shares
    cost = prc_pur*shares

    profit = value - cost
    profit = "$" + str(profit)

    gain = (prc_sold - prc_pur/prc_pur) * 100  # for percentage gain

    result.config(text=profit)


def clear():
    pp_box.delete("1.0", "end")
    sp_box.delete("1.0", "end")
    share_box.delete("1.0", "end")


# ticker will be "get_text of ticker entry box"

def scrape(ticker):

    url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'

    # store webpage in variable

    html = urlopen(url)

    # convert webpage to soup object

    soup = BeautifulSoup(html, 'html.parser')

    price_elem = soup.find(
        'span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})

    price = price_elem.get_text()

    return price


# cur_price = scrape()

# print(cur_price)


# buttons


calc_button = tk.Button(window, height=2, width=4, command=calculate)
calc_button.place(x=120, y=110)

clear_button = tk.Button(window, height=2, width=4,
                         command=clear)  # command=clear function
clear_button.place(x=270, y=110)

window.mainloop()

# create ticker entry box
