from tkinter import*
from breezypythongui import*
from breezypythongui import tkinter.Frame
root = Tk()
root.geometry("400x600")
w = Label(root, text ='GeeksForGeeks', font = "50") 
w.pack()
class Checkbutton(EasyFrame):
 
    #Allows user to place order from available options.
    def __init__(self):
        EasyFrame.__init__(self, "School Supplies")
        
    #add check buttons
        self.note = self.addCheckbutton(text = "Notebook", row = 0, column = 0)
        self.pens = self.addCheckbutton(text = "Pens", row = 0 , column = 1)  
        self.pen = self.addCheckbutton(text = "Pencils", row = 1, column = 1)
        self.lap = self.addCheckbutton(text = "Laptop", row = 1, column = 0)
    
    #command button
        self.addButton(text = "Place order", row = 2, column = 0, columnspan = 2, command = self.placeOrder)
    
#event handling
def placeOrder(self):
    message = ""
    if self.note.isChecked():
        message +="Notebook\n\n"
    if self.pens.isChecked():
        message +="Pens\n\n"
    if self.pen.isChecked():
        message +="Pencils\n\n"
    if self.lap.isChecked():
        message +="Laptop\n\n"
    if message =="": message = "Cart is empty!"
    self.messageBox(title = "Shopping Cart", message = message)

mainloop()
