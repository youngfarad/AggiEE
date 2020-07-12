import tkinter as tk

class GUI(tk.Frame):
	def __init__(self, x, y, master):
		super().__init__(master)
		self.master = master
		master.title("AggiEE")
		self.generate_grid(x,y)
		self.pack()
		self.buttons = {}
		self.labels = {}
		self.entries = {}

	def generate_grid(self, x, y):
		self.frames = []
		for i in range(x):
			self.columnconfigure(i, weight=1, minsize=75)
			self.rowconfigure(i, weight=1, minsize=50)
			lst = []
			for j in range(y):
				frame = tk.Frame(
					master=self,
					borderwidth=1
				)
				frame.grid(row=i, column=j, padx=5, pady=5)
				lst.append(frame)
				#label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
				#label.pack(padx=5, pady=5)
			self.frames.append(lst)

	def create_button(self, text, loc, size=(25,2), func=None):
		x = loc[0]
		y = loc[1]
		btn = tk.Button(
			master=self.frames[y][x],
			text=text,
			command=func,
			width=size[0],
			height=size[1]
		)
		btn.pack()
		self.buttons[loc] = btn

	def create_label(self, text, loc):
		x = loc[0]
		y = loc[1]
		lb = tk.Label(
			master=self.frames[y][x],
			text=text
		)
		lb.pack()
		self.labels[loc] = lb

	def create_entry(self, loc):
		x = loc[0]
		y = loc[1]
		ent = tk.Entry(
			master=self.frames[y][x]
		)
		ent.pack()
		self.entries[loc] = ent

gui = GUI(5,5,tk.Tk())
gui.create_label("Enter your name:", (0,0))
gui.create_entry((1,0))
gui.create_button("Enter", (0,1), func=lambda: print("Your name is: %s" %gui.entries[(1,0)].get()))
gui.mainloop()