from tkinter import *
import random

root = Tk()

root.title("Random Word Generator")
root.geometry("500x500")
root.configure(bg = "light blue")

label1 = Label(root, bg = "red")

def rwg():
    alpha_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    rn1 = random.randint(0,25)
    rn2 = random.randint(0,25)
    rn3 = random.randint(0,25)
    rn4 = random.randint(0,25)
    rn5 = random.randint(0,25)
    print(rn1, rn2, rn3, rn4, rn5)
    ra1 = alpha_list[rn1]
    ra2 = alpha_list[rn2]
    ra3 = alpha_list[rn3]
    ra4 = alpha_list[rn4]
    ra5 = alpha_list[rn5]
    
    label1["text"] = ra1+ra2+ra3+ra4+ra5
    
btn1 = Button(root, text = "Generate Random Word", command = rwg, bg = "red")
btn1.place(relx = 0.49, rely = 0.4, anchor = CENTER)
label1.place(relx = 0.51, rely = 0.5, anchor = CENTER)

root.mainloop()
