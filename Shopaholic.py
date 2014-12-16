import Tkinter
import tkMessageBox
from Tkinter import *

master = Tk()

class App:
    
   paylist = []
   translist = []
   value = 0
   total = 0

   ### MAIN WINDOW ##

   """ all fn in this class will call this function """
   def __init__(self,master):
      
      master.minsize(width=200, height=250)

      B_NEW = Tkinter.Button(master, text ="NEW ORDER", width=30, height=3, font=100, command = self.addTask) #to add order function
      B_EDIT = Tkinter.Button(master, text ="DELETE ORDER", width=30, height=3, font=100, command = self.Delete) #link to delete function
      B_RESULT = Tkinter.Button(master, text ="CHECK TOTAL", width=30, font=100, height=3, command = self.showList) #link to showlist function
      B_EXIT = Tkinter.Button(master, text ="EXIT", width=30, height=3, font=100, command = master.destroy) #close program

      B_NEW.pack()
      B_EDIT.pack()
      B_RESULT.pack()
      B_EXIT.pack()
      


   ### ADD ORDER ##
      
   """ add order function """
   def addTask(self):
      
      master = Tk()
                             
      Label(master, text="PRODUCT PRICE :").grid(row=0)
      Label(master, text="DISCOUNT(%) :").grid(row=1)
      Label(master, text="QUANTITY :").grid(row=2)

      entry1 = Entry(master)
      entry2 = Entry(master)
      entry3 = Entry(master)

      self.entry1 = entry1
      self.entry2 = entry2
      self.entry3 = entry3

      entry1.grid(row=0, column=1)
      entry2.grid(row=1, column=1)
      entry3.grid(row=2, column=1)
      

      Button(master, text='ADD', command=self.showResult).grid(row=3, column=0, sticky=W, pady=4)
      Button(master, text='CANCEL', command=master.destroy).grid(row=3, column=1, sticky=W, pady=4)


   """ when click 'ADD'(Button)in ADD ORDER(window) this message box will show to alert some information """
   def showResult(self):
      value = (float(self.entry1.get()) -(float(self.entry1.get()) * float(self.entry2.get())/100.0)) * float(self.entry3.get())
      self.paylist.append(float(value))
      self.translist.append([self.entry1.get(),self.entry2.get(),self.entry3.get(),float(value)])
      tkMessageBox.showinfo( "Total Pay!" , str(value) + " THB\n" +"Total pay : "+str(sum(self.paylist))+" THB\n"+"Now you got "+ str(len(self.paylist))+" Order!")



   ### CHECK TOTAL ##

   """ when click 'CHECK TOTAL'(Button)in Main(window) this message box will show to alert all information """
   def showList(self):
      tkMessageBox.showinfo( "Total Pay!" , "Your Total Pay is "+str(sum(self.paylist)) + " THB\n" + "Your Pay List : " + str(self.paylist)+"\n"+"Now you got "+ str(len(self.paylist))+" Order!" )



   ### DELETE ORDER ##

   """ delete order function """
   def Delete(self):
      
      """ show selected index that take action in python shell """
      def whichSelected () :
            print "At %s of %d" % (select.curselection(), len(self.translist))
            return int(select.curselection()[0])

      """ delete funtion """
      def deleteEntry() :
            del self.translist[whichSelected()]
            del self.paylist[whichSelected()]

            setSelect ()
            
      """ load entry funtion """
      def loadEntry  () :
            global price, discount, quantity, total
            price_s, discount_s, quantity_s, total_s = self.translist[whichSelected()]
            price.delete(0,END)
            price.insert(0,str(price_s))
            discount.delete(0,END)
            discount.insert(0,str(discount_s))
            quantity.delete(0,END)
            quantity.insert(0,str(quantity_s))
            total.delete(0,END)
            total.insert(0,str(total_s))

      """ main interface window of delete order function """
      def makeWindow():
            global price, discount, quantity, total
            global select
            win = Tk()

            frame1 = Frame(win)
            frame1.pack()
            
            Label(frame1, text="Price").grid(row=0, column=0, sticky=W)
            priceVar = StringVar()
            price = Entry(frame1, textvariable=priceVar)
            price.grid(row=0, column=1, sticky=W)

            Label(frame1, text="Discount").grid(row=1, column=0, sticky=W)
            discountVar= StringVar()
            discount= Entry(frame1, textvariable=discountVar)
            discount.grid(row=1, column=1, sticky=W)

            Label(frame1, text="Quantity").grid(row=2, column=0, sticky=W)
            quantityVar= StringVar()
            quantity= Entry(frame1, textvariable=quantityVar)
            quantity.grid(row=2, column=1, sticky=W)

            Label(frame1, text="Total").grid(row=3, column=0, sticky=W)
            totalVar= StringVar()
            total= Entry(frame1, textvariable=totalVar)
            total.grid(row=3, column=1, sticky=W)

            frame2 = Frame(win)       
            frame2.pack()
            b3 = Button(frame2,text="Delete",command=deleteEntry)
            b4 = Button(frame2,text=" Load ",command=loadEntry)
            b3.pack(side=LEFT); b4.pack(side=LEFT)

            frame3 = Frame(win)      
            frame3.pack()
            scroll = Scrollbar(frame3, orient=VERTICAL)
            select = Listbox(frame3, yscrollcommand=scroll.set, height=8)
            scroll.config (command=select.yview)
            scroll.pack(side=RIGHT, fill=Y)
            select.pack(side=LEFT,  fill=BOTH, expand=1)
            return win

      """ setselect action function """
      def setSelect () :
            self.translist.sort()
            select.delete(0,END)
            for element in self.translist :
               select.insert (END, element)

            self.paylist.sort()
            select.delete(0,END)
            for price in self.paylist :
               select.insert (END, price)

      win = makeWindow() 
      setSelect ()

window = App(master) #make main window
master.mainloop() # start the event loop

