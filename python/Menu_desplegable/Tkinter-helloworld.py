import tkinter as tk
RIDGE=0
BOTH=0
BOTTOM=0
button=tk.Pack()
frame = tk.Frame(tk, relief=RIDGE, borderwidth=2) 
frame.pack(fill= BOTH,expand=1) 
label = tk.Label(frame, text="Hello, World") 
label.pack(fill= tk.X, expand=1) 
tk.Button(frame,text="Exit",command= tk.DISABLED) 
button.pack(side=BOTTOM) 
tk.mainloop()