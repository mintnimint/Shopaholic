import Tkinter
import tkMessageBox
from Tkinter import *

master = Tk()

class App:
    
   paylist = []
   translist = []
   value = 0
   total = 0
   
   def __init__(self,master):
      master.minsize(width=200, height=250)


      B_NEW = Tkinter.Button(master, text ="NEW", width=30, height=3, font=100, command = self.addTask)
      B_EDIT = Tkinter.Button(master, text ="EDIT", width=30, height=3, font=100, command = self.Delete)
      B_RESULT = Tkinter.Button(master, text ="CHECK TOTAL", width=30, font=100, height=3, command = self.showList)
      B_EXIT = Tkinter.Button(master, text ="EXIT", width=30, height=3, font=100, command = master.destroy)

      B_NEW.pack()
      B_EDIT.pack()
      B_RESULT.pack()
      B_EXIT.pack()


   def addTask(self):
      
      master = Tk()
                             
      Label(master, text="PRODUCT PRICE :").grid(row=0)
      Label(master, text="DISCOUNT(%) :").grid(row=1)
      Label(master, text="QUANTITY :").grid(row=2)

      e1 = Entry(master)
      e2 = Entry(master)
      e3 = Entry(master)

      self.e1 = e1
      self.e2 = e2
      self.e3 = e3

      e1.grid(row=0, column=1)
      e2.grid(row=1, column=1)
      e3.grid(row=2, column=1)
      

      Button(master, text='ADD', command=self.showResult).grid(row=3, column=0, sticky=W, pady=4)
      Button(master, text='CANCEL', command=master.destroy).grid(row=3, column=1, sticky=W, pady=4)
 
   def showResult(self):
      value = (float(self.e1.get()) -(float(self.e1.get()) * float(self.e2.get())/100.0)) * float(self.e3.get())
      self.paylist.append(float(value))
      self.translist.append([float(value),self.e1.get(),self.e2.get(),self.e3.get()])
      tkMessageBox.showinfo( "Total Pay!" , str(value) + " THB\n" +"Total pay : "+str(sum(self.paylist))+" THB\n"+"Now you got "+ str(len(self.paylist))+" Order!")

window = App(master)

# start the event loop
master.mainloop()
