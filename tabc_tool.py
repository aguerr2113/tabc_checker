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
window.mainloop()