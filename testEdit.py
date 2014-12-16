from Tkinter import *

translist = [
  [110000, 1100, 10, 10],
  [120000, 2000, 10, 20],
  [200000, 5000, 20, 20],
]

def whichSelected () :
            print "At %s of %d" % (select.curselection(), len(translist))
            return int(select.curselection()[0])

def updateEntry() :
            translist[whichSelected()] = [totalVar.get(), priceVar.get(), discountVar.get(), quantityVar.get()]
            setSelect ()

def deleteEntry() :
            del translist[whichSelected()]
            setSelect ()

def loadEntry  () :
            total, price, discount, quantity = translist[whichSelected()]
            totalVar.set(total)
            priceVar.set(price)
            discountVar.set(discount)
            quantityVar.set(quantity)

def makeWindow () :
            global totalVar, priceVar, discountVar,  quantityVar, select
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

            Label(frame1, text="Total:").grid(row=3, column=0, sticky=W)
            totalVar= StringVar()
            total= Entry(frame1, textvariable=totalVar, state = DISABLED)
            total.grid(row=3, column=1, sticky=W)

            frame2 = Frame(win)       
            frame2.pack()
            b2 = Button(frame2,text="Update",command=updateEntry)
            b3 = Button(frame2,text="Delete",command=deleteEntry)
            b4 = Button(frame2,text=" Load ",command=loadEntry)
            b2.pack(side=LEFT)
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
    translist.sort()
    select.delete(0,END)
    for price in translist :
        select.insert (END, price)

win = makeWindow()
setSelect ()
win.mainloop()
