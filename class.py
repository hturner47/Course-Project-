from tkinter import*
import tkinter as tk
root = tk.Tk()
root.geometry("400x400")
root.title("StartPage")
root.mainloop()

class WindowOne():
    def __init__(self):
        window1 = tk.Toplevel(root)
        window1.title("Window 1")
        
        def create_labels(self):
            label1 = tk.Label(window1, text="Click or unclick the checkboxes to select your answer then hit the ""NEXT"" button to continue or the ""BACK"" button to go back to the previous page.")
            label1.pack()
            label2 = tk.Label(window1, text= "Enjoy the program")
            label2.pack()
            label3 = tk.Label(window1, text="Question: How are you doing?")
            label3.pack(side = "top")
            label3 = tk.Label(window1, text="Question: Have you had breakfast yet?")
            label3.pack(side = "top")
            label3 = tk.Label(window1, text="Question: Do you have any plans today?")
            label3.pack(side = "top")
            
        def create_checkbuttons(self):
# create the window 1 check buttons and set its properties
            checkbutton3 = tk.Checkbutton(window1, text="Good")
            checkbutton3.pack()
            checkbutton4 = tk.Checkbutton(window1, text="meh")
            checkbutton4.pack()
            checkbutton5 = tk.Checkbutton(window1, text="Bad")
            checkbutton5.pack()
            checkbutton3 = tk.Checkbutton(window1, text="yes")
            checkbutton3.pack()
            checkbutton4 = tk.Checkbutton(window1, text="no")
            checkbutton4.pack()
            checkbutton3 = tk.Checkbutton(window1, text="yes")
            checkbutton3.pack()
            checkbutton4 = tk.Checkbutton(window1, text="no")
            checkbutton4.pack()
class Windowtwo():
    def __init__(self):
        window2 = tk.Toplevel(root)
        window2.title("Window 2")
        
        def labelstwo(slef):
        # create the labels and Check buttons for window 2
            label2 = tk.Label(window2, text="Click the EXIT button to exit the program or the BACK button to go back.")
            label2.pack()
            label2 = tk.Label(window2, text="Question: Did you enjoy the program?")
            label2.pack()
        def chaeckbuttonsTwo(slef):
            checkbutton2 = tk.Checkbutton(window2, text="yes")
            checkbutton2.pack()
            checkbutton5 = tk.Checkbutton(window2, text="yes")
            checkbutton5.pack()
class root():
    def windows(self):
      window1 = tk.Toplevel(root)
      window1.title("Window 1")
      window2 = tk.Toplevel(root)
      window2.title("Window 2")
      
      def rootlabels(self):
            label1 = tk.Label(root, text="Click the START button to begin.")
            label1.pack()
        
        def buttons(self):
            # create the buttons for page 1
            button1 = tk.Button(window1, text="NEXT", command=window2)
            button1.pack()
            button2 = tk.Button(window1, text="BACK", command=root)
            button2.pack()
            button3 = tk.Button(window1, text="EXIT", command=window1.quit)
            button3.pack()
# create the buttons for page 2
            button4 = tk.Button(window2, text="BACK", command=window1)
            button4.pack()
            button5 = tk.Button(window2, text="EXIT", command=window2.quit)
            button5.pack()
# create the buttons for starter page
            button6 = tk.Button(root, text="START", command=window1)
            button6.pack()

# create the exit button and set its properties
            exit_button = tk.Button(root, text="EXIT", command=root.quit)
            exit_button.pack()
#create images
def image(filename = "image1.png"):
    image1 = Image(root,text= "smileyface")
    print("Close the image window to continue. ")
    image1.draw()


def image(filename = "image2.png"):
    image1 = Image(root,text= "congratulations")
    print("Close the image window to continue. ")
    image1.draw()

root.mainloop