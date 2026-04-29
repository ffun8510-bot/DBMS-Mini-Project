#Frontend

from tkinter import *
import tkinter.messagebox
import MiniProject_Backend
from tkinter import ttk

class Movie:
	def __init__(self, root):
		self.root=root
		self.root.title("Online Movie Ticket Booking System")
		self.root.geometry("1600x800+0+0")
		self.root.resizable(True, True)
		self.root.config(bg="black")

		# Style for Treeview
		style = ttk.Style()
		try:
			style.theme_use('clam')
		except:
			pass
		style.configure("Treeview", background="black", foreground="white", fieldbackground="black", bordercolor="black", lightcolor="black", darkcolor="black")
		style.configure("Treeview.Heading", background="black", foreground="orange", bordercolor="black")
		style.map("Treeview", background=[('selected', 'orange')])
		style.configure("TScrollbar", background="black", troughcolor="black", bordercolor="black", arrowcolor="white")

		self.Movie_Name=StringVar()
		self.Movie_ID=StringVar()
		self.Release_Date=StringVar()
		self.Director=StringVar()
		self.Cast=StringVar()
		self.Budget=StringVar()
		self.Duration=StringVar()
		self.Rating=StringVar()
		self.rows = []
		self.sd = None

		#Fuctions
		def iExit():
			iExit=tkinter.messagebox.askyesno("Online Movie Ticket Booking System", "Are you sure???")
			if iExit>0:
				root.destroy()
			return

		def clcdata():
			self.txtMovie_ID.delete(0,END)
			self.txtMovie_Name.delete(0,END)
			self.txtRelease_Date.delete(0,END)
			self.txtDirector.delete(0,END)
			self.txtCast.delete(0,END)
			self.txtBudget.delete(0,END)
			self.txtRating.delete(0,END)
			self.txtDuration.delete(0,END)

		def adddata():
			if(len(self.Movie_ID.get())!=0):
				MiniProject_Backend.AddMovieRec(self.Movie_ID.get(),self.Movie_Name.get(),self.Release_Date.get(),self.Director.get(),self.Cast.get(),self.Budget.get(),self.Duration.get(),self.Rating.get())
				tree.delete(*tree.get_children())
				disdata()

		def disdata():
			tree.delete(*tree.get_children())
			self.rows = MiniProject_Backend.ViewMovieData()
			for row in self.rows:
				tree.insert('', 'end', values=row)

		def movierec(event):
			if tree.selection():
				item = tree.selection()[0]
				self.sd = tree.item(item, 'values')

				self.txtMovie_ID.delete(0,END)
				self.txtMovie_ID.insert(END,self.sd[1])
				self.txtMovie_Name.delete(0,END)
				self.txtMovie_Name.insert(END,self.sd[2])
				self.txtRelease_Date.delete(0,END)
				self.txtRelease_Date.insert(END,self.sd[3])
				self.txtDirector.delete(0,END)
				self.txtDirector.insert(END,self.sd[4])
				self.txtCast.delete(0,END)
				self.txtCast.insert(END,self.sd[5])
				self.txtBudget.delete(0,END)
				self.txtBudget.insert(END,self.sd[6])
				self.txtDuration.delete(0,END)
				self.txtDuration.insert(END,self.sd[7])
				self.txtRating.delete(0,END)
				self.txtRating.insert(END,self.sd[8])

		def deldata():
			if self.sd and len(self.Movie_ID.get())!=0:
				MiniProject_Backend.DeleteMovieRec(self.sd[0])
				clcdata()
				disdata()

		def searchdb():
			tree.delete(*tree.get_children())
			self.rows = MiniProject_Backend.SearchMovieData(self.Movie_ID.get(),self.Movie_Name.get(),self.Release_Date.get(),self.Director.get(),self.Cast.get(),self.Budget.get(),self.Duration.get(),self.Rating.get())
			for row in self.rows:
				tree.insert('', 'end', values=row)

		def updata():
			if self.sd and len(self.Movie_ID.get())!=0:
				MiniProject_Backend.UpdateMovieData(self.sd[0], self.Movie_ID.get(),self.Movie_Name.get(),self.Release_Date.get(),self.Director.get(),self.Cast.get(),self.Budget.get(),self.Duration.get(),self.Rating.get())
				tree.delete(*tree.get_children())
				disdata()

		#Frames
		MainFrame=Frame(self.root, bg="black")
		MainFrame.grid(sticky='nsew')
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_columnconfigure(0, weight=1)

		TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
		TFrame.grid(row=0, column=0, sticky='ew')

		DFrame=Frame(MainFrame, bd=2, padx=20, pady=10, bg="black", relief=RIDGE)
		DFrame.grid(row=1, column=0, sticky='nsew')
		MainFrame.grid_rowconfigure(1, weight=1)
		MainFrame.grid_columnconfigure(0, weight=1)

		BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
		BFrame.grid(row=2, column=0, sticky='ew')

		DFrameL=LabelFrame(DFrame, bd=2, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Movie Info_\n", fg="white")
		DFrameL.grid(row=0, column=0, sticky='nsew')

		DFrameR=LabelFrame(DFrame, bd=2, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Movie Details_\n", fg="white")
		DFrameR.grid(row=0, column=1, sticky='nsew')
		DFrame.grid_rowconfigure(0, weight=1)
		DFrame.grid_columnconfigure(0, weight=1)
		DFrame.grid_columnconfigure(1, weight=1)

		#Labels & Entry Box

		self.lblMovie_ID=Label(DFrameL, font=('Arial', 18, 'bold'), text="Movie ID:", padx=2, pady=2, bg="black", fg="orange")
		self.lblMovie_ID.grid(row=0, column=0, sticky=W)
		self.txtMovie_ID=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Movie_ID, width=39, bg="black", fg="white")
		self.txtMovie_ID.grid(row=0, column=1) 

		self.lblMovie_Name=Label(DFrameL, font=('Arial', 18, 'bold'), text="Movie Name:", padx=2, pady=2, bg="black", fg="orange")
		self.lblMovie_Name.grid(row=1, column=0, sticky=W) 
		self.txtMovie_Name=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Movie_Name, width=39, bg="black", fg="white")
		self.txtMovie_Name.grid(row=1, column=1)

		self.lblRelease_Date=Label(DFrameL, font=('Arial', 18, 'bold'), text="Release Date:", padx=2, pady=2, bg="black", fg="orange")
		self.lblRelease_Date.grid(row=2, column=0, sticky=W) 
		self.txtRelease_Date=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Release_Date, width=39, bg="black", fg="white")
		self.txtRelease_Date.grid(row=2, column=1)

		self.lblDirector=Label(DFrameL, font=('Arial', 18, 'bold'), text="Director:", padx=2, pady=2, bg="black", fg="orange")
		self.lblDirector.grid(row=3, column=0, sticky=W) 
		self.txtDirector=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Director, width=39, bg="black", fg="white")
		self.txtDirector.grid(row=3, column=1)

		self.lblCast=Label(DFrameL, font=('Arial', 18, 'bold'), text="Cast:", padx=2, pady=2, bg="black", fg="orange")
		self.lblCast.grid(row=4, column=0, sticky=W) 
		self.txtCast=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Cast, width=39, bg="black", fg="white")
		self.txtCast.grid(row=4, column=1)

		self.lblBudget=Label(DFrameL, font=('Arial', 18, 'bold'), text="Budget (Crores INR):", padx=2, pady=2, bg="black", fg="orange")
		self.lblBudget.grid(row=5, column=0, sticky=W) 
		self.txtBudget=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Budget, width=39, bg="black", fg="white")
		self.txtBudget.grid(row=5, column=1)

		self.lblDuration=Label(DFrameL, font=('Arial', 18, 'bold'), text="Duration (Hrs):", padx=2, pady=2, bg="black", fg="orange")
		self.lblDuration.grid(row=6, column=0, sticky=W) 
		self.txtDuration=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Duration, width=39, bg="black", fg="white")
		self.txtDuration.grid(row=6, column=1)

		self.lblRating=Label(DFrameL, font=('Arial', 18, 'bold'), text="Rating (Out of 5):", padx=2, pady=2, bg="black", fg="orange")
		self.lblRating.grid(row=7, column=0, sticky=W) 
		self.txtRating=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=self.Rating, width=39, bg="black", fg="white")
		self.txtRating.grid(row=7, column=1)

		#Treeview & ScrollBars
		tree = ttk.Treeview(DFrameR, columns=('ID', 'Movie_ID', 'Movie_Name', 'Release_Date', 'Director', 'Cast', 'Budget', 'Duration', 'Rating'), show='headings', height=16)
		tree.heading('ID', text='ID')
		tree.heading('Movie_ID', text='Movie ID')
		tree.heading('Movie_Name', text='Movie Name')
		tree.heading('Release_Date', text='Release Date')
		tree.heading('Director', text='Director')
		tree.heading('Cast', text='Cast')
		tree.heading('Budget', text='Budget')
		tree.heading('Duration', text='Duration')
		tree.heading('Rating', text='Rating')
		tree.column('ID', width=30)
		tree.column('Movie_ID', width=80)
		tree.column('Movie_Name', width=200)
		tree.column('Release_Date', width=100)
		tree.column('Director', width=150)
		tree.column('Cast', width=200)
		tree.column('Budget', width=80)
		tree.column('Duration', width=80)
		tree.column('Rating', width=80)
		vsb = ttk.Scrollbar(DFrameR, orient="vertical", command=tree.yview)
		hsb = ttk.Scrollbar(DFrameR, orient="horizontal", command=tree.xview)
		tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree.grid(row=0, column=0, sticky='nsew')
		vsb.grid(row=0, column=1, sticky='ns')
		hsb.grid(row=1, column=0, sticky='ew')
		DFrameR.grid_rowconfigure(0, weight=1)
		DFrameR.grid_columnconfigure(0, weight=1)
		tree.bind('<<TreeviewSelect>>', movierec)

		#Buttons
		self.btnadd=Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=adddata)
		self.btnadd.grid(row=0, column=0)

		self.btndis=Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=disdata)
		self.btndis.grid(row=0, column=1)

		self.btnclc=Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=clcdata)
		self.btnclc.grid(row=0, column=2)

		self.btnse=Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=searchdb)
		self.btnse.grid(row=0, column=3)

		self.btndel=Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=deldata)
		self.btndel.grid(row=0, column=4)

		self.btnup=Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=updata)
		self.btnup.grid(row=0, column=5)

		self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=iExit)
		self.btnx.grid(row=0, column=6)

		# Load data on startup
		MiniProject_Backend.MovieData()
		disdata()


if __name__=='__main__':
	root=Tk()
	datbase=Movie(root)
	root.mainloop()