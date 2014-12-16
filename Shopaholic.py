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

      B_NEW = Tkinter.Button(master, text ="NEW ORDER", width=30, height=3, font=100, command = self.addTask)
      B_EDIT = Tkinter.Button(master, text ="DELETE ORDER", width=30, height=3, font=100, command = self.Delete)
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
      self.translist.append([self.e1.get(),self.e2.get(),self.e3.get(),float(value)])
      tkMessageBox.showinfo( "Total Pay!" , str(value) + " THB\n" +"Total pay : "+str(sum(self.paylist))+" THB\n"+"Now you got "+ str(len(self.paylist))+" Order!")
      
   def showList(self):
      tkMessageBox.showinfo( "Total Pay!" , str(sum(self.paylist)) + " THB\n" + "Your Pay List : " + str(self.paylist) )

  

   def Delete(self):
       
      def whichSelected () :
            print "At %s of %d" % (select.curselection(), len(self.translist))
            return int(select.curselection()[0])

      def deleteEntry() :
            del self.translist[whichSelected()]
            del self.paylist[whichSelected()]

            setSelect ()

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

window = App(master)

# start the event loop
master.mainloop()
