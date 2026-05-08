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
record_count_var = tk.StringVar(value='No data loaded.')
status_bar = ttk.Frame(window, padding = (20,4))
status_bar.pack(fill='x',side='bottom')
ttk.Label(status_bar,textvariable=record_count_var).pack(side='left')
#---------------------------------------------------------------------------------
table_frame = ttk.Frame(window, padding=(20, 10, 20, 10))
table_frame.pack(fill='both', expand=True)

columns = ('license_id', 'primary_status', 'secondary_status', 'expiration_date')
tree = ttk.Treeview(table_frame, columns=columns, show='headings')

tree.heading('license_id',   	text='License ID')
tree.heading('primary_status',   text='Primary Status')
tree.heading('secondary_status', text='Secondary Status')
tree.heading('expiration_date',  text='Expiration Date')

tree.column('license_id',   	width=100)
tree.column('primary_status',   width=130)
tree.column('secondary_status', width=160)
tree.column('expiration_date',  width=120)

vsb = ttk.Scrollbar(table_frame, orient='vertical',   command=tree.yview)
hsb = ttk.Scrollbar(table_frame, orient='horizontal', command=tree.xview)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.pack(side='left', fill='both', expand=True)
vsb.pack(side='right',  fill='y')
hsb.pack(side='bottom', fill='x')

#-------------------------------------Test rows-----------------------------------

tree.insert('', 'end', values=('100000001', 'Active',  '',           	'2026-12-31'))
tree.insert('', 'end', values=('100000002', 'Expired', '',               '2024-06-15'))
tree.insert('', 'end', values=('100000003', 'Active',  'Renewal Pending','2025-03-01'))
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
window.mainloop()