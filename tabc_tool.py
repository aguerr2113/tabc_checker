import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("TABC License's")
window.geometry('960x720')
window.configure(bg='#0d1117')

#---------------------------------------------------------------------------------
# container
top_frame = ttk.Frame(window, padding=(20,14,20,0))
top_frame.pack(fill='x')


header = ttk.Label(top_frame, text='TABC License Fetcher',font=('Segoe UI', 14, 'bold'), foreground='#58a6ff',background='#0d1117')
 
header.pack(side='left')

#---------------------------------------------------------------------------------
token_var = tk.StringVar(value='')
token_frame = ttk.Frame(window,padding=(20,6,20,0))
token_frame.pack(fill='x')

ttk.Label(token_frame,textvariable=token_var,width=40).pack(side='left',padx=8)

#---------------------------------------------------------------------------------
btn_frame = ttk.Frame(window,padding = (20,10,20,0))
btn_frame.pack(fill='x')
#---------------------------------------------------------------------------------
def on_fetch_click():
    token = token_var.get()
    print(f'Fetch clicked! Token = {token}')

fetch_btn = ttk.Button(btn_frame, text='Fetch TABC Data',command=on_fetch_click)
fetch_btn.pack(side='left')

#---------------------------------------------------------------------------------
window.mainloop()