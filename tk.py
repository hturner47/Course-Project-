import tkinter as tk

# Create the root window
root = tk.Tk()

# Create the first window and set its title
window1 = tk.Toplevel(root)
window1.title("Window 1")

# Create the second window and set its title
window2 = tk.Toplevel(root)
window2.title("Window 2")

# Create the first image and place it in window 1
image1 = tk.PhotoImage(file="image1.png")
label1 = tk.Label(window1, image=image1)
label1.pack(side="top")

# Create the second image and place it in window 2
image2 = tk.PhotoImage(file="image2.png")
label2 = tk.Label(window2, image=image2)
label2.pack(side="top")

# Create the first label and place it in the root window
label3 = tk.Label(root, text="This is label 1")
label3.pack(side="top")

# Create the second label and place it in the root window
label4 = tk.Label(root, text="This is label 2")
label4.pack(side="top")

# Create the third label and place it in the root window
label5 = tk.Label(root, text="This is label 3")
label5.pack(side="top")

# Create the first button and place it in the root window
button1 = tk.Button(root, text="Button 1")
button1.pack(side="top")

# Create the second button and place it in the root window
button2 = tk.Button(root, text="Button 2")
button2.pack(side="top")

# Create the third button and place it in the root window
button3 = tk.Button(root, text="Button 3")
button3.pack(side="top")

# Create the exit button and place it in the root window
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(side="bottom")

# Define the first callback function
def on_button1_clicked():
    print("Button 1 was clicked!")

# Define the second callback function
def on_button2_clicked():
    print("Button 2 was clicked!")

# Define the third callback function
def on_button3_clicked():
    print("Button 3 was clicked!")

# Connect the first button to the first callback function
button1.configure(command=on_button1_clicked)

# Connect the second button to the second callback function
button2.configure(command=on_button2_clicked)

# Connect the third button to the third callback function
button3.configure(command=on_button3_clicked)

# Start the event loop
root.mainloop()
